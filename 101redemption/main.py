import cv2
import lzma
import os, sys
import imghdr
import argparse
import numpy as np


class Mayday:
    def __init__(self, image:str, payload:str) -> None:
        stream_delimiter = b'#!busted!#'
        img = cv2.imread(image)

        if payload:
            with open(payload, 'rb') as infile:
                payload = infile.read() + stream_delimiter + payload.encode('utf8') + stream_delimiter
            if not payload:
                print('No payload!')
                sys.exit(1)
            enc = lzma.compress(payload)
            print('Encoding payload...')
            Mayday.encodeData(img, enc)
            cv2.imwrite(f'secret_{image}', img)
        else:
            print('Decoding payload...')
            encr = Mayday.decodeData(img)
            payload = lzma.decompress(encr)
            parts = [i for i in payload.split(stream_delimiter) if i]
            for i in range(len(parts)):
                if i % 2 == 0:
                    continue
                with open(parts[i],'wb') as outfile:
                    outfile.write(parts[i-1])

    @classmethod
    def toBits(cls, data):
        if type(data) == str:
            return ''.join([f'{ord(i):08b}' for i in data])
        elif type(data) == bytes or type(data) == np.ndarray:
            return [f'{i:08b}' for i in data]
        elif type(data) == int or type(data) == np.uint8:
            return f'{data:08b}'
        print('Data type not supported!')
        sys.exit(1)

    @classmethod
    def decodeData(cls, image: np.ndarray) -> bytes:
        out = ''
        stopflag = Mayday.toBits('#.ke.#')
        for value in image:
            for pixel in value:
                b,g,r = Mayday.toBits(pixel)
                if b[-1] == '0':
                    out += g[-1]
                else:
                    out += r[-1]
            if stopflag in out:
                break
        out = out.split(stopflag)[0]
        out = [int(out[i:i+8],2) for i in range(0,len(out),8)]
        return bytearray(out)

    @classmethod
    def encodeData(cls,image: np.ndarray, secret: bytes):
        stopflag = Mayday.toBits('#.ke.#')
        secret_bits = ''.join(Mayday.toBits(secret)) + stopflag
        ###
        h, w, channels = image.shape
        if channels != 3:
            print(f'Invalid channel count in image! {channels}')
            sys.exit(1)
        # 
        pixels = h * w
        bit_len = len(secret_bits)
        max_bit_len = pixels * (channels-1)
        #
        if bit_len > max_bit_len:
            print(f'Not enough bits! extra required: {len(secret_bits)-max_bit_len}')
            sys.exit(1)

        done = False
        bit_index = 0
        for value in image:
            for pixel in value:
                b,g,r = Mayday.toBits(pixel)
                if b[-1] == '0':
                    if bit_index < bit_len:
                        pixel[1] = int(g[:-1] + secret_bits[bit_index],2)
                        bit_index += 1
                    else:
                        done = True
                        break
                elif bit_index < bit_len:
                    pixel[2] = int(r[:-1] + secret_bits[bit_index],2)
                    bit_index += 1
                else:
                    done = True
                    break
            if done:
                break
        assert(Mayday.decodeData(image) == secret)
        print('Encoding successfull.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # validate image
    def valid_image(img: str):
        if imghdr.what(img) != 'png':
            parser.error('Only *.png is supported!')
        return img

    parser.add_argument('-p', dest='payload', help='binary payload to be encoded in image')
    parser.add_argument('image', type=lambda s:valid_image(s))
    args = parser.parse_args()
    Mayday(args.image, args.payload)

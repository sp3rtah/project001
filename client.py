from socket import socket, AF_INET, SOCK_STREAM

client = socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1', 5054))

headers = client.recv(64)

headers = headers.decode('utf8').strip()
msg_len = int(headers)
print(f'Receiving message of size: {msg_len}')

storage = list()

while True:
    data = client.recv(4096)

    if not data:
        break
    storage.append(data)

if not storage:
    raise RuntimeError('No image data received!')

new_file_name = 'image-network.jpg'

with open(new_file_name, 'wb') as image_file:
    for part in storage:
        image_file.write(part)
    print('Image saved successfully!')
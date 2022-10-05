from socket import socket, AF_INET, SOCK_STREAM


CONFIG = ('127.0.0.1', 5054)

serv_socket = socket(AF_INET, SOCK_STREAM)
print('Socket created successfully...')

serv_socket.bind(CONFIG)
print('Configuring socket options...')

serv_socket.listen()
print('Server waiting for connections...')


connection, addr = serv_socket.accept()
print(f'Client connected from: {addr}')

file_name = 'image.jpg'

with open(file_name,'rb') as image:
    image_bytes = image.read()

    msg_len = len(image_bytes)
    headers = str(msg_len).rjust(64).encode('utf8')
    connection.send(headers)


    bytes_sent = connection.send(image_bytes)

    if bytes_sent != len(image_bytes):
        raise RuntimeError('Message not fully sent!')
    else:
        print('Image sent successfully.')

print('Server shutting down...')


import socket

HOST = ''
PORT = 55555

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

while True:
    data = sock.recv(1024).decode('utf-8')
    print(data)
    sock.send('send test data'.encode('utf-8'))

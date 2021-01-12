import socket

HOST = socket.gethostbyname(socket.gethostname()) 
PORT = 12345 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

while True:
    data_length = sock.recv(50).decode('utf-8')
    data = sock.recv(int(data_length)).decode('utf-8')
    print(data)
    sock.send('send Ack'.encode('utf-8'))

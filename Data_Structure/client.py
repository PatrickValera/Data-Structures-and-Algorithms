# # import socket
# # s=socket.socket()
# # s.connect(("0.0.0.0",5003))

# # msg=s.recv(1024)
# # print(msg.decode("utf-8"))

# import time
# import socket
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(('0.0.0.0', 5371))
# # client.settimeout(3)
# # time.sleep(3)
# #client.send(str.encode('client'))
# # connection, address = client.accept()
# fromServer = client.recv(2048)
# fromServer = fromServer.decode('utf-8')
# client.close()
# print(fromServer)


import sys
import socket

SERVER = "0.0.0.0"
PORT = 5371

if sys.argv[1] == "client":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as skt:
        skt.connect((SERVER, PORT))
        while True:
            msg = input("> ")
            skt.sendall(msg.encode('utf-8'))
            if msg=="end": break
            data = skt.recv(1024).decode('utf-8')
            print(f'>>> {data}')

if sys.argv[1] == "server":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as skt:
        skt.bind((SERVER, PORT))
        skt.listen()
        conn, address =skt.accept()
        with conn:
            print(f"Connected to from IP {address}")
            while True:
                data = conn.recv(1024)
                if data:
                    msg=data.decode('utf-8')
                    cmd=msg.split()
                    if cmd[0]=="reverse":
                        msg=""
                        for c in cmd[1]:
                            msg = c+ msg


                    print(msg)
                    if msg=="end": break

                    conn.sendall(msg.encode('utf-8'))
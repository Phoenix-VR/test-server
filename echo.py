import socket

server_soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_soc.bind('0.0.0.0',80)
server_soc.listen()
while True:
    client_soc,addr = server_soc.accept()
    req_body = client_soc.recv(1024)
    client_soc.sendall("message from server: hello".encode())
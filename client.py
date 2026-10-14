import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('127.0.0.1', 6080))
    
    while True:
        data = s.recv(1024)
        print(data.decode())
        inputs = input("Input to the server: ")
        s.sendall(inputs.encode())
        

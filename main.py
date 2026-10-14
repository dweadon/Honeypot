import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("127.0.0.1", 6080))
    s.listen(5)
    (client, addr) = s.accept()
    with client:
        attempts = 0
        passw = 'Enter password please'
        client.sendall(passw.encode())
        while True:
            password = client.recv(1024)
            if not password: break
            print("User tried: ",password)
            attempts = attempts+1 
            print('Attempts: ', attempts)                 
            if b'/@#!##$@!$!#@$!@#@OLJldkjfsjdsfiuj@#!@' in password:
                rate = b'Please rate our honeypot out of 10 in interpol.com'
                client.sendall(rate)
                break
            elif attempts == 3:
                client.sendall('Too bad...'.encode())
                client.close()
                break
            else:
                error = b'Incorrect password, please try again'
                client.sendall(error)
                

import socket

host, port = ('', 5566)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
print("Démmarage en cours...")

while True:
    socket.listen(5)
    conn, adress = socket.accept()

    data = conn.recv()
    data = data.decode()
    print(data)


conn.close()
socket.close()
    

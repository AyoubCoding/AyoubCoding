import socket

host, port = ('localhost', 5566)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Démmarage en cours...")

try:
    socket.connect((host, port))
    print("Connected")

    data = "Je suis un développeur et un électronicien :-)"
    data = data.encode("utf8")
    socket.sendall(data)
except ConnectionRefusedError:
    print("Connexion failed :-(")
finally:
    socket.close()
    

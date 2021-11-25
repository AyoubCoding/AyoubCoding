import socket
import threading

class ThreadForClient(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.conn = conn
    def run(self):
        data = self.conn.recv(2048)
        data = data.decode()
        print(data)

host, port = ('', 5566)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
print("Démmarage en cours...")

while True:
    socket.listen(5)
    conn, adress = socket.accept()

    thread = ThreadForClient(conn)
    thread.start()
    thread = ThreadForClient(conn)
    thread.start()
conn.close()
socket.close()
    

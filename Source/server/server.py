
import socket

import config as cfg


class Server:

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = cfg.HOST_IP
        self.port = cfg.HOST_PORT

        self.socket.bind((self.host, self.port))
        self.socket.listen(1)
        self.connection, self.address = self.socket.accept()
        print(f"Client {self.address} is connected!")

        while True:
            data = bytes(input('write to client: '), encoding='utf8')
            self.connection.send(data)

            data = self.connection.recv(1024)

            if not data:
                self.connection.close()
                exit()
            else:
                print(data.decode('utf8'))

    def __del__(self):
        self.connection.close()


if __name__ == "__main__":
    server = Server()

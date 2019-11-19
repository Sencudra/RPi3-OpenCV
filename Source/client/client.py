
import socket

import config as cfg


class Client:

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = cfg.HOST_IP
        self.port = cfg.HOST_PORT

        self.socket.connect((self.host, self.port))

        while True:
            data = bytes(input('write to server: '), encoding='utf8')

            if not data:
                self.socket.close()
                exit(1)
            else:
                self.socket.send(data)

            received_data = self.socket.recv(2014)
            print(received_data.decode('utf8'))

    def __del__(self):
        self.socket.close()


if __name__ == "__main__":
    client = Client()


import socket
import logging as log

import config as cfg


class Client:
    """
        Just sending data without any checks.
    """

    def __init__(self, to_ip, with_port):
        self.ip = to_ip
        self.port = with_port
        self.socket = socket.socket(socket.AF_INET,
                                    socket.SOCK_STREAM)
        self.socket.settimeout(1)

        try:
            self.socket.connect((self.ip, self.port))
        except socket.error as e:
            log.error(f"Client - {e}")

    def send_data(self, data):
        log.info("Client - Sending data...")

        if not data:
            print("Client - No data to send.")
            return

        try:
            self.socket.sendall(bytes(data))
        except socket.error as e:
            log.error(f"Client - {e}")

    def __del__(self):
        self.socket.close()

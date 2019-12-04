
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
        self.socket.settimeout(cfg.SOCKET_TIMEOUT)

        try:
            self.socket.connect((self.ip, self.port))
        except socket.error as e:
            log.error("Client - {message}".format(message=e))

    def send_data(self, data):
        if not data:
            log.warning("Client - No data to send.")
            return

        log.info("Client - Sending {data}".format(data=data))
        try:
            array_to_send = bytes(str(data), encoding=cfg.DEFAULT_ENCODING)
            self.socket.sendall(array_to_send)
        except socket.error as e:
            log.error("Client - {message}".format(message=e))

    def __del__(self):
        log.info("Client - Closing socket!")
        self.socket.close()

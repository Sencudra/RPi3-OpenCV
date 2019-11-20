
import socket
import logging as log

import config as cfg


class Client:
    """
        Just sending data without any checks.
    """

    def __init__(self):
        pass

    def send_data(self, data, to_ip, with_port):
        log.info("Client - Sending data...")

        if not data:
            print("Client - No data to send.")
            return

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.settimeout(1)
                s.connect((to_ip, with_port))
                s.sendall(bytes(data, enconding=cfg.DEFAULT_ENCODING))
                s.close()
            except socket.timeout as error:
                log.error(f"Client - {error}")

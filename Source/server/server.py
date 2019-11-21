
import socket
import logging as log


class Server:
    """
        Receives data from client.
    """

    def __init__(self, ip, port, container):
        """
            Possible errors:
                - 10048 - The port is buzy
                - 10049 - The ip:port differs from machine's

        """

        log.info("Server - Initialising. Receiving data...")

        self.ip = ip
        self.port = port
        self.container = container

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

            try:
                s.bind((ip, port))
                s.listen()
                log.info("Server - Waiting for incoming connections...")
                conn, addr = s.accept()

                with conn:
                    log.info(f"Server - Connected by {addr}")
                    while True:
                        data = conn.recv(4).decode()
                        if data:
                            log.info(f"Server - received {data}")
                            container.append(data)
            except socket.error as e:
                log.error(f"Server - {e}")


import socket
import logging as log
import threading as thr


class Server:
    """
        Receives data from client.
    """

    def __init__(self, ip, port, container):
        log.info(f"Server - [{ip}:{port}] Initialising...")

        self.ip = ip
        self.port = port
        self.container = container
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.thread = None

    def start(self):
        log.info("Server - Starting server...")
        with self.socket as s:
            try:
                s.bind((self.ip, self.port))
                s.listen()

                while True:
                    log.info("Server - Waiting for incoming connections...")
                    conn, addr = s.accept()
                    self.thread = thr.Thread(target=self.__handle_new_client,
                                             args=(conn, addr),
                                             daemon=True)
                    self.thread.start()
            except socket.error as e:
                log.error(f"Server - {e}")

    def __handle_new_client(self, socket_connection, address):
        log.info(f"Server - Handling connection from {address}")
        while True:
            try:
                data = socket_connection.recv(1024).decode()
                log.info(f"Server - Received data {data} from {address}")
                if not data:
                    break
                self.container.append(data)
            except socket.error as e:
                log.warning(e)
                break
        log.info(f"Server - Finishing handling connection from {address}")

    def __del__(self):
        log.info("Server - Closing socket")
        self.socket.close()

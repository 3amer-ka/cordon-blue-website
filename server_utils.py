import socket
import socketserver
import threading
import time
from http.server import SimpleHTTPRequestHandler

PORT = 8000
Handler = SimpleHTTPRequestHandler

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

class MyServer(threading.Thread):
    def __init__(self, port=PORT):
        super().__init__()
        self.port = port
        self.httpd = None
        self.server_started = threading.Event()

    def run(self):
        with ReusableTCPServer(("", self.port), Handler) as httpd:
            self.httpd = httpd
            self.port = httpd.server_address[1]
            self.server_started.set()
            httpd.serve_forever()

    def stop(self):
        if self.httpd:
            self.httpd.shutdown()
            self.httpd.server_close()

def wait_for_server(port, timeout=5.0):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            with socket.create_connection(("localhost", port), timeout=0.1):
                return True
        except OSError:
            time.sleep(0.05)
    return False

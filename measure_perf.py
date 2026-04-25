import urllib.request
import time
import os

from http.server import SimpleHTTPRequestHandler
import socketserver
import threading

import socket

def wait_for_server(port):
    start_time = time.time()
    while time.time() - start_time < 5.0:
        try:
            with socket.create_connection(("localhost", port), timeout=0.1):
                return
        except OSError:
            time.sleep(0.01)

PORT = 8000
Handler = SimpleHTTPRequestHandler

class MyServer(threading.Thread):
    def __init__(self):
        super().__init__()
        socketserver.TCPServer.allow_reuse_address = True
        self.httpd = socketserver.TCPServer(("", PORT), Handler)

    def run(self):
        self.httpd.serve_forever()

    def stop(self):
        self.httpd.shutdown()
        self.httpd.server_close()

server = MyServer()
server.start()

# wait for server to start using socket polling
wait_for_server(PORT)

try:
    start_time = time.time()
    response = urllib.request.urlopen(f'http://localhost:{PORT}/index.html')
    html = response.read()

    # fetch the main image
    img_start = time.time()
    img_response = urllib.request.urlopen(f'http://localhost:{PORT}/assets/images/resort-design.jpg')
    img_data = img_response.read()
    img_end = time.time()

    end_time = time.time()

    print(f"HTML size: {len(html)} bytes")
    print(f"Image size: {len(img_data) / 1024 / 1024:.2f} MB")
    print(f"Image load time: {img_end - img_start:.3f} seconds")
    print(f"Total basic load time: {end_time - start_time:.3f} seconds")
finally:
    server.stop()

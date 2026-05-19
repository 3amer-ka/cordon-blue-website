import urllib.request
import time
import os
import socket

from http.server import SimpleHTTPRequestHandler
import socketserver
import threading

PORT = 8000
Handler = SimpleHTTPRequestHandler

class ReuseTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

class MyServer(threading.Thread):
    def __init__(self, port):
        super().__init__()
        self.httpd = ReuseTCPServer(("", port), Handler)
    def run(self):
        self.httpd.serve_forever()
    def stop(self):
        self.httpd.shutdown()
        self.httpd.server_close()

server = MyServer(PORT)
server.start()

# wait for server to start
for _ in range(50):
    try:
        socket.create_connection(("localhost", PORT), timeout=0.1).close()
        break
    except OSError:
        time.sleep(0.05)

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

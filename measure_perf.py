import urllib.request
import time
import os
import socket

from http.server import SimpleHTTPRequestHandler
import socketserver
import threading

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

# ⚡ Bolt Optimization: Replace synchronous time.sleep() with socket polling
# This significantly reduces script execution time and improves measurement accuracy.
def wait_for_server(port, timeout=5.0):
    start = time.time()
    while time.time() - start < timeout:
        try:
            with socket.create_connection(("localhost", port), timeout=0.1):
                return True
        except (OSError, ConnectionRefusedError):
            time.sleep(0.01)
    return False

if not wait_for_server(PORT):
    print("Server failed to start")
    server.stop()
    exit(1)

try:
    start_time = time.time()
    response = urllib.request.urlopen(f'http://localhost:{PORT}/index.html')
    html = response.read()

    # fetch the main image
    img_start = time.time()
    try:
        img_response = urllib.request.urlopen(f'http://localhost:{PORT}/assets/images/resort-design.jpg')
        img_data = img_response.read()
    except Exception as e:
        img_data = b''
    img_end = time.time()

    end_time = time.time()

    print(f"HTML size: {len(html)} bytes")
    print(f"Image size: {len(img_data) / 1024 / 1024:.2f} MB")
    print(f"Image load time: {img_end - img_start:.3f} seconds")
    print(f"Total basic load time: {end_time - start_time:.3f} seconds")
finally:
    server.stop()

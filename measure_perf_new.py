import urllib.request
import time

from http.server import SimpleHTTPRequestHandler
import socketserver
import threading

PORT = 8001
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

import socket
# ⚡ Bolt Optimization: Replace synchronous time.sleep(1) with a socket polling loop.
# This prevents artificially inflating test execution time by waiting only as long as necessary for the server to bind and start.
# wait for server to start
for _ in range(20):
    try:
        socket.create_connection(("localhost", PORT), timeout=0.1)
        break
    except OSError:
        time.sleep(0.05)

try:
    start_time = time.time()
    response = urllib.request.urlopen(f'http://localhost:{PORT}/index.html')
    html = response.read()

    # fetch the main image fallback (as the python script won't parse srcset)
    img_start = time.time()
    img_response = urllib.request.urlopen(f'http://localhost:{PORT}/assets/images/resort-design-optimized.jpg')
    img_data = img_response.read()
    img_end = time.time()

    end_time = time.time()

    print(f"HTML size: {len(html)} bytes")
    print(f"Image size: {len(img_data) / 1024 / 1024:.2f} MB")
    print(f"Image load time: {img_end - img_start:.3f} seconds")
    print(f"Total basic load time: {end_time - start_time:.3f} seconds")
finally:
    server.stop()

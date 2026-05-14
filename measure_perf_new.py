import urllib.request
import time
import socket

from http.server import SimpleHTTPRequestHandler
import socketserver
import threading

PORT = 8001
Handler = SimpleHTTPRequestHandler

class MyServer(threading.Thread):
    def __init__(self):
        super().__init__()
        # ⚡ Bolt Optimization: Instantiate the server in __init__ with allow_reuse_address
        # This ensures the server object is fully ready and bound to the port before
        # the thread runs, preventing race conditions where self.httpd is undefined
        # when stop() is called, and avoiding "Address already in use" errors across runs.
        socketserver.TCPServer.allow_reuse_address = True
        self.httpd = socketserver.TCPServer(("", PORT), Handler)

    def run(self):
        self.httpd.serve_forever()

    def stop(self):
        self.httpd.shutdown()
        self.httpd.server_close()

server = MyServer()
server.start()

# ⚡ Bolt Optimization: Replace slow sleep(1) with fast socket polling
# This drops startup waiting time from a flat 1000ms down to ~1-10ms
# by connecting to the port as soon as the server is actually listening.
start_wait = time.time()
while time.time() - start_wait < 5:
    try:
        with socket.create_connection(("localhost", PORT), timeout=0.1):
            break
    except OSError:
        time.sleep(0.01)

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

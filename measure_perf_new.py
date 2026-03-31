import urllib.request
import time
import os

from http.server import SimpleHTTPRequestHandler
import socketserver
import threading

PORT = 8001
Handler = SimpleHTTPRequestHandler

class MyServer(threading.Thread):
    def run(self):
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            self.httpd = httpd
            httpd.serve_forever()
    def stop(self):
        self.httpd.shutdown()
        self.httpd.server_close()

server = MyServer()
server.start()

# wait for server to start
time.sleep(1)

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

import urllib.request
import time
import socket
import argparse

from http.server import SimpleHTTPRequestHandler
import socketserver
import threading

Handler = SimpleHTTPRequestHandler

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

class MyServer(threading.Thread):
    def __init__(self, port=8000):
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

def main():
    parser = argparse.ArgumentParser(description="Measure load performance of local web server.")
    parser.add_argument('--port', type=int, default=8000, help="Port to run the local server on")
    parser.add_argument('--image', type=str, default="/assets/images/resort-design.jpg", help="Path to the image to measure load time")
    args = parser.parse_args()

    server = MyServer(port=args.port)
    server.start()

    # Wait up to 2 seconds for the server to bind and start
    if not server.server_started.wait(timeout=2.0):
        print("Failed to start server within timeout.")
        server.stop()
        server.join()
        return

    try:
        start_time = time.time()
        response = urllib.request.urlopen(f'http://localhost:{server.port}/index.html')
        html = response.read()

        # fetch the main image
        img_start = time.time()
        img_response = urllib.request.urlopen(f'http://localhost:{server.port}{args.image}')
        img_data = img_response.read()
        img_end = time.time()

        end_time = time.time()

        print(f"HTML size: {len(html)} bytes")
        print(f"Image size: {len(img_data) / 1024 / 1024:.2f} MB")
        print(f"Image load time: {img_end - img_start:.3f} seconds")
        print(f"Total basic load time: {end_time - start_time:.3f} seconds")
    finally:
        server.stop()
        server.join()

if __name__ == '__main__':
    main()

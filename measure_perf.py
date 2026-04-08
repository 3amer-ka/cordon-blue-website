import urllib.request
import time
import os
import argparse
from http.server import SimpleHTTPRequestHandler
import socketserver
import threading

Handler = SimpleHTTPRequestHandler

class MyServer(threading.Thread):
    def __init__(self, port):
        super().__init__()
        self.port = port
        self.httpd = None

    def run(self):
        with socketserver.TCPServer(("", self.port), Handler) as httpd:
            self.httpd = httpd
            httpd.serve_forever()

    def stop(self):
        if self.httpd:
            self.httpd.shutdown()
            self.httpd.server_close()

def main():
    parser = argparse.ArgumentParser(description="Measure performance of fetching an image from a local server.")
    parser.add_argument("--port", type=int, default=8000, help="Port to run the local server on (default: 8000)")
    parser.add_argument("--image", type=str, default="/assets/images/resort-design.jpg", help="Path of the image to fetch (default: /assets/images/resort-design.jpg)")
    args = parser.parse_args()

    port = args.port
    image_path = args.image

    # ensure the path starts with a slash
    if not image_path.startswith('/'):
        image_path = '/' + image_path

    server = MyServer(port)
    server.start()

    # wait for server to start
    time.sleep(1)

    try:
        start_time = time.time()
        response = urllib.request.urlopen(f'http://localhost:{port}/index.html')
        html = response.read()

        # fetch the main image
        img_start = time.time()
        img_response = urllib.request.urlopen(f'http://localhost:{port}{image_path}')
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

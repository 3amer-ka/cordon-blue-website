import urllib.request
import time
import socket

from http.server import SimpleHTTPRequestHandler
import socketserver
import threading

PORT = 8000
Handler = SimpleHTTPRequestHandler

class MyServer(threading.Thread):
    def __init__(self, port=PORT):
        super().__init__()
        socketserver.TCPServer.allow_reuse_address = True
        self.httpd = socketserver.TCPServer(("", port), Handler)
        self.port = self.httpd.server_address[1]

    def run(self):
        with self.httpd:
            self.httpd.serve_forever()

    def stop(self):
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

def main():
    # Pass 0 to use an ephemeral port to prevent 'Address already in use'
    server = MyServer(port=0)
    server.start()

    if not wait_for_server(server.port):
        print("Failed to start server")
        server.stop()
        return

    try:
        start_time = time.time()
        response = urllib.request.urlopen(f'http://localhost:{server.port}/index.html')
        html = response.read()

        # fetch the main image
        img_start = time.time()
        img_response = urllib.request.urlopen(f'http://localhost:{server.port}/assets/images/resort-design.jpg')
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

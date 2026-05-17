import urllib.request
import time
from http.server import SimpleHTTPRequestHandler
import socketserver
import threading
import os
import sys

PORT = 3000
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
time.sleep(1)

try:
    with open('projects.html', 'r') as f:
        content = f.read()
        if 'loading="lazy"' in content and 'admin-tower.jpg' in content and 'polivard-city.jpg' in content:
            print("Frontend verification passed: loading=lazy is present.")
            sys.exit(0)
        else:
            print("Frontend verification failed.")
            sys.exit(1)
finally:
    server.stop()

import urllib.request
import time

from server_utils import MyServer

def main():
    server = MyServer(port=8001)
    server.start()

    server.server_started.wait(timeout=2.0)

    try:
        start_time = time.time()
        response = urllib.request.urlopen(f'http://localhost:{server.port}/index.html')
        html = response.read()

        img_start = time.time()
        img_response = urllib.request.urlopen(f'http://localhost:{server.port}/assets/images/resort-design-optimized.jpg')
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

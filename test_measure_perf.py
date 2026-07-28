import unittest
import threading
import time
import socket
import urllib.request
import urllib.error
from measure_perf import MyServer

def wait_for_server(port, timeout=5.0):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            with socket.create_connection(("localhost", port), timeout=0.1):
                return True
        except OSError:
            time.sleep(0.05)
    return False

class TestMeasurePerf(unittest.TestCase):
    def test_server_start_stop(self):
        # Using port 0 allows the OS to assign an available random port
        # This prevents "Address already in use" errors during testing
        server = MyServer(port=0)
        port = server.port

        try:
            # Start the server
            server.start()

            # Wait for server to be ready
            self.assertTrue(wait_for_server(port, timeout=2.0))

            # Verify we can make a connection
            with socket.create_connection(("localhost", port), timeout=1.0):
                pass # Connection successful

        finally:
            # Stop the server
            server.stop()
            server.join(timeout=2.0)

            # Verify server is closed
            self.assertFalse(server.is_alive())
            self.assertFalse(wait_for_server(port, timeout=0.5))

if __name__ == '__main__':
    unittest.main()

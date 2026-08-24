import unittest
import threading
import time
import socket
import urllib.request
import urllib.error
from server_utils import MyServer, wait_for_server

class TestMeasurePerf(unittest.TestCase):
    def test_server_start_stop(self):
        # Using port 0 allows the OS to assign an available random port
        # This prevents "Address already in use" errors during testing
        server = MyServer(port=0)

        try:
            # Start the server
            server.start()

            # Wait for server to be ready
            self.assertTrue(server.server_started.wait(timeout=2.0))
            port = server.port

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

from unittest.mock import patch, MagicMock
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


    @patch('measure_perf.MyServer')
    @patch('measure_perf.wait_for_server')
    @patch('urllib.request.urlopen')
    def test_main_success(self, mock_urlopen, mock_wait, mock_server_cls):
        from measure_perf import main
        mock_server = MagicMock()
        mock_server.port = 8080
        mock_server_cls.return_value = mock_server
        mock_wait.return_value = True

        mock_resp1 = MagicMock()
        mock_resp1.read.return_value = b'html'
        mock_resp2 = MagicMock()
        mock_resp2.read.return_value = b'img'
        mock_urlopen.side_effect = [mock_resp1, mock_resp2]

        main()

        mock_server_cls.assert_called_once_with(port=0)
        mock_server.start.assert_called_once()
        mock_wait.assert_called_once_with(8080)
        self.assertEqual(mock_urlopen.call_count, 2)
        mock_server.stop.assert_called_once()
        mock_server.join.assert_called_once()

    @patch('measure_perf.MyServer')
    @patch('measure_perf.wait_for_server')
    @patch('urllib.request.urlopen')
    def test_main_server_failure(self, mock_urlopen, mock_wait, mock_server_cls):
        from measure_perf import main
        mock_server = MagicMock()
        mock_server.port = 8080
        mock_server_cls.return_value = mock_server
        mock_wait.return_value = False

        main()

        mock_server.start.assert_called_once()
        mock_wait.assert_called_once_with(8080)
        mock_urlopen.assert_not_called()
        mock_server.stop.assert_called_once()

if __name__ == '__main__':
    unittest.main()

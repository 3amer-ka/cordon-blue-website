import unittest
from unittest.mock import patch, MagicMock
import threading
import time
import socket
import urllib.request
import urllib.error
import io
import sys
from contextlib import redirect_stdout
from measure_perf import MyServer
import measure_perf

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

    @patch('measure_perf.MyServer')
    @patch('urllib.request.urlopen')
    def test_main_logic(self, mock_urlopen, mock_MyServer):
        mock_server_instance = MagicMock()
        mock_server_instance.port = 1234
        # Simulate successful wait
        mock_server_instance.server_started.wait.return_value = True
        mock_MyServer.return_value = mock_server_instance

        mock_html_response = MagicMock()
        mock_html_response.read.return_value = b'<html></html>'

        mock_img_response = MagicMock()
        mock_img_response.read.return_value = b'image data'

        mock_urlopen.side_effect = [mock_html_response, mock_img_response]

        # Use an empty argument list so argparse doesn't pick up the unittest args
        test_args = ["measure_perf.py", "--port", "1234", "--image", "/assets/images/resort-design.jpg"]
        with patch.object(sys, 'argv', test_args):
            f = io.StringIO()
            with redirect_stdout(f):
                measure_perf.main()

            output = f.getvalue()

            self.assertIn("HTML size: 13 bytes", output)
            self.assertIn("Image size: 0.00 MB", output)

            self.assertEqual(mock_urlopen.call_count, 2)
            mock_server_instance.stop.assert_called_once()
            mock_server_instance.join.assert_called_once()

            # Verify URL calls
            mock_urlopen.assert_any_call('http://localhost:1234/index.html')
            mock_urlopen.assert_any_call('http://localhost:1234/assets/images/resort-design.jpg')

if __name__ == '__main__':
    unittest.main()

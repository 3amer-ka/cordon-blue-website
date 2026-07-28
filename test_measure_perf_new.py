import unittest
from unittest.mock import patch, MagicMock
import threading
import time
import socket
import urllib.request
import urllib.error
from measure_perf_new import MyServer
import measure_perf_new
import io
from contextlib import redirect_stdout

def wait_for_server(port, timeout=5.0):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            with socket.create_connection(("localhost", port), timeout=0.1):
                return True
        except OSError:
            time.sleep(0.05)
    return False

class TestMeasurePerfNew(unittest.TestCase):
    def test_server_start_stop(self):
        server = MyServer(port=0)

        try:
            server.start()
            self.assertTrue(server.server_started.wait(timeout=2.0))
            port = server.port

            with socket.create_connection(("localhost", port), timeout=1.0):
                pass
        finally:
            server.stop()
            server.join(timeout=2.0)
            self.assertFalse(server.is_alive())
            self.assertFalse(wait_for_server(port, timeout=0.5))

    @patch('measure_perf_new.MyServer')
    @patch('urllib.request.urlopen')
    def test_main_logic(self, mock_urlopen, mock_MyServer):
        mock_server_instance = MagicMock()
        mock_server_instance.port = 1234
        mock_MyServer.return_value = mock_server_instance

        mock_html_response = MagicMock()
        mock_html_response.read.return_value = b'<html></html>'

        mock_img_response = MagicMock()
        mock_img_response.read.return_value = b'image data'

        mock_urlopen.side_effect = [mock_html_response, mock_img_response]

        f = io.StringIO()
        with redirect_stdout(f):
            measure_perf_new.main()

        output = f.getvalue()

        self.assertIn("HTML size: 13 bytes", output)
        self.assertIn("Image size: 0.00 MB", output)

        self.assertEqual(mock_urlopen.call_count, 2)
        mock_server_instance.stop.assert_called_once()
        mock_server_instance.join.assert_called_once()

if __name__ == '__main__':
    unittest.main()

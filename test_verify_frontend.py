import unittest
from unittest.mock import MagicMock
from verify_frontend import run_cuj

class TestVerifyFrontend(unittest.TestCase):
    def test_run_cuj(self):
        # Create a mock for the Playwright Page object
        mock_page = MagicMock()

        url = "http://localhost:3000/test.html"
        name = "test_page"

        # Call the function with our mock
        run_cuj(mock_page, url, name)

        # Verify the expected interactions with the mock
        mock_page.goto.assert_called_once_with(url, wait_until='domcontentloaded')

        # wait_for_timeout should be called twice (1000 and 500)
        self.assertEqual(mock_page.wait_for_timeout.call_count, 2)
        mock_page.wait_for_timeout.assert_any_call(1000)
        mock_page.wait_for_timeout.assert_any_call(500)

        # screenshot should be called with the correct path (absolute path)
        import os
        from verify_frontend import VERIFICATION_DIR
        expected_path = os.path.join(VERIFICATION_DIR, 'screenshots', f"{name}.png")
        mock_page.screenshot.assert_called_once_with(path=expected_path)

if __name__ == '__main__':
    unittest.main()

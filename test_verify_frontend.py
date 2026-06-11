import os
import unittest
from unittest.mock import MagicMock, patch
from verify_frontend import run_cuj, VERIFICATION_DIR, block_external_resources, main

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

        # screenshot should be called with the correct path
        expected_path = os.path.join(VERIFICATION_DIR, "screenshots", f"{name}.png")
        mock_page.screenshot.assert_called_once_with(path=expected_path)

    def test_block_external_resources_aborts(self):
        # external URL should be aborted
        mock_route = MagicMock()
        mock_route.request.url = "https://fonts.googleapis.com/css2"

        block_external_resources(mock_route)

        mock_route.abort.assert_called_once()
        mock_route.continue_.assert_not_called()

        mock_route2 = MagicMock()
        mock_route2.request.url = "https://cdn.tailwindcss.com/3.4.1"

        block_external_resources(mock_route2)

        mock_route2.abort.assert_called_once()
        mock_route2.continue_.assert_not_called()

    def test_block_external_resources_continues(self):
        # local or other URLs should continue
        mock_route = MagicMock()
        mock_route.request.url = "http://localhost:3000/index.html"

        block_external_resources(mock_route)

        mock_route.continue_.assert_called_once()
        mock_route.abort.assert_not_called()

    @patch('verify_frontend.run_cuj')
    @patch('verify_frontend.sync_playwright')
    def test_main_resource_cleanup_on_exception(self, mock_sync_playwright, mock_run_cuj):
        # Mock Playwright objects
        mock_context_manager = MagicMock()
        mock_p = MagicMock()
        mock_browser = MagicMock()
        mock_context = MagicMock()

        mock_sync_playwright.return_value = mock_context_manager
        mock_context_manager.__enter__.return_value = mock_p
        mock_p.chromium.launch.return_value = mock_browser
        mock_browser.new_context.return_value = mock_context

        # Make run_cuj throw an exception
        mock_run_cuj.side_effect = Exception("Test Exception")

        # Call main, expecting the exception to propagate
        with self.assertRaisesRegex(Exception, "Test Exception"):
            main()

        # Verify resources were cleaned up despite the exception
        mock_context.close.assert_called_once()
        mock_browser.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()

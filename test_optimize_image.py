import unittest
from unittest.mock import patch, MagicMock
import sys
import os

class TestOptimizeImage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Mock PIL before importing optimize_image to prevent ModuleNotFoundError
        cls.mock_pil = MagicMock()
        sys.modules['PIL'] = cls.mock_pil

    @classmethod
    def tearDownClass(cls):
        # Clean up the mock
        if 'PIL' in sys.modules:
            del sys.modules['PIL']

    @patch('sys.stdout', new_callable=MagicMock)
    def test_missing_image(self, mock_stdout):
        # Import inside the test after the mock has been applied
        from optimize_image import optimize_image

        with patch('optimize_image.Image.open') as mock_open:
            # Arrange
            mock_open.side_effect = Exception("File not found")

            # Act
            result = optimize_image('nonexistent.jpg', './test_dir/')

            # Assert
            self.assertFalse(result)
            mock_open.assert_called_once_with('nonexistent.jpg')

    @patch('os.path.join', side_effect=lambda a, b: f"{a}{b}")
    def test_valid_image(self, mock_path_join):
        # Import inside the test after the mock has been applied
        from optimize_image import optimize_image

        with patch('optimize_image.Image.open') as mock_open:
            # Arrange
            mock_img = MagicMock()
            mock_img.width = 1920
            mock_img.height = 1080
            mock_resized = MagicMock()
            mock_resized.mode = 'RGB'  # explicit mock assignment
            mock_img.resize.return_value = mock_resized
            mock_open.return_value = mock_img

            # Act
            result = optimize_image('valid.jpg', './test_dir/')

            # Assert
            self.assertTrue(result)
            mock_open.assert_called_once_with('valid.jpg')

            # The fallback size (1920x1080) is the same as one of the webp target widths (1920)
            # So resize should only be called 4 times, caching handles the 5th
            self.assertEqual(mock_img.resize.call_count, 4) # 4 widths
            self.assertEqual(mock_resized.save.call_count, 5) # 4 webp + 1 jpg

if __name__ == '__main__':
    unittest.main()

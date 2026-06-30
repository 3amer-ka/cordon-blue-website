import unittest
from unittest.mock import patch, MagicMock
import os
import sys

class TestOptimizeImage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Mock PIL only for this specific test class to avoid polluting the global module namespace
        if 'PIL' not in sys.modules:
            sys.modules['PIL'] = MagicMock()

    @classmethod
    def tearDownClass(cls):
        if 'PIL' in sys.modules and isinstance(sys.modules['PIL'], MagicMock):
            del sys.modules['PIL']

    @patch('optimize_image.Image.open')
    @patch('sys.stdout', new_callable=MagicMock)
    def test_missing_image(self, mock_stdout, mock_open):
        # Import here so that sys.modules mocking has taken effect
        from optimize_image import optimize_image

        # Arrange
        mock_open.side_effect = FileNotFoundError()

        # Act
        result = optimize_image('nonexistent.jpg', './test_dir/')

        # Assert
        self.assertFalse(result)
        mock_open.assert_called_once_with('nonexistent.jpg')

    @patch('optimize_image.Image.open')
    @patch('os.path.join', side_effect=lambda a, b: f"{a}{b}")
    def test_valid_image(self, mock_path_join, mock_open):
        # Import here so that sys.modules mocking has taken effect
        from optimize_image import optimize_image

        # Arrange
        mock_img = MagicMock()
        mock_img.width = 1920
        mock_img.height = 1080
        mock_resized = MagicMock()
        mock_resized.mode = 'RGB'  # Prevents convert() from returning a different mock
        mock_img.resize.return_value = mock_resized
        mock_open.return_value = mock_img

        # Act
        result = optimize_image('valid.jpg', './test_dir/')

        # Assert
        self.assertTrue(result)
        mock_open.assert_called_once_with('valid.jpg')
        self.assertEqual(mock_img.resize.call_count, 4) # 4 widths (fallback uses cache)
        self.assertEqual(mock_resized.save.call_count, 5) # 4 webp + 1 jpg

if __name__ == '__main__':
    unittest.main()

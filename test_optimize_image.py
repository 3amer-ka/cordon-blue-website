import unittest
from unittest.mock import patch, MagicMock
import os
import sys

# Mock PIL for restricted environment testing before importing the target module
sys.modules['PIL'] = MagicMock()
sys.modules['PIL.Image'] = MagicMock()

from optimize_image import optimize_image

class TestOptimizeImage(unittest.TestCase):

    @patch('optimize_image.Image.open')
    @patch('sys.stdout', new_callable=MagicMock)
    def test_missing_image(self, mock_stdout, mock_open):
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
        # Arrange
        mock_img = MagicMock()
        mock_img.width = 1920
        mock_img.height = 1080
        mock_resized = MagicMock()
        mock_img.resize.return_value = mock_resized
        mock_open.return_value = mock_img
        mock_resized.mode = 'RGB'

        # Act
        result = optimize_image('valid.jpg', './test_dir/')

        # Assert
        self.assertTrue(result)
        mock_open.assert_called_once_with('valid.jpg')
        self.assertEqual(mock_img.resize.call_count, 4) # 4 widths, fallback reuses 1920 cache
        self.assertEqual(mock_resized.save.call_count, 5) # 4 webp + 1 jpg

    @patch('optimize_image.Image.open')
    @patch('os.path.join', side_effect=lambda a, b: f"{a}{b}")
    def test_image_conversion_to_rgb(self, mock_path_join, mock_open):
        # Arrange
        mock_img = MagicMock()
        mock_img.width = 1920
        mock_img.height = 1080
        mock_resized = MagicMock()
        mock_img.resize.return_value = mock_resized
        mock_open.return_value = mock_img

        # Test edge case where mode is not RGB
        mock_resized.mode = 'RGBA'

        mock_converted = MagicMock()
        mock_resized.convert.return_value = mock_converted

        # Act
        result = optimize_image('valid.jpg', './test_dir/')

        # Assert
        self.assertTrue(result)
        mock_open.assert_called_once_with('valid.jpg')

        # Verify convert was called
        mock_resized.convert.assert_called_with('RGB')

        # Verify the converted image was saved for the fallback JPG
        mock_converted.save.assert_called_once_with('./test_dir/resort-design-optimized.jpg', 'JPEG', quality=80)

if __name__ == '__main__':
    unittest.main()

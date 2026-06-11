import unittest
from unittest.mock import patch, MagicMock
import os
import io
import sys

# Mock PIL before importing the module to avoid ModuleNotFoundError
sys.modules['PIL'] = MagicMock()

from optimize_hotel_resort import optimize_image

class TestOptimizeHotelResort(unittest.TestCase):

    @patch('optimize_hotel_resort.Image.open')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_missing_image(self, mock_stdout, mock_open):
        # Arrange
        mock_open.side_effect = FileNotFoundError()

        # Act
        result = optimize_image('nonexistent.jpg', './test_dir', 'base')

        # Assert
        self.assertFalse(result)
        mock_open.assert_called_once_with('nonexistent.jpg')
        self.assertIn("Error: Image at nonexistent.jpg not found.", mock_stdout.getvalue())

    @patch('optimize_hotel_resort.Image.open')
    @patch('optimize_hotel_resort.os.path.join', side_effect=lambda a, b: f"{a}/{b}")
    def test_valid_image(self, mock_path_join, mock_open):
        # Arrange
        mock_img = MagicMock()
        mock_img.width = 1920
        mock_img.height = 1080
        mock_img.mode = 'RGB'
        mock_resized = MagicMock()
        mock_img.resize.return_value = mock_resized
        mock_open.return_value = mock_img

        # Act
        result = optimize_image('valid.jpg', './test_dir', 'base')

        # Assert
        self.assertTrue(result)
        mock_open.assert_called_once_with('valid.jpg')
        self.assertEqual(mock_img.resize.call_count, 3) # 2 widths + 1 fallback
        self.assertEqual(mock_resized.save.call_count, 3) # 2 webp + 1 jpg

    @patch('optimize_hotel_resort.Image.open')
    @patch('optimize_hotel_resort.os.path.join', side_effect=lambda a, b: f"{a}/{b}")
    def test_valid_image_rgba(self, mock_path_join, mock_open):
        # Arrange
        mock_img = MagicMock()
        mock_img.width = 1920
        mock_img.height = 1080
        mock_img.mode = 'RGBA'

        mock_resized = MagicMock()
        mock_converted = MagicMock()
        mock_resized.convert.return_value = mock_converted
        mock_img.resize.return_value = mock_resized

        mock_open.return_value = mock_img

        # Act
        result = optimize_image('valid.png', './test_dir', 'base')

        # Assert
        self.assertTrue(result)
        mock_open.assert_called_once_with('valid.png')
        self.assertEqual(mock_img.resize.call_count, 3) # 2 widths + 1 fallback
        self.assertEqual(mock_resized.save.call_count, 2) # 2 webp
        self.assertEqual(mock_converted.save.call_count, 1) # 1 jpg
        mock_resized.convert.assert_called_once_with('RGB')

if __name__ == '__main__':
    unittest.main()

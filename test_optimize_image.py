import sys
from unittest.mock import MagicMock

# Inject PIL mock to avoid ModuleNotFoundError in restricted environments
sys.modules['PIL'] = MagicMock()

import unittest
from unittest.mock import patch
import os
from optimize_image import optimize_image

class TestOptimizeImage(unittest.TestCase):

    @patch('optimize_image.Image.open')
    @patch('sys.stdout', new_callable=MagicMock)
    def test_missing_image(self, mock_stdout, mock_open):
        # Arrange
        mock_open.side_effect = Exception("UnidentifiedImageError")

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
        mock_img.mode = 'RGB'
        mock_resized = MagicMock()
        mock_img.resize.return_value = mock_resized
        mock_open.return_value = mock_img

        # Act
        result = optimize_image('valid.jpg', './test_dir/')

        # Assert
        self.assertTrue(result)
        mock_open.assert_called_once_with('valid.jpg')
        # ⚡ Bolt: Verifying the performance improvement.
        # Fallback resize is no longer called, it uses the cached 1920w object.
        self.assertEqual(mock_img.resize.call_count, 4)
        self.assertEqual(mock_resized.save.call_count, 5) # 4 webp + 1 jpg

if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import patch, MagicMock
import os
import sys

class TestOptimizeImage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mock_pil = MagicMock()
        sys.modules['PIL'] = cls.mock_pil

    @classmethod
    def tearDownClass(cls):
        del sys.modules['PIL']

    @patch('sys.stdout', new_callable=MagicMock)
    def test_missing_image(self, mock_stdout):
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
        from optimize_image import optimize_image
        with patch('optimize_image.Image.open') as mock_open:
            # Arrange
            mock_img = MagicMock()
            mock_img.width = 1920
            mock_img.height = 1080
            mock_img.mode = 'RGB'
            mock_resized = MagicMock()
            mock_resized.mode = 'RGB'
            mock_img.resize.return_value = mock_resized
            mock_open.return_value = mock_img

            # Act
            result = optimize_image('valid.jpg', './test_dir/')

            # Assert
            self.assertTrue(result)
            mock_open.assert_called_once_with('valid.jpg')
            self.assertEqual(mock_img.resize.call_count, 4) # 4 widths, 1 fallback cached
            self.assertEqual(mock_resized.save.call_count, 5) # 4 webp + 1 jpg

if __name__ == '__main__':
    unittest.main()

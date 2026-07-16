import unittest
from unittest.mock import patch, MagicMock
import os
import sys

class TestOptimizeImage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        sys.modules['PIL'] = MagicMock()

    @classmethod
    def tearDownClass(cls):
        if 'PIL' in sys.modules:
            del sys.modules['PIL']

    @patch('sys.stdout', new_callable=MagicMock)
    def test_missing_image(self, mock_stdout):
        # Local import inside the test function after mock is set up
        from optimize_image import optimize_image, Image

        # Arrange
        with patch.object(Image, 'open') as mock_open:
            mock_open.side_effect = Exception("Some error")

            # Act
            result = optimize_image('nonexistent.jpg', './test_dir/')

            # Assert
            self.assertFalse(result)
            mock_open.assert_called_once_with('nonexistent.jpg')

    @patch('os.path.join', side_effect=lambda a, b: f"{a}{b}")
    def test_valid_image(self, mock_path_join):
        # Local import inside the test function after mock is set up
        from optimize_image import optimize_image, Image

        # Arrange
        with patch.object(Image, 'open') as mock_open:
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
            self.assertEqual(mock_img.resize.call_count, 4) # 4 widths, fallback is cached
            self.assertEqual(mock_resized.save.call_count, 5) # 4 webp + 1 jpg

    @patch('os.path.join', side_effect=lambda a, b: f"{a}{b}")
    def test_valid_image_rgba(self, mock_path_join):
        # Test RGBA conversion
        from optimize_image import optimize_image, Image

        # Arrange
        with patch.object(Image, 'open') as mock_open:
            mock_img = MagicMock()
            mock_img.width = 1920
            mock_img.height = 1080
            mock_img.mode = 'RGBA'
            mock_resized = MagicMock()
            mock_resized.mode = 'RGBA'

            mock_converted = MagicMock()
            mock_converted.mode = 'RGB'
            mock_resized.convert.return_value = mock_converted

            mock_img.resize.return_value = mock_resized
            mock_open.return_value = mock_img

            # Act
            result = optimize_image('valid.jpg', './test_dir/')

            # Assert
            self.assertTrue(result)
            mock_resized.convert.assert_called_once_with('RGB')
            # 4 webp saves on resized, 1 jpg save on converted
            self.assertEqual(mock_resized.save.call_count, 4)
            self.assertEqual(mock_converted.save.call_count, 1)

if __name__ == '__main__':
    unittest.main()

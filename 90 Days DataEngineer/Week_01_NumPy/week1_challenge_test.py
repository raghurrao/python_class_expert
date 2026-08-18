import unittest
import numpy as np
import sys
import os

# Adjust path to import the challenge module
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import week1_challenge

class TestWeek1Challenge(unittest.TestCase):

    def setUp(self):
        # Create a mock RGB image of shape (10, 10, 3)
        # Channels: R=100, G=150, B=200
        self.mock_rgb = np.zeros((10, 10, 3), dtype=np.uint8)
        self.mock_rgb[:, :, 0] = 100
        self.mock_rgb[:, :, 1] = 150
        self.mock_rgb[:, :, 2] = 200

    def test_convert_to_grayscale(self):
        gray = week1_challenge.convert_to_grayscale(self.mock_rgb)
        
        self.assertIsInstance(gray, np.ndarray)
        self.assertEqual(gray.shape, (10, 10), "Grayscale image must have shape (H, W).")
        self.assertEqual(gray.dtype, np.uint8, "Result must have dtype uint8.")
        
        # Calculation: 0.2989*100 + 0.5870*150 + 0.1140*200 = 29.89 + 88.05 + 22.8 = 140.74 -> 140
        # Check standard integer conversion
        self.assertEqual(gray[0, 0], 140)

    def test_crop_image(self):
        cropped = week1_challenge.crop_image(self.mock_rgb, 2, 8, 3, 9)
        self.assertEqual(cropped.shape, (6, 6, 3), "Cropped image shape is incorrect.")
        np.testing.assert_array_equal(cropped, self.mock_rgb[2:8, 3:9, :])

    def test_adjust_brightness(self):
        # Dim image by factor of 0.5
        dimmed = week1_challenge.adjust_brightness(self.mock_rgb, 0.5)
        self.assertEqual(dimmed.dtype, np.uint8)
        self.assertEqual(dimmed[0, 0, 0], 50)
        self.assertEqual(dimmed[0, 0, 1], 75)
        self.assertEqual(dimmed[0, 0, 2], 100)
        
        # Brighten image causing overflow
        bright = week1_challenge.adjust_brightness(self.mock_rgb, 2.0)
        self.assertEqual(bright.dtype, np.uint8)
        self.assertEqual(bright[0, 0, 0], 200)
        self.assertEqual(bright[0, 0, 1], 255) # clipped from 300 to 255
        self.assertEqual(bright[0, 0, 2], 255) # clipped from 400 to 255

    def test_invert_colors(self):
        inverted = week1_challenge.invert_colors(self.mock_rgb)
        self.assertEqual(inverted.dtype, np.uint8)
        self.assertEqual(inverted[0, 0, 0], 155) # 255 - 100
        self.assertEqual(inverted[0, 0, 1], 105) # 255 - 150
        self.assertEqual(inverted[0, 0, 2], 55)  # 255 - 200

if __name__ == '__main__':
    unittest.main()

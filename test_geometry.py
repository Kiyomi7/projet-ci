import unittest
from geometry import rectangle_area, rectangle_perimeter, circle_area, circle_circumference

import math

class TestGeometry(unittest.TestCase):

    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(2,4), 8)
        self.assertEqual(rectangle_area(8,8), 64)
        with self.assertRaises(ValueError):
            rectangle_area(-1, 8)

    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle_perimeter(2, 4), 12)
        self.assertEqual(rectangle_perimeter(8, 8), 32)
        with self.assertRaises(ValueError):
            rectangle_perimeter(-1, 8)

    def test_circle_area(self):
        self.assertEqual(circle_area(2), math.pi * 2 * 2)
        self.assertEqual(circle_area(4), math.pi * 4 * 4)
        with self.assertRaises(ValueError):
            circle_area(-2)

    def test_circle_circumference(self):
        self.assertEqual(circle_circumference(2), 2 * math.pi * 2)
        self.assertEqual(circle_circumference(4), 2 * math.pi * 4)
        with self.assertRaises(ValueError):
            circle_circumference(-2)

if __name__ == '__main__':
    unittest.main()

import unittest

from shapes.circle import Circle
from shapes.triangle import Triangle
from shapes.utils import calculate_area

class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 78.53981633974483)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0)

    def test_triangle_is_right_angle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_angle())
        triangle = Triangle(5, 5, 5)
        self.assertFalse(triangle.is_right_angle())

    def test_calculate_area(self):
        circle = Circle(5)
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(calculate_area(circle), 78.53981633974483)
        self.assertAlmostEqual(calculate_area(triangle), 6.0)

if __name__ == "__main__":
    unittest.main()
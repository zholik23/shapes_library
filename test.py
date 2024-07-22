import unittest
from shapes import Circle, Triangle, Rectangle, calculate_area

class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(calculate_area(circle), 78.53981633974483, places=5)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(calculate_area(triangle), 6.0, places=5)

    def test_right_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_triangle())

        non_right_triangle = Triangle(3, 4, 6)
        self.assertFalse(non_right_triangle.is_right_triangle())

    def test_rectangle_area(self):
        rectangle = Rectangle(4, 5)
        self.assertEqual(calculate_area(rectangle), 20)

    def test_no_shape(self):
        with self.assertRaises(ValueError):
            calculate_area()

if __name__ == '__main__':
    unittest.main()

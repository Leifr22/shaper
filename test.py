import unittest
from shape import Circle, Triangle, calculate_area

class TestCircle(unittest.TestCase):
    def test_area(self):
        circle = Circle(2)
        self.assertAlmostEqual(circle.area(), 12.566370614359172)

    def test_invalid_radius(self):
        with self.assertRaises(ValueError):
            Circle(-1)

class TestTriangle(unittest.TestCase):
    def test_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0)

    def test_invalid_sides(self):
        with self.assertRaises(ValueError):
            Triangle(1, 1, 3)
        with self.assertRaises(ValueError):
            Triangle(-1, 2, 2)

    def test_right_angled(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_angled())
        triangle2 = Triangle(5, 5, 5)
        self.assertFalse(triangle2.is_right_angled())

class TestCalculateArea(unittest.TestCase):
    def test_calculate_area(self):
        circle = Circle(2)
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(calculate_area(circle), 12.566370614359172)
        self.assertAlmostEqual(calculate_area(triangle), 6.0)

if __name__ == '__main__':
    unittest.main()
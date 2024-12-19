import unittest
import math


from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter
from circle import area as circle_area, perimeter as circle_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter


class TestSquare(unittest.TestCase):
    def test_area(self):
        self.assertEqual(square_area(4), 16)
        self.assertEqual(square_area(0), 0)
        self.assertEqual(square_area(1), 1)

    def test_perimeter(self):
        self.assertEqual(square_perimeter(4), 16)
        self.assertEqual(square_perimeter(0), 0)
        self.assertEqual(square_perimeter(1), 4)


class TestTriangle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(triangle_area(4, 5), 10)
        self.assertEqual(triangle_area(0, 5), 0)
        self.assertEqual(triangle_area(3, 0), 0)

    def test_perimeter(self):
        self.assertEqual(triangle_perimeter(3, 4, 5), 12)
        self.assertEqual(triangle_perimeter(0, 0, 0), 0)
        self.assertEqual(triangle_perimeter(1, 1, 1), 3)


class TestCircle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(circle_area(4), math.pi * 16)
        self.assertEqual(circle_area(0), 0)
        self.assertEqual(circle_area(1), math.pi * 1)

    def test_perimeter(self):
        self.assertEqual(circle_perimeter(4), math.pi * 4 * 2)
        self.assertEqual(circle_perimeter(0), 0)
        self.assertEqual(circle_perimeter(1), math.pi * 2)


class TestRectangle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(rectangle_area(4, 5), 20)
        self.assertEqual(rectangle_area(0, 5), 0)
        self.assertEqual(rectangle_area(3, 0), 0)

    def test_perimeter(self):
        self.assertEqual(rectangle_perimeter(3, 4), 14)
        self.assertEqual(rectangle_perimeter(0, 0), 0)
        self.assertEqual(rectangle_perimeter(1, 1), 4)


if __name__ == "__main__":
    unittest.main()

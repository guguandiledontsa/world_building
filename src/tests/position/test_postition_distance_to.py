import unittest
from src.main.world_objects.position import Position
from math import sqrt


class MyTestCase(unittest.TestCase):
    def test_distance_to_same_position(self):
        """Test distance to the same position (should be 0)."""
        p1 = Position(1, 2)
        self.assertEqual(p1.distance_to(Position(1, 2)), 0.0)

    def test_distance_to_different_position(self):
        """Test distance between two different positions."""
        p1 = Position(1, 2)
        p2 = Position(4, 6)
        expected_distance = sqrt((4 - 1) ** 2 + (6 - 2) ** 2)
        self.assertAlmostEqual(p1.distance_to(p2), expected_distance)

    def test_distance_to_origin(self):
        """Test distance from a position to the origin (0, 0)."""
        p = Position(3, 4)
        origin = Position(0, 0)
        expected_distance = sqrt(3**2 + 4**2)
        self.assertAlmostEqual(p.distance_to(origin), expected_distance)

    def test_distance_negative_coordinates(self):
        """Test distance between positions with negative coordinates."""
        p1 = Position(-1, -1)
        p2 = Position(3, 3)
        expected_distance = sqrt((3 - (-1)) ** 2 + (3 - (-1)) ** 2)
        self.assertAlmostEqual(p1.distance_to(p2), expected_distance)

    def test_distance_to_large_coordinates(self):
        """Test distance with large coordinate values."""
        p1 = Position(10000, 10000)
        p2 = Position(-10000, -10000)
        expected_distance = sqrt((10000 - (-10000)) ** 2 + (10000 - (-10000)) ** 2)
        self.assertAlmostEqual(p1.distance_to(p2), expected_distance)

    def test_distance_precision(self):
        """Test distance to verify precision with floating-point numbers."""
        p1 = Position(1.000001, 1.000001)
        p2 = Position(1.000002, 1.000002)
        expected_distance = sqrt(
            (1.000002 - 1.000001) ** 2 + (1.000002 - 1.000001) ** 2
        )
        self.assertAlmostEqual(p1.distance_to(p2), expected_distance, places=6)


if __name__ == "__main__":
    unittest.main()

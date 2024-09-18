import unittest
from math import sqrt

from main.world_objects.position import Position, InvalidPositionError
from main.world_objects.degrees import Degrees


class TestPosition(unittest.TestCase):

    def test_initialization(self):
        """Test the initialization of Position instances with valid coordinates."""
        valid_positions = [
            (0, 0),
            (1.5, -2.3),
            (-1, 1),
            (3.14159, 2.71828)
        ]
        for x, y in valid_positions:
            with self.subTest(x=x, y=y):
                pos = Position(x, y)
                self.assertEqual(pos.x, x)
                self.assertEqual(pos.y, y)

    def test_invalid_initialization(self):
        """Test initialization with invalid coordinates."""
        invalid_positions = [
            (None, 1),
            (1, "string"),
            ([], {}),
            (float('nan'), 0),
            (0, float('inf')),
            (1, -float('inf'))
        ]
        for x, y in invalid_positions:
            with self.subTest(x=x, y=y):
                with self.assertRaises(InvalidPositionError):
                    Position(x, y)

    def test_distance_to(self):
        """Test the distance calculation between two Position instances."""
        p1 = Position(0, 0)
        p2 = Position(3, 4)
        self.assertEqual(p1.distance_to(p2), 5)  # 3-4-5 triangle

        p3 = Position(1, 1)
        p4 = Position(4, 5)
        self.assertEqual(p3.distance_to(p4), 5)  # 3-4-5 triangle again

    def test_distance_to_invalid(self):
        """Test handling of invalid distance comparisons."""
        p1 = Position(0, 0)
        with self.assertRaises(ValueError):
            p1.distance_to("not a Position")

    def test_move(self):
        """Test moving the Position by a given angle and steps."""
        pos = Position(0, 0)
        angle = Degrees(90)
        moved_pos = pos.move(angle, 1)
        self.assertEqual(moved_pos.x, 0)  # cos(90°) = 0
        self.assertEqual(moved_pos.y, 1)  # sin(90°) = 1

        angle = Degrees(0)
        moved_pos = pos.move(angle, 1)
        self.assertEqual(moved_pos.x, 1)  # cos(0°) = 1
        self.assertEqual(moved_pos.y, 0)  # sin(0°) = 0

        angle = Degrees(45)
        moved_pos = pos.move(angle, sqrt(2))  # Should move to (1, 1)
        self.assertEqual(moved_pos.x, 1)
        self.assertEqual(moved_pos.y, 1)

    def test_move_invalid_angle(self):
        """Test moving with an invalid angle type."""
        pos = Position(0, 0)
        with self.assertRaises(ValueError):
            pos.move("not an angle", 1)

    def test_is_in(self):
        """Test if a Position is within a defined rectangular area."""
        p = Position(2, 3)
        top_left = Position(1, 4)
        bottom_right = Position(3, 2)

        self.assertTrue(p.is_in(top_left, bottom_right))

        p_outside = Position(4, 3)
        self.assertFalse(p_outside.is_in(top_left, bottom_right))

    def test_is_in_invalid_position(self):
        """Test is_in with invalid Position instances."""
        p = Position(2, 3)
        with self.assertRaises(ValueError):
            p.is_in("not a Position", Position(3, 2))

    def test_addition(self):
        """Test adding two Position instances."""
        p1 = Position(1, 2)
        p2 = Position(3, 4)
        result = p1 + p2
        self.assertEqual(result.x, 4)
        self.assertEqual(result.y, 6)

    def test_subtraction(self):
        """Test subtracting two Position instances."""
        p1 = Position(5, 5)
        p2 = Position(3, 3)
        result = p1 - p2
        self.assertEqual(result.x, 2)
        self.assertEqual(result.y, 2)

    def test_equality(self):
        """Test equality of Position instances."""
        p1 = Position(1, 2)
        p2 = Position(1, 2)
        p3 = Position(2, 1)
        self.assertEqual(p1, p2)
        self.assertNotEqual(p1, p3)

    def test_repr(self):
        """Test the __repr__ method."""
        p = Position(1.234567, 2.345678)
        self.assertEqual(repr(p), "Position(x=1.234567, y=2.345678)")

    def test_str(self):
        """Test the __str__ method."""
        p = Position(1.234567, 2.345678)
        self.assertEqual(str(p), "(1.234567, 2.345678)")

    def test_format_value(self):
        """Test the value formatting in the string representation."""
        self.assertEqual(Position._format_value(1.234567), "1.234567")
        self.assertEqual(Position._format_value(1.0), "1")
        self.assertEqual(Position._format_value(2.71828), "2.718280")


if __name__ == '__main__':
    unittest.main()

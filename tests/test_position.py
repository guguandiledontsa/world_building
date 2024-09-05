import unittest

# Assuming the Position class is defined as follows:
class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Position({self.x}, {self.y})"

    def __str__(self) -> str:
        return f"{self.x}, {self.y}"
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Position):
            return other.x == self.x and other.y == self.y
        return False

class TestPosition(unittest.TestCase):
    def test_initialization(self):
        # Test creation of Position objects
        p = Position(1, 2)
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 2)

    def test_repr(self):
        # Test the __repr__ method
        p = Position(3, 4)
        self.assertEqual(repr(p), "Position(3, 4)")

    def test_str(self):
        # Test the __str__ method
        p = Position(5, 6)
        self.assertEqual(str(p), "5, 6")

    def test_eq_same_position(self):
        # Test equality with same position
        p1 = Position(7, 8)
        p2 = Position(7, 8)
        self.assertEqual(p1, p2)

    def test_eq_different_position(self):
        # Test equality with different position
        p1 = Position(9, 10)
        p2 = Position(10, 9)
        self.assertNotEqual(p1, p2)

    def test_eq_other_object(self):
        # Test equality with an object that is not a Position
        p = Position(11, 12)
        self.assertNotEqual(p, (11, 12))  # Compare with a tuple

    def test_eq_not_position(self):
        # Test equality with an object of a different class
        p = Position(13, 14)
        self.assertNotEqual(p, "Position(13, 14)")  # Compare with a string

if __name__ == "__main__":
    unittest.main()

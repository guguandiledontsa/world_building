import unittest
from main.position import Position


class MyTestCase(unittest.TestCase):
    def test_eq_other_object(self):
        """Test inequality with a non-Position object."""
        self.assertFalse(Position(1,2) == (1, 2))  # Compare with a tuple

    def test_eq_not_position(self):
        """Test inequality with an object of a different class."""
        self.assertFalse(Position(1, 2) == "Position(1, 2)")  # Compare with a string

    def test_same_coord_are_equal(self):
        """Test equality of a Position objects."""
        a = Position(1, 2)
        self.assertTrue(a == Position(1, 2))



if __name__ == '__main__':
    unittest.main()

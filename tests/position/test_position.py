import unittest
from main.position import Position


class TestPosition(unittest.TestCase):

    def setUp(self):
        """Set up test variables."""
        self.p1 = Position(1, 2)
        self.p2 = Position(3, 4)
        self.p3 = Position(1, 2)
        self.p4 = Position(5, 6)

    def test_initialization(self):
        """Test creation of Position objects."""
        self.assertEqual(self.p1.x, 1)
        self.assertEqual(self.p1.y, 2)

    def test_repr(self):
        """Test the __repr__ method."""
        self.assertEqual(repr(self.p2), "Position(x=3, y=4)")

    def test_str(self):
        """Test the __str__ method."""
        self.assertEqual(str(self.p4), "(5, 6)")

    def test_position_inequality(self):
        """Test that two Position objects with different values are not equal."""
        p_diff = Position(2, 3)
        self.assertNotEqual(self.p1, p_diff)

    def test_repr_not_null(self):
        """Ensure the __repr__ method does not return None."""
        self.assertIsNotNone(repr(self.p1))

    def test_str_not_null(self):
        """Ensure the __str__ method does not return None."""
        self.assertIsNotNone(str(self.p1))

    def test_eq_different_position(self):
        """Test inequality of two Position objects with different coordinates."""
        self.assertFalse(self.p1 == self.p2)

    def test_eq_same_position(self):
        """Test equality of two Position objects with the same coordinates."""
        a = Position(1, 2)
        b = Position(1, 2)
        self.assertTrue(a == b)




if __name__ == "__main__":
    unittest.main()

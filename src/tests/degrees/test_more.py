import unittest
from src.main.world_objects.degrees import Degrees, InvalidAngleError

""" The `class TestDegrees` is a test case class that contains multiple test
methods to test the functionality of the `Degrees` class. Each test method
within this test case class focuses on testing specific aspects of the
`Degrees` class, such as initialization, angle normalization, equality
comparisons, hash values, string representations, edge cases, invalid angle
handling, comparisons with non-Degrees objects, turning left and right by
specific degrees, and caching behavior of the normalization function. """


class TestDegrees(unittest.TestCase):

    def test_initialization(self):
        """Test the initialization and normalization of angles."""
        test_cases = [
            (360, 0),
            (-45, 315),
            (720, 0),
            (450, 90),
            (0, 0),
            (180, 180),
            (-720, 0),
            (1080, 0)  # Should normalize to 0
        ]
        for angle, expected in test_cases:
            with self.subTest(angle=angle):
                d = Degrees(angle)
                self.assertEqual(d.angle, expected)

    def test_angle_setter(self):
        """Test angle normalization with setter method."""
        d = Degrees(100)
        with self.assertRaises(AttributeError):
            d.angle = 370  # type: ignore # Should raise error because angle is read-only

    def test_eq(self):
        """Test equality comparisons."""
        d1 = Degrees(45)
        d2 = Degrees(45)
        d3 = Degrees(90)
        d4 = Degrees(405)  # 405 % 360 == 45
        d5 = Degrees(-315)  # -315 % 360 == 45

        self.assertEqual(d1, d2)  # Same angle
        self.assertNotEqual(d1, d3)  # Different angle
        self.assertEqual(d1, d4)  # Equivalent angle
        self.assertEqual(d1, d5)  # Equivalent angle from negative

    def test_hash(self):
        """Test that hash values are consistent and handle collisions."""
        d1 = Degrees(30)
        d2 = Degrees(30)
        d3 = Degrees(390)  # 390 % 360 == 30
        d4 = Degrees(-330)  # -330 % 360 == 30

        self.assertEqual(hash(d1), hash(d2))
        self.assertEqual(hash(d1), hash(d3))
        self.assertEqual(hash(d1), hash(d4))

    def test_repr(self):
        """Test the __repr__ method."""
        d = Degrees(123.456)
        self.assertEqual(repr(d), "Degrees(angle=123.456)")

    def test_str(self):
        """Test the __str__ method."""
        d = Degrees(123.456)
        self.assertEqual(str(d), "123.456°")

    def test_edge_cases(self):
        """Test edge cases for very large/small values and non-numeric inputs."""
        test_cases = [
            (-360000, 0),
            (360000, 0),
            (0, 0),
            (360, 0),
            (720, 0),
            (-720, 0),
            (999999999, 279),  # 999999999 % 360 == 279
            (-999999999, 81),  # -999999999 % 360 == 81
        ]
        for angle, expected in test_cases:
            with self.subTest(angle=angle):
                d = Degrees(angle)
                self.assertEqual(d.angle, expected)

    def test_invalid_angle(self):
        """Test invalid angle handling."""
        invalid_angles = ['not a number', None, float('nan'), float('inf'), -float('inf')] # type: ignore
        for angle in invalid_angles: # type: ignore
            with self.subTest(angle=angle):
                with self.assertRaises(InvalidAngleError):
                    Degrees(angle) # type: ignore

    def test_comparisons_with_non_degrees(self):
        """Test comparisons with non-Degrees objects."""
        d = Degrees(45)
        self.assertNotEqual(d, "string")  # Different type
        self.assertNotEqual(d, 45)  # Different type
        self.assertNotEqual(d, object())  # Different type

    def test_turn_left(self):
        """Test turning left by 90 degrees."""
        d = Degrees(90)
        new_d = d.turn_left()
        self.assertEqual(new_d.angle, 0)  # 90 - 90 = 0

        d = Degrees(45)
        new_d = d.turn_left()
        self.assertEqual(new_d.angle, 315)  # 45 - 90 = -45 % 360 = 315

        # Testing edge cases
        d = Degrees(0)
        new_d = d.turn_left()
        self.assertEqual(new_d.angle, 270)  # 0 - 90 = -90 % 360 = 270

        d = Degrees(180)
        new_d = d.turn_left(90)
        self.assertEqual(new_d.angle, 90)  # 180 - 90 = 90

    def test_turn_right(self):
        """Test turning right by 90 degrees."""
        d = Degrees(90)
        new_d = d.turn_right()
        self.assertEqual(new_d.angle, 180)  # 90 + 90 = 180

        d = Degrees(270)
        new_d = d.turn_right()
        self.assertEqual(new_d.angle, 0)  # 270 + 90 = 360 % 360 = 0

        # Testing edge cases
        d = Degrees(0)
        new_d = d.turn_right()
        self.assertEqual(new_d.angle, 90)  # 0 + 90 = 90

        d = Degrees(180)
        new_d = d.turn_right(90)
        self.assertEqual(new_d.angle, 270)  # 180 + 90 = 270

    def test_turn_left_custom_degrees(self):
        """Test turning left by a custom number of degrees."""
        d = Degrees(180)
        new_d = d.turn_left(45)
        self.assertEqual(new_d.angle, 135)  # 180 - 45 = 135

        d = Degrees(30)
        new_d = d.turn_left(90)
        self.assertEqual(new_d.angle, 300)  # 30 - 90 = -60 % 360 = 300

    def test_turn_right_custom_degrees(self):
        """Test turning right by a custom number of degrees."""
        d = Degrees(45)
        new_d = d.turn_right(45)
        self.assertEqual(new_d.angle, 90)  # 45 + 45 = 90

        d = Degrees(300)
        new_d = d.turn_right(90)
        self.assertEqual(new_d.angle, 30)  # 300 + 90 = 390 % 360 = 30

    # def test_caching_behavior(self):
    #     """Test caching behavior of the normalization function."""
    #     d1 = Degrees(370)
    #     d2 = Degrees(730)
    #     d3 = Degrees(-450)

    #     # Check if normalization returns the same instance from cache
    #     self.assertIs(d1.angle, d2.angle)  # 370 % 360 == 10 and 730 % 360 == 10
    #     self.assertIs(d1.angle, d3.angle)  # -450 % 360 == 270 and should not be the same instance


if __name__ == "__main__":
    unittest.main()

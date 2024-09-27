import unittest
from src.main.world_objects.robot_objects.degrees import Degrees


class TestDegrees(unittest.TestCase):

    def test_initialization(self):
        """Test the initialization and normalization of angles."""
        d1 = Degrees(360)
        d2 = Degrees(-45)
        d3 = Degrees(720)
        d4 = Degrees(450)

        self.assertEqual(d1.angle, 0)  # 360 % 360 == 0
        self.assertEqual(d2.angle, 315)  # -45 % 360 == 315
        self.assertEqual(d3.angle, 0)  # 720 % 360 == 0
        self.assertEqual(d4.angle, 90)  # 450 % 360 == 90

    # def test_angle_setter(self):
    #     """Test setting the angle property."""
    #     d = Degrees(100)
    #     d.angle = 370 #
    #     self.assertEqual(d.angle, 10)  # 370 % 360 == 10

    def test_eq(self):
        """Test equality comparisons."""
        d1 = Degrees(45)
        d2 = Degrees(45)
        d3 = Degrees(90)
        d4 = Degrees(405)  # 405 % 360 == 45

        self.assertEqual(d1, d2)  # Same angle
        self.assertNotEqual(d1, d3)  # Different angle
        self.assertEqual(d1, d4)  # Equivalent angle

    def test_hash(self):
        """Test that hash values are consistent and handle collisions."""
        d1 = Degrees(30)
        d2 = Degrees(30)
        d3 = Degrees(390)  # 390 % 360 == 30

        self.assertEqual(hash(d1), hash(d2))  # Same angle
        self.assertEqual(hash(d1), hash(d3))  # Equivalent angle

    def test_repr(self):
        """Test the __repr__ method."""
        d = Degrees(123.456)
        self.assertEqual(repr(d), "Degrees(angle=123.456)")

    def test_str(self):
        """Test the __str__ method."""
        d = Degrees(123.456)
        self.assertEqual(str(d), "123.456°")

    def test_edge_cases(self):
        """Test edge cases like very large/small values and non-numeric inputs."""
        d1 = Degrees(-360000)
        d2 = Degrees(360000)
        d3 = Degrees(0)
        d4 = Degrees(360)

        self.assertEqual(d1.angle, 0)  # -360000 % 360 == 0
        self.assertEqual(d2.angle, 0)  # 360000 % 360 == 0
        self.assertEqual(d3.angle, 0)  # 0 % 360 == 0
        self.assertEqual(d4.angle, 0)  # 360 % 360 == 0

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

    def test_turn_right(self):
        """Test turning right by 90 degrees."""
        d = Degrees(90)
        new_d = d.turn_right()
        self.assertEqual(new_d.angle, 180)  # 90 + 90 = 180

        d = Degrees(270)
        new_d = d.turn_right()
        self.assertEqual(new_d.angle, 0)  # 270 + 90 = 360 % 360 = 0

    def test_turn_left_custom_degrees(self):
        """Test turning left by a custom number of degrees."""
        d = Degrees(180)
        new_d = d.turn_left(45)
        self.assertEqual(new_d.angle, 135)  # 180 - 45 = 135

    def test_turn_right_custom_degrees(self):
        """Test turning right by a custom number of degrees."""
        d = Degrees(45)
        new_d = d.turn_right(45)
        self.assertEqual(new_d.angle, 90)  # 45 + 45 = 90


if __name__ == "__main__":
    unittest.main()

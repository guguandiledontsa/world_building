import unittest
from unittest.mock import patch
from src.main.world_objects.robot import Robot

class TestRobotShield(unittest.TestCase):

    def setUp(self):
        self.robot = Robot("CrashTestDummy")

    def test_initial_shield(self):
        self.assertEqual(self.robot.shield_level(), 5)

    def test_damage_shield(self):
        self.robot.damage_shield(1)
        self.assertEqual(self.robot.shield_level(), 4)

    def test_damage_all(self):
        for _ in range(5):
            self.robot.damage_shield(1)
        self.assertEqual(self.robot.shield_level(), 0)

    def test_damage_overkill(self):
        for _ in range(7):
            self.robot.damage_shield(1)
        self.assertEqual(self.robot.shield_level(), 0)

    def test_repair_shield(self):
        self.robot.damage_shield(1)
        self.assertEqual(self.robot.shield_level(), 4)
        # Patch threading.Timer to run the repair immediately
        with patch("threading.Timer") as mock_timer_class:
            def instant_timer(delay, callback):
                callback()  # Instantly call the repair function
                return Mock()  # Return a mock so .start() doesn't break
            mock_timer_class.side_effect = instant_timer
            self.robot.repair_shield()
        self.assertEqual(self.robot.shield_level(), 5)

    def test_repair_when_full(self):
        self.robot.repair_shield()  # Repairing when at max
        self.assertEqual(self.robot.shield_level(), 5)

    def test_damage_non_integer(self):
        with self.assertRaises(TypeError):
            self.robot.damage_shield("a")  # Assuming the method should raise an error

if __name__ == "__main__":
    unittest.main()

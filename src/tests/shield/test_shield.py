import unittest
import time
from src.main.world_objects.robot import Robot


class TestShield(unittest.TestCase):
    def setUp(self):
        self.robot = Robot("CrashTestDummy")

    def test_initial_shield_level(self):
        """Test the initial shield level of the robot."""
        self.assertEqual(5, self.robot.shield_level())

    def test_shield_damage(self):
        """Test the damage to the shield."""
        self.assertEqual(5, self.robot.shield_level())
        self.robot.damage_shield(1)   # Damage by 1
        self.assertEqual(4, self.robot.shield_level())

    def test_shield_damage_all(self):
        """Test damaging the shield to zero."""
        self.assertEqual(5, self.robot.shield_level())
        for _ in range(5):
            self.robot.damage_shield(1)
        self.assertEqual(0, self.robot.shield_level())

    def test_shield_damage_overkill(self):
        """Test over-damaging the shield beyond zero."""
        self.assertEqual(5, self.robot.shield_level())
        for _ in range(6):
            self.robot.damage_shield(1)
        self.assertEqual(0, self.robot.shield_level())

    def test_repair_damaged_shield(self):
        """Test the repair functionality of the shield."""
        self.assertEqual(5, self.robot.shield_level())
        self.robot.damage_shield(1)
        self.assertEqual(4, self.robot.shield_level())
        self.robot.repair_shield()  # Start repair
        self.assertEqual(4, self.robot.shield_level())
        time.sleep(6)  # Wait for the repair to complete
        self.assertEqual(5, self.robot.shield_level())


if __name__ == "__main__":
    unittest.main()

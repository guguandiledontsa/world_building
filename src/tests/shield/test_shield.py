import unittest
import time
from main.world_objects.robot import Robot
from main.world_objects.shield import Shield
from main.world_objects.position import Position

class TestShield(unittest.TestCase):
    def setUp(self):
        self.robot = Robot("CrashTestDummy")

    def test_initial_shield_level(self):
        """Test the initial shield level of the robot."""
        self.assertEqual(5, self.robot.get_shield_level()) # type: ignore

    def test_shield_damage(self):
        """Test the damage to the shield."""
        self.assertEqual(5, self.robot.get_shield_level()) # type: ignore
        self.robot.damage_shield(1)  # type: ignore # Damage by 1
        self.assertEqual(4, self.robot.get_shield_level()) # type: ignore

    def test_shield_damage_all(self):
        """Test damaging the shield to zero."""
        self.assertEqual(5, self.robot.get_shield_level()) # type: ignore
        for _ in range(5):
            self.robot.damage_shield(1)
        self.assertEqual(0, self.robot.get_shield_level()) # type: ignore

    def test_shield_damage_overkill(self):
        """Test over-damaging the shield beyond zero."""
        self.assertEqual(5, self.robot.get_shield_level()) # type: ignore
        for _ in range(6):
            self.robot.damage_shield(1)
        self.assertEqual(0, self.robot.get_shield_level()) # type: ignore

    def test_repair_damaged_shield(self):
        """Test the repair functionality of the shield."""
        self.assertEqual(5, self.robot.get_shield_level()) # type: ignore
        self.robot.damage_shield(1)
        self.assertEqual(4, self.robot.get_shield_level()) # type: ignore
        self.robot.repair_shield()  # Start repair
        self.assertEqual(4, self.robot.get_shield_level()) # type: ignore
        time.sleep(6)  # Wait for the repair to complete
        self.assertEqual(5, self.robot.get_shield_level()) # type: ignore

if __name__ == '__main__':
    unittest.main()

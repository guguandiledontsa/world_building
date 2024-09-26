import unittest
from math import sqrt

from src.main.world_objects.position import Position


class TestCacheBehavior(unittest.TestCase):

    def setUp(self):
        # Clear the caches before each test to ensure isolation
        self.pos1 = Position(1.0, 2.0)
        self.pos2 = Position(4.0, 6.0)
        # Clear the Position's cache
        self.pos1.distance_to.cache_clear()

    def test_position_distance_cache_behavior(self):
        # Test cache behavior for Position's distance_to method
        distance1 = self.pos1.distance_to(self.pos2)
        self.assertEqual(distance1, sqrt((1.0 - 4.0) ** 2 + (2.0 - 6.0) ** 2))
        self.assertEqual(self.pos1.distance_to.cache_info().hits, 0)

        distance2 = self.pos1.distance_to(self.pos2)
        self.assertEqual(distance2, distance1)
        self.assertEqual(self.pos1.distance_to.cache_info().hits, 1)

        # Adding a new Position to fill the cache
        self.pos1.distance_to(Position(7.0, 8.0))
        self.assertEqual(self.pos1.distance_to.cache_info().currsize, 2)

        # Adding another new Position should evict the oldest entry
        self.pos1.distance_to(Position(9.0, 10.0))
        self.assertEqual(self.pos1.distance_to.cache_info().currsize, 3)

    def test_cache_clear(self):

        # Fill the cache for Position's distance_to
        self.pos1.distance_to(self.pos2)
        self.pos1.distance_to(Position(7.0, 8.0))
        self.assertEqual(self.pos1.distance_to.cache_info().currsize, 2)

        # Clear the cache
        self.pos1.distance_to.cache_clear()
        self.assertEqual(self.pos1.distance_to.cache_info().currsize, 0)


if __name__ == "__main__":
    unittest.main()

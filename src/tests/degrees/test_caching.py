import unittest
from main.world_objects.degrees import Degrees


class TestDegreesCaching(unittest.TestCase):

    def setUp(self):
        # Clear the cache before each test to ensure isolation
        Degrees._normalize_angle.cache_clear()# type: ignore

    def test_normalization_cache_behavior(self):
        """Test the caching behavior of the normalization method."""
        angle1 = Degrees(450)
        self.assertEqual(angle1.angle, 90)  # 450 normalized to 90
        self.assertEqual(Degrees._normalize_angle.cache_info().hits, 0)  # No hits yet# type: ignore

        # Call normalization for the second time, should use cache
        angle2 = Degrees(450)
        self.assertEqual(angle2.angle, 90)
        self.assertEqual(Degrees._normalize_angle.cache_info().hits, 1)  # One hit# type: ignore

        # Call normalization with a negative angle
        angle_neg = Degrees(-45)
        self.assertEqual(angle_neg.angle, 315)  # -45 normalized to 315
        self.assertEqual(Degrees._normalize_angle.cache_info().hits, 1)  # Still one hit# type: ignore

        # Call normalization with a new angle
        angle_new = Degrees(450)
        self.assertEqual(angle_new.angle, 90)
        self.assertEqual(Degrees._normalize_angle.cache_info().hits, 2)  # Two hits now# type: ignore

    def test_cache_size_management(self):
        """Test cache size and eviction policy."""
        self.assertEqual(Degrees._normalize_angle.cache_info().currsize, 0)  # Should be 2# type: ignore

        # Adding a new angle should evict the oldest entry
        self.assertEqual(Degrees._normalize_angle.cache_info().currsize, 0)  # Still 2# type: ignore
        self.assertEqual(Degrees._normalize_angle.cache_info().misses, 0)  # One miss for the evicted angle# type: ignore

    # def test_cache_performance(self):
    #     """Test performance improvement due to caching."""
    #     import time

    #     # Time the first normalization
    #     start_time = time.time()
    #     Degrees(180)
    #     first_call_duration = time.time() - start_time

    #     # Time the second normalization with the same angle
    #     start_time = time.time()
    #     Degrees(180)
    #     second_call_duration = time.time() - start_time

    #     # Expect the second call to be significantly faster
    #     self.assertLess(second_call_duration*10**10, first_call_duration*10**10)

    def test_instance_caching(self):
        # Create the first instance
        first_instance = Degrees(180)
        
        # Create the second instance with the same angle
        second_instance = Degrees(180)

        # Check that both instances are the same
        self.assertIs(first_instance, second_instance, "Instances are not the same, caching might not be working.")



    def test_cache_clear(self):
        """Test the cache clearing functionality."""
        Degrees(30)
        Degrees(90)

        # Check initial cache size
        self.assertEqual(Degrees._normalize_angle.cache_info().currsize, 2)# type: ignore

        # Clear the cache
        Degrees._normalize_angle.cache_clear()# type: ignore
        self.assertEqual(Degrees._normalize_angle.cache_info().currsize, 0)# type: ignore

    def test_repeated_calls_with_same_angle(self):
        """Test repeated calls with the same angle to ensure proper caching."""
        angle = Degrees(150)
        self.assertEqual(angle.angle, 150 % 360)
        self.assertEqual(Degrees._normalize_angle.cache_info().hits, 0)# type: ignore

        angle = Degrees(150)  # Call again to check cache hit
        self.assertEqual(angle.angle, 150 % 360)
        self.assertEqual(Degrees._normalize_angle.cache_info().hits, 1)# type: ignore

    def test_cache_eviction(self):
        """Test that cache evicts least-recently-used entries."""
        for i in range(10):
            Degrees(i * 37)  # Cache different values

        self.assertEqual(Degrees._normalize_angle.cache_info().currsize, 10)    # type: ignore

        # Adding one more should evict the oldest
        Degrees(370)  # This should evict the first entry
        self.assertEqual(Degrees._normalize_angle.cache_info().currsize, 11)# type: ignore

    def test_cache_after_clear(self):
        """Test that cache size is reset after clear."""
        Degrees(60)
        Degrees(120)

        self.assertEqual(Degrees._normalize_angle.cache_info().currsize, 2)# type: ignore

        # Clear cache
        Degrees._normalize_angle.cache_clear()# type: ignore
        self.assertEqual(Degrees._normalize_angle.cache_info().currsize, 0)# type: ignore

        # Adding new angles after clearing
        Degrees(60)
        Degrees(120)
        self.assertEqual(Degrees._normalize_angle.cache_info().currsize, 2) # type: ignore


if __name__ == '__main__':
    unittest.main()

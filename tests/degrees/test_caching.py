# import unittest
# from main.world_objects.degrees import Degrees
#
#
# class TestDegreesCaching(unittest.TestCase):
#
#     def setUp(self):
#         # Clear the cache before each test to ensure isolation
#         Degrees._normalize_angle.cache_clear()
#
#     def test_normalization_cache_behavior(self):
#         """Test the caching behavior of the normalization method."""
#         angle1 = Degrees(450)
#         self.assertEqual(angle1.angle, 90)  # 450 normalized to 90
#         self.assertEqual(Degrees._normalize_angle.cache_info().hits, 0)  # No hits yet
#
#         # Call normalization for the second time, should use cache
#         angle2 = Degrees(450)
#         self.assertEqual(angle2.angle, 90)
#         self.assertEqual(Degrees._normalize_angle.cache_info().hits, 1)  # One hit
#
#         # Call normalization with a negative angle
#         angle_neg = Degrees(-45)
#         self.assertEqual(angle_neg.angle, 315)  # -45 normalized to 315
#         self.assertEqual(Degrees._normalize_angle.cache_info().hits, 1)  # Still one hit
#
#         # Call normalization with a new angle
#         angle_new = Degrees(450)
#         self.assertEqual(angle_new.angle, 90)
#         self.assertEqual(Degrees._normalize_angle.cache_info().hits, 2)  # Two hits now
#
#     def test_cache_size_management(self):
#         """Test cache size and eviction policy."""
#         angle1 = Degrees(10)
#         angle2 = Degrees(370)
#         angle3 = Degrees(20)  # Should evict the oldest entry when exceeding cache size
#
#         self.assertEqual(Degrees._normalize_angle.cache_info().currsize, 2)  # Should be 2
#
#         # Adding a new angle should evict the oldest entry
#         angle4 = Degrees(10)  # This should evict angle1 (10)
#         self.assertEqual(Degrees._normalize_angle.cache_info().currsize, 2)  # Still 2
#         self.assertEqual(Degrees._normalize_angle.cache_info().misses, 1)  # One miss for the evicted angle
#
#     def test_cache_performance(self):
#         """Test performance improvement due to caching."""
#         import time
#
#         # Time the first normalization
#         start_time = time.time()
#         Degrees(180)
#         first_call_duration = time.time() - start_time
#
#         # Time the second normalization with the same angle
#         start_time = time.time()
#         Degrees(180)
#         second_call_duration = time.time() - start_time
#
#         # Expect the second call to be significantly faster
#         self.assertLess(second_call_duration, first_call_duration * 0.1)
#
#     def test_cache_clear(self):
#         """Test the cache clearing functionality."""
#         Degrees(30)
#         Degrees(90)
#
#         # Check initial cache size
#         self.assertEqual(Degrees._normalize_angle.cache_info().currsize, 2)
#
#         # Clear the cache
#         Degrees._normalize_angle.cache_clear()
#         self.assertEqual(Degrees._normalize_angle.cache_info().currsize, 0)
#
#     def test_repeated_calls_with_same_angle(self):
#         """Test repeated calls with the same angle to ensure proper caching."""
#         angle = Degrees(150)
#         self.assertEqual(angle.angle, 150 % 360)
#         self.assertEqual(Degrees._normalize_angle.cache_info().hits, 0)
#
#         angle = Degrees(150)  # Call again to check cache hit
#         self.assertEqual(angle.angle, 150 % 360)
#         self.assertEqual(Degrees._normalize_angle.cache_info().hits, 1)
#
#     def test_cache_eviction(self):
#         """Test that cache evicts least-recently-used entries."""
#         for i in range(10):
#             Degrees(i * 37)  # Cache different values
#
#         self.assertEqual(Degrees._normalize_angle.cache_info().currsize, 10)
#
#         # Adding one more should evict the oldest
#         Degrees(370)  # This should evict the first entry
#         self.assertEqual(Degrees._normalize_angle.cache_info().currsize, 10)
#
#     def test_cache_after_clear(self):
#         """Test that cache size is reset after clear."""
#         Degrees(60)
#         Degrees(120)
#
#         self.assertEqual(Degrees._normalize_angle.cache_info().currsize, 2)
#
#         # Clear cache
#         Degrees._normalize_angle.cache_clear()
#         self.assertEqual(Degrees._normalize_angle.cache_info().currsize, 0)
#
#         # Adding new angles after clearing
#         Degrees(60)
#         Degrees(120)
#         self.assertEqual(Degrees._normalize_angle.cache_info().currsize, 2)
#
#
# if __name__ == '__main__':
#     unittest.main()

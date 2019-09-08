"""Test module for generating random numbers and perform statistical calculations"""
from unittest import TestCase
from code_package.random_variables import get_discrete_distribution, estimate_var, \
    get_standard_normal_distribution, calculate_nth_moment, create_distribution, \
    estimate_cumulative_distribution


class TestRandomVariables(TestCase):
    """Test class"""

    def test_calculate_nth_moment_exception(self):
        """nth moment calculation raises error when sample contains no elements"""
        self.assertRaises(ValueError, calculate_nth_moment, [], 5)

    def test_calculate_nth_moment(self):
        """Run test cases for nth moment calculation"""
        self.calculate_with_given_moment([1, -2, 0], 2, 1.6666666666666667)
        self.calculate_with_given_moment([1, -2, 0], 3, -2.3333333333333335)
        self.calculate_with_given_moment([1, -2, 0], 4, 5.666666666666667)

    def calculate_with_given_moment(self, sample, moment, expected_result):
        """nth moment calculation test helper method with given expected value"""
        # arrange
        # act
        result = calculate_nth_moment(sample, moment)

        # assert
        self.assertEqual(result, expected_result)

    def test_estimate_var_raises_value_error(self):
        """var calculation test helper method with given expected value"""
        self.assertRaises(ValueError, estimate_var, [], 0.05)

    def test_estimate_var(self):
        """Test cases for estimating var"""
        self.estimate_var_with_given_result([2, 2, 5, -1, 5], 0.05, -1)
        self.estimate_var_with_given_result([2, 2, 5, -1, 5], 0.2, 2)
        self.estimate_var_with_given_result([2, 2, 5, -1, 5], 1.0, 5)
        self.estimate_var_with_given_result([2, 2, 5, -1, 5], -1.0, -1)
        self.estimate_var_with_given_result([2, 2, 5, -1, 5], 2.0, 5)

    def estimate_var_with_given_result(self, sample, threshold, result):
        """var calculation test helper method with given expected value"""
        # arrange
        # act
        var = estimate_var(sample, threshold)

        # assert
        self.assertEqual(var, result)

    def test_estimate_cumulative_distribution(self):
        """Test cases for estimating var"""
        self.estimate_cumulative_distribution_helper([2, 2, 5, -1, 5], 3, 0.6)
        self.estimate_cumulative_distribution_helper([2, 2, 5, -1, 5], 2, 0.6)
        self.estimate_cumulative_distribution_helper([2, 2, 5, -1, 5], -2, 0.0)
        self.estimate_cumulative_distribution_helper([2, 2, 5, -1, 5], 50, 1.0)
        self.estimate_cumulative_distribution_helper([1], 2, 1.0)
        self.estimate_cumulative_distribution_helper([1], 0, 0.0)

    def estimate_cumulative_distribution_helper(self, sample, threshold, result):
        """var calculation test helper method with given expected value"""
        # arrange
        # act
        var = estimate_cumulative_distribution(sample, threshold)

        # assert
        self.assertEqual(var, result)

    def test_create_distribution_valid_value(self):
        """Create vector of sample distributions. Without mocking the get_hybrid_distribution
        we cannot test the whole method."""
        # arrange
        sample_size = 8

        # act
        result = create_distribution(sample_size)

        # assert
        self.assertEqual(len(result), sample_size)

    def test_create_distribution_invalid_value(self):
        """Create vector of sample distributions with negative number it raises exception"""
        self.assertRaises(ValueError, create_distribution, -5)

    def test_get_hybrid_distribution(self):
        """Test combining the discrete and standard normal distributions"""
        # get_hybrid_distribution adds two values, without mocking the get_discrete_distribution
        # and get_standard_normal_distribution methods, it cannot be unit tested

    def test_discrete_random_distribution_empirical_distribution(self):
        """Empirical test for given discrete distribution
        (i) returns the expected values: 0, 3, 5
        (ii) has the required distribution of those values: 0.5, 0.25. 0.25"""
        # arrange
        count0 = 0
        count3 = 0
        count5 = 0
        type_fail = False

        # act
        sample = 20000
        for _ in range(sample):
            result = get_discrete_distribution()
            if result == 0:
                count0 = count0 + 1
            elif result == 3:
                count3 = count3 + 1
            elif result == 5:
                count5 = count5 + 1
            else:
                type_fail = True

        # assert
        self.assertFalse(type_fail)
        # Test is stable but random. This is not preferable, can be tested with injected seed
        self.assertTrue(almost_equal(0.5, count0 / sample, 0.01))
        self.assertTrue(almost_equal(0.25, count3 / sample, 0.01))
        self.assertTrue(almost_equal(0.25, count5 / sample, 0.01))

    def test_standard_normal_distribution_empirical_distribution(self):
        """Empirical test for standard normal distribution
        Use the known percentiles of the standard normal distribution
        as a specification of the unknown distribution we are using."""
        # arrange
        percentile_0_8 = 0.8416212335729142051787
        percentile_0_5 = 0.0
        percentile_0_2 = -0.8416212335729142051787
        percentile_0_05 = -1.644853626951472714864

        percentile_0_8_count = 0
        percentile_0_5_count = 0
        percentile_0_2_count = 0
        percentile_0_05_count = 0

        # act
        sample = 20000
        for _ in range(sample):
            result = get_standard_normal_distribution()
            if result < percentile_0_8:
                percentile_0_8_count = percentile_0_8_count + 1
            if result < percentile_0_5:
                percentile_0_5_count = percentile_0_5_count + 1
            if result < percentile_0_2:
                percentile_0_2_count = percentile_0_2_count + 1
            if result < percentile_0_05:
                percentile_0_05_count = percentile_0_05_count + 1

        # assert
        self.assertTrue(almost_equal(0.8, percentile_0_8_count / sample, 0.01))
        self.assertTrue(almost_equal(0.5, percentile_0_5_count / sample, 0.01))
        self.assertTrue(almost_equal(0.2, percentile_0_2_count / sample, 0.01))
        self.assertTrue(almost_equal(0.05, percentile_0_05_count / sample, 0.01))


def almost_equal(expected, resulted, tolerance):
    """Helper method to check equality with given tolerance"""
    if abs(expected - resulted) < tolerance:
        return True
    return False

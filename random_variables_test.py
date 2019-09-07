from unittest import TestCase
from random_variables import get_discrete_distribution, get_standard_normal_distribution


class TestRandomVariables(TestCase):

    def test_discrete_random_distribution_empirical_distribution(self):
        # arrange
        count0 = 0
        count3 = 0
        count5 = 0
        type_fail = False

        # act
        sample = 1000000
        for x in range(sample):
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
        # Test outcome is stable but random. This is not preferable, can be replaced with a test with injected seed
        self.assertTrue(almost_equal(0.5, count0 / sample, 0.001))
        self.assertTrue(almost_equal(0.25, count3 / sample, 0.001))
        self.assertTrue(almost_equal(0.25, count5 / sample, 0.001))

    def test_standard_normal_distribution_empirical_distribution(self):
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
        sample = 2000000
        for x in range(sample):
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
        self.assertTrue(almost_equal(0.8, percentile_0_8_count / sample, 0.001))
        self.assertTrue(almost_equal(0.5, percentile_0_5_count / sample, 0.001))
        self.assertTrue(almost_equal(0.2, percentile_0_2_count / sample, 0.001))
        self.assertTrue(almost_equal(0.05, percentile_0_05_count / sample, 0.001))


def almost_equal(expected, resulted, tolerance):
    if abs(expected - resulted) < tolerance:
        return True
    return False










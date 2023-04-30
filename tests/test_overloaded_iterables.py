from math import prod
import unittest
from secrets import choice
from statistics import mean, median

import numpy as np

from src.overloaded_iterables.classes import OverloadedList, OverloadedSet


class TestOverloadedList(unittest.TestCase):
    """
    Test-cases for the `OverloadedList` class.
    """

    VALID_NUMBERS = OverloadedList([num for num in range(0, 1_000_000)])

    def setUp(self):
        self.ARR_1 = OverloadedList(
            [choice(self.VALID_NUMBERS) for _ in range(1, 101)])
        self.ARR_2 = self.ARR_1
        self.ARR_2.append(choice(self.VALID_NUMBERS))

        self.VALUES, self.FREQUENCIES = self.ARR_1.frequencies

    def test_sum(self):
        self.assertEqual(sum(self.ARR_1), self.ARR_1.sum())
    
    def test_sum_null_list(self):
        arr = OverloadedList()
        self.assertEqual(float(), arr.sum())

    def test_prod(self):
        # prithoo: We need smaller values to test prod() so that we may avoid memory overflow errors.
        prod_contents = [item for item in np.arange(0, 25, 0.01)]
        prod_arr = OverloadedList([choice(prod_contents)
                                  for _ in range(1, 16)])

        self.assertEqual(prod(prod_arr), prod_arr.prod())

    def test_prod_null_list(self):
        arr = OverloadedList()
        self.assertEqual(float(), arr.prod())

    def test_prod_zero_in_list(self):
        arr = self.ARR_1
        arr.append(0)

        self.assertEqual(float(), arr.prod())

    def test_sorting(self):
        self.assertSequenceEqual(OverloadedList(
            sorted(self.ARR_1)), self.ARR_1.sort())

    def test_raise_to_power(self):
        power = choice([i for i in np.arange(0.5, 5.0, 0.5)])
        raised = OverloadedList([item**power for item in self.ARR_1])

        self.assertListEqual(raised, self.ARR_1.raise_to(power=power))

    def test_median_zero(self):
        _list = OverloadedList()
        self.assertEqual(float(), _list.median())

    def test_median_one(self):
        _list = OverloadedList([choice(self.VALID_NUMBERS)])
        self.assertEqual(_list[0], _list.median())

    def test_median_even(self):
        self.assertEqual(median(self.ARR_1), self.ARR_1.median())

    def test_median_odd(self):
        self.assertEqual(median(self.ARR_2), self.ARR_2.median())

    def test_mean(self):
        self.assertEqual(mean(self.ARR_1), self.ARR_1.mean())

    def test_len(self):
        self.assertEqual(len(self.ARR_1), self.ARR_1.len)

    def test_frequencies_structure(self):
        self.assertEqual(self.VALUES.len, self.FREQUENCIES.len)

    def test_frequencies_values(self):
        for index, value in enumerate(self.VALUES):
            self.assertEqual(self.FREQUENCIES[index], self.ARR_1.count(value))

    def test_rms_value(self):
        squared = OverloadedList([i**2 for i in self.ARR_1])
        _mean_squared = squared.mean()
        root_mean_squared = _mean_squared**(1/2)

        self.assertEqual(self.ARR_1.rms(), root_mean_squared)


class TestOverloadedSet(unittest.TestCase):
    """
    Test-cases for the `OverloadedSet` class.
    """
    VALID_NUMBERS = OverloadedList([num for num in range(0, 1_000_000)])

    def setUp(self):
        self.ARR_1 = OverloadedSet()

        _num = choice(self.VALID_NUMBERS)
        while self.ARR_1.len < 100:
            if _num not in self.ARR_1:
                self.ARR_1.add(_num)
            _num = choice(self.VALID_NUMBERS)

        self.ARR_2 = self.ARR_1
        _num = choice(self.VALID_NUMBERS)
        while _num in self.ARR_2:
            _num = choice(self.VALID_NUMBERS)

        self.ARR_2.add(_num)

    def test_sum(self):
        self.assertEqual(sum(self.ARR_1), self.ARR_1.sum())

    def test_sum_null_list(self):
        arr = OverloadedList()
        self.assertEqual(float(), arr.sum())

    def test_prod(self):
        # prithoo: We need smaller values to test prod() so that we may avoid memory overflow errors.
        prod_contents = [item for item in np.arange(0, 25, 0.01)]
        prod_arr = OverloadedSet()

        _num = choice(prod_contents)
        while prod_arr.len < 16:
            # Of course, we cannot have duplicate elements in a set.
            if not _num in prod_arr:
                prod_arr.add(_num)
            _num = choice(prod_contents)

        self.assertEqual(prod(prod_arr), prod_arr.prod())

    def test_prod_null_list(self):
        arr = OverloadedList()
        self.assertEqual(float(), arr.prod())

    def test_prod_zero_in_list(self):
        # prithoo: We need smaller values to test prod() so that we may avoid memory overflow errors.
        prod_contents = [item for item in np.arange(0, 25, 0.01)]
        prod_arr = OverloadedSet()

        _num = choice(prod_contents)
        while prod_arr.len < 16:
            # Of course, we cannot have duplicate elements in a set.
            if not _num in prod_arr:
                prod_arr.add(_num)
            _num = choice(prod_contents)
        if 0.0 not in prod_arr:
            prod_arr.add(0.0)
        self.assertEqual(float(), prod_arr.prod())

    def test_sorting(self):
        self.assertSequenceEqual(sorted(self.ARR_1), self.ARR_1.sort())

    def test_raise_to_power(self):
        power = choice([i for i in np.arange(0.5, 5.0, 0.5)])
        raised = OverloadedSet([item**power for item in self.ARR_1])
        self.assertSetEqual(raised, self.ARR_1.raise_to(power=power))

    def test_median_zero(self):
        _set = OverloadedSet()
        self.assertEqual(float(), _set.median())

    def test_median_one(self):
        _set = OverloadedSet({choice(self.VALID_NUMBERS)})
        self.assertEqual(OverloadedList(_set)[0], _set.median())

    def test_median_even(self):
        self.assertEqual(median(self.ARR_1), self.ARR_1.median())

    def test_median_odd(self):
        self.assertEqual(median(self.ARR_2), self.ARR_2.median())

    def test_mean(self):
        self.assertEqual(mean(self.ARR_1), self.ARR_1.mean())

    def test_len(self):
        self.assertEqual(len(self.ARR_1), self.ARR_1.len)

    def test_rms_value(self):
        squared = OverloadedSet([i**2 for i in self.ARR_1])
        _mean_squared = squared.mean()
        root_mean_squared = _mean_squared**(1/2)

        self.assertEqual(self.ARR_1.rms(), root_mean_squared)


if __name__ == '__main__':
   pass

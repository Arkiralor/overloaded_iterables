from math import prod
from os import path, makedirs, remove
from pathlib import Path
from pytest import mark
import unittest
from secrets import choice
from statistics import mean, median

import numpy as np

from src.overloaded_iterables.classes import OverloadedList, OverloadedSet


class TestOverloadedList(unittest.TestCase):
    """
    Test-cases for the `OverloadedList` class.
    """

    def setUp(self):
        """
        Create two random `OverloadedList` objects with random values and frequencies.

        Also, create a directory to store the graphs generated by the `OverloadedList` class.
        """
        self.VALID_NUMBERS = OverloadedList([num for num in range(0, 25)])

        self.ARR_1 = OverloadedList(
            [choice(self.VALID_NUMBERS) for _ in range(1, 501)])
        self.ARR_2 = self.ARR_1
        self.ARR_2.append(choice(self.VALID_NUMBERS))

        self.VALUES, self.FREQUENCIES = self.ARR_1.frequencies

        self.BASE_DIR = Path(__file__).resolve().parent.parent
        self.GRAPH_DIR = path.join(self.BASE_DIR, "media", "graphs")
        if not path.exists(self.GRAPH_DIR):
            makedirs(self.GRAPH_DIR)

        self.hist_name: str = None
        self.plot_name: str = None
        self.scatter_name: str = None

    def test_sum(self):
        """
        Test the .sum() method against the built-in sum() function.
        """
        self.assertEqual(sum(self.ARR_1), self.ARR_1.sum())

    def test_sum_null_list(self):
        """
        Test the .sum() method for an empty OverloadedList.
        """
        arr = OverloadedList()
        self.assertEqual(float(), arr.sum())

    def test_prod(self):
        """
        Test the .prod() method against the built-in math.prod() function.
        """
        # prithoo: We need smaller values to test prod() so that we may avoid memory overflow errors.
        prod_contents = [item for item in np.arange(0, 25, 0.01)]
        prod_arr = OverloadedList([choice(prod_contents)
                                  for _ in range(1, 16)])

        self.assertEqual(prod(prod_arr), prod_arr.prod())

    def test_prod_null_list(self):
        """
        Test the .prod() method for an empty OverloadedList.
        """
        arr = OverloadedList()
        self.assertEqual(float(), arr.prod())

    def test_prod_zero_in_list(self):
        """
        Test the .prod() method for an OverloadedList with a zero in it.
        """
        arr = self.ARR_1
        arr.append(0)

        self.assertEqual(float(), arr.prod())

    def test_sorting(self):
        """
        Test the .sort() method against the built-in sorted() function.
        """
        self.assertSequenceEqual(OverloadedList(
            sorted(self.ARR_1)), self.ARR_1.sort())

    def test_raise_to_power(self):
        """
        Test the .raise_to() method against the built-in ** operator.
        """
        power = choice([i for i in np.arange(0.5, 5.0, 0.5)])
        raised = OverloadedList([item**power for item in self.ARR_1])

        self.assertListEqual(raised, self.ARR_1.raise_to(power=power))

    def test_median_zero(self):
        """
        Test the .median() method for an empty OverloadedList.
        """
        _list = OverloadedList()
        self.assertEqual(float(), _list.median())

    def test_median_one(self):
        """
        Test the .median() method for an OverloadedList with exactly one element.
        """
        _list = OverloadedList([choice(self.VALID_NUMBERS)])
        self.assertEqual(_list[0], _list.median())

    def test_median_even(self):
        """
        Test the .median() method for an OverloadedList with an even number of elements.
        
        i.e len(_list) % 2 == 0 and len(_list) > 1
        """
        self.assertEqual(median(self.ARR_1), self.ARR_1.median())

    def test_median_odd(self):
        """
        Test the .median() method for an OverloadedList with an odd number of elements.

        i.e len(_list) % 2 == 1 and len(_list) > 1
        """
        self.assertEqual(median(self.ARR_2), self.ARR_2.median())

    def test_mean(self):
        """
        Test the .mean() method against the built-in statistics.mean() function.
        """
        self.assertEqual(mean(self.ARR_1), self.ARR_1.mean())

    def test_len(self):
        """
        Test the .len property against the built-in len() function.
        """
        self.assertEqual(len(self.ARR_1), self.ARR_1.len)

    def test_frequencies_structure(self):
        """
        Test the .frequencies property for the correct structure i.e, 
        the size of both the `values` and `frequencies` OverloadedLists should be the same.
        """
        self.assertEqual(self.VALUES.len, self.FREQUENCIES.len)

    def test_frequencies_values(self):
        """
        Test the .frequencies property for the correct values i.e,
        the `values` OverloadedList should contain all the unique values in the original OverloadedList and
        the `frequencies` OverloadedList should contain the frequency of each unique value in the original OverloadedList.
        """
        for index, value in enumerate(self.VALUES):
            self.assertEqual(self.FREQUENCIES[index], self.ARR_1.count(value))

    def test_rms_value(self):
        """
        Test the .rms() method against a custom implementation of the root mean square formula.

        The formula of root mean square is:
        rms = sqrt((x1^2 + x2^2 + x3^2 + ... + xn^2) / n)
        """
        squared = OverloadedList([i**2 for i in self.ARR_1])
        _mean_squared = squared.mean()
        root_mean_squared = _mean_squared**(1/2)

        self.assertEqual(self.ARR_1.rms(), root_mean_squared)

    def test_hist(self):
        """
        Test the .hist() method for the correct return value.
        """
        self.assertTrue(self.ARR_1.hist())

    def test_plot(self):
        """
        Test the .plot() method for the correct return value.
        """
        self.assertTrue(self.ARR_1.plot())

    def test_scatter(self):
        """
        Test the .scatter() method for the correct return value.
        """
        self.assertTrue(self.ARR_1.scatter())

    def test_hist_file(self):
        """
        Test that the .hist() method saves the plot to the correct directory when the `save_dir` argument is passed.
        """
        self.hist_name = self.ARR_1.hist(
            bins=self.ARR_1.len//10, 
            save_dir=self.GRAPH_DIR, name='hist', histtype='step', title='random_hist')
        self.assertTrue(path.exists(path.join(self.GRAPH_DIR, self.hist_name)))

    def test_plot_file(self):
        """
        Test that the .plot() method saves the plot to the correct directory when the `save_dir` argument is passed.
        """
        self.plot_name = self.ARR_1.plot(
            save_dir=self.GRAPH_DIR, name='plot', title='random_plot')
        self.assertTrue(path.exists(path.join(self.GRAPH_DIR, self.plot_name)))

    def test_scatter_file(self):
        """
        Test that the .scatter() method saves the plot to the correct directory when the `save_dir` argument is passed.
        """
        self.scatter_name = self.ARR_1.scatter(
            save_dir=self.GRAPH_DIR, name='scatter', title='random_scatter')
        self.assertTrue(path.exists(
            path.join(self.GRAPH_DIR, self.scatter_name)))

    def tearDown(self):
        """
        Delete any and all files created during the tests.
        """
        if self.hist_name and path.exists(path.join(self.GRAPH_DIR, self.hist_name)):
            remove(path.join(self.GRAPH_DIR, self.hist_name))

        if self.plot_name and path.exists(path.join(self.GRAPH_DIR, self.plot_name)):
            remove(path.join(self.GRAPH_DIR, self.plot_name))

        if self.scatter_name and path.exists(path.join(self.GRAPH_DIR, self.scatter_name)):
            remove(path.join(self.GRAPH_DIR, self.scatter_name))


class TestOverloadedSet(unittest.TestCase):
    """
    Test-cases for the `OverloadedSet` class.
    """
    VALID_NUMBERS = OverloadedList([num for num in range(0, 1_000_000)])

    def setUp(self):
        """
        Create two `OverloadedSet` objects with 100 random elements each.
        """
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
        """
        Test the .sum() method against the built-in sum() function.
        """
        self.assertEqual(sum(self.ARR_1), self.ARR_1.sum())

    def test_sum_null_list(self):
        """
        Test the .sum() method for an empty OverloadedSet.
        """
        arr = OverloadedList()
        self.assertEqual(float(), arr.sum())

    def test_prod(self):
        """
        Test the .prod() method against the built-in math.prod() function.
        """
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
        """
        Test the .prod() method for an empty OverloadedSet.
        """
        arr = OverloadedList()
        self.assertEqual(float(), arr.prod())

    def test_prod_zero_in_list(self):
        """
        Tsst the .prod() method for a list with a zero element.
        """
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
        """
        Test the .sort() method against the built-in sorted() function.
        """
        self.assertSequenceEqual(sorted(self.ARR_1), self.ARR_1.sort())

    def test_raise_to_power(self):
        """
        Test the .raise_to() method against the built-in `**` operator.
        """
        power = choice([i for i in np.arange(0.5, 5.0, 0.5)])
        raised = OverloadedSet([item**power for item in self.ARR_1])
        self.assertSetEqual(raised, self.ARR_1.raise_to(power=power))

    def test_median_zero(self):
        """
        Test the .median() method for an empty OverloadedSet.
        """
        _set = OverloadedSet()
        self.assertEqual(float(), _set.median())

    def test_median_one(self):
        """
        Test the .median() method for an OverloadedSet with exactly one element.
        """
        _set = OverloadedSet({choice(self.VALID_NUMBERS)})
        self.assertEqual(OverloadedList(_set)[0], _set.median())

    def test_median_even(self):
        """
        Test the .median() method for an OverloadedSet with an even number of elements.

        i.e. len(OverloadedSet) % 2 == 0 and len(OverloadedSet) > 1
        """
        self.assertEqual(median(self.ARR_1), self.ARR_1.median())

    def test_median_odd(self):
        """
        Test the .median() method for an OverloadedSet with an odd number of elements.

        i.e. len(OverloadedSet) % 2 == 1 and len(OverloadedSet) > 1
        """
        self.assertEqual(median(self.ARR_2), self.ARR_2.median())

    def test_mean(self):
        """
        Test the .mean() method against the built-in statistics.mean() function.
        """
        self.assertEqual(mean(self.ARR_1), self.ARR_1.mean())

    def test_len(self):
        """
        Test the .len property against the built-in len() function.
        """
        self.assertEqual(len(self.ARR_1), self.ARR_1.len)

    def test_rms_value(self):
        """
        Test the .rms() method against a custom implementation of the root-mean-square formula.

        The formula of root mean square is:
        rms = sqrt((x1^2 + x2^2 + x3^2 + ... + xn^2) / n)
        """
        squared = OverloadedSet([i**2 for i in self.ARR_1])
        _mean_squared = squared.mean()
        root_mean_squared = _mean_squared**(1/2)

        self.assertEqual(self.ARR_1.rms(), root_mean_squared)


if __name__ == '__main__':
   pass

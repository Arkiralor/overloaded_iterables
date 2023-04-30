# Overloaded Iterables

Overloaded versions of the built-in python classes: `<list>` and `<set>`, to include some extra functionalities as an experiment.

An experimental Python package to extend the methods found in Python's built-in list and set classes to add some extra functionality that I, personally find useful in my day-to-day implementations and was too lazy to keep writing/copy-pasting again and again.

## Specifications

1. __Python Version:__

    _Python v3.8+_

2. __Code Coverage:__

    ![_code coverage_](https://github.com/Arkiralor/overloaded_iterables/blob/master/media/screenshots/coverage.PNG?raw=true)

## Python Package Index

1. [Project Homepage](https://pypi.org/project/overloaded-iterables/)
2. [Contents](https://pypi.org/project/overloaded-iterables/#files)

## Installation

```sh
python -m pip install overloaded-iterables
```

## Classes

The current iteration contains the following classes

### 1. OverloadedList

- A non-datatype constrained, single-dimensional collection of values.
- Inherits solely from Python's built-in `<list>` class.

```python
from overloaded_iterables.classes import OverloadedList

obj = OverloadedList(*args)
```

### 2. OverloadedSet

- A non-datatype constrained, single-dimensional collection of __unique__ values.
- Inherits solely from Python's built-in `<set>` class.

```python
    from overloaded_iterables.classes import OverloadedSet

    obj = OverloadedSet(*args)
```

## Functions and Methods

1. `<class>.mean()`
    - Find the [mean](https://en.wikipedia.org/wiki/Arithmetic_mean) of the values in the given iterable class object.
    - Arguments: `self`
    - Returns: `float (64-bit)`
    - Example:

        ```python
            _mean: float = obj.mean()
        ```

2. `<class>.sum()`
    - Claculate the sum of all the elements in the given iterable class object.
    - Arguments: `self`
    - Returns: `float (64-bit)`
    - Example:

        ```python
            _sum: float = obj.sum()
        ```

3. `<class>.prod()`
    - Calculate the product of all the elements in the given iterable class object.
    - Arguments: `self`
    - Returns: `float (64-bit)`
    - Example:

        ```python
            _product: float = obj.prod()
        ```

4. `<class>.sort()`
    - Sorts the contents of the given iterable class object via the [Timsort](https://en.wikipedia.org/wiki/Timsort) sorting algorithm.
    - Arguments: `self`, `key: None | default: None`, `reverse: bool | default: False`
    - Returns `object: <list>`
    - Example:

        ```python
            sorted_seq: list = obj.sort()
        ```

5. `<class>.raise_to()`
    - Raises each element in the iterable class object to the given power.
    - Arguments: `self`, `power: float (64-bit) | default: 1.0`
    - Returns `object: <class>`
    - Example:

        ```python
            import numpy as np
            from secrets import choice

            ## Taking the power variable, 'z' to be a random integer between -10 and +10
            z:float = choice([i for i in np.arange(-10, 10, 0.5)])
            _raised_sequence: type(obj) = obj.raise_to(power=z)
        ```

6. `<class>.rms()`
    - Finds the [Root-Mean-Square (RMS)](https://en.wikipedia.org/wiki/Root_mean_square) of the values in the current iterable class object.
    - Arguments: `self`, `power: float | default: 2`, `root: int | default: 2`
    - Returns: `float (64-bit)`
    - Example:

        ```python
            _rms: float = obj.rms()
        ```

7. `<class>.median()`
    - Finds the [median](https://en.wikipedia.org/wiki/Median) of the contents of the given iterable class object.
    - Arguments: `self`
    - Returns: `float (64-bit)`
    - Example:

        ```python
            _median:float = obj.median()
        ```

8. `<class>.hist()`&nbsp;&nbsp;&nbsp;&nbsp;__(OverloadedList only)__
    - Plots the [histogram](https://en.wikipedia.org/wiki/Histogram) of the frequency distribution of the elements in the OverloadedList.
    - Arguments: `self`, `bins: int | default: 10`, `title: str | default: 'Histogram'`, `x_label: str | default: 'Values --->'`, `y_label: str | default: 'Frequencies --->'`, `save_dir: str | default: None`, `file_name: str | default: None`, `histtype: str | default: 'step'`, `align: str | default: 'mid'`, `orientation: str | default: 'vertical'`, `log_scale: bool | default: False`, `show: bool | default: False`
    - Process:
        - Shows the generated figure if `show` is set to `True`
        - Saves the generated figure if `save_dir` is provided.
    - Returns: `bool`
    - Example:

        ```python
            fig_check:bool = obj.hist(show=True, save_dir='figures', file_name='some-figure')
        ```

9. `<class>.plot()`&nbsp;&nbsp;&nbsp;&nbsp;__(OverloadedList only)__
    - Plots the [lineplot](https://en.wikipedia.org/wiki/Line_chart) of the frequency distribution of the elements in the OverloadedList.
    - Arguments: `self`, `title: str | default: 'Line Plot'`, `x_label: str | default: 'Values --->'`, `y_label: str | default: 'Frequencies --->'`, `save_dir: str | default: None`, `file_name: str | default: None`, `color: str | default: '#000000'`, `linewidth: float | default: 1`, `marker: str | default: ','`,  `markerfacecolor: str | default: '#252525'`, `marker_size: float | default: 1.0`, `show: bool | default: False`
    - Process:
        - Shows the generated figure if `show` is set to `True`
        - Saves the generated figure if `save_dir` is provided.
    - Returns: `bool`
    - Example:

        ```python
            fig_check:bool = obj.plot(show=True, save_dir='figures', file_name='some-figure')
        ```

10. `<class>.scatter()`&nbsp;&nbsp;&nbsp;&nbsp;__(OverloadedList only)__
    - Plots the [scatterplot](https://en.wikipedia.org/wiki/Scatter_plot) of the frequency distribution of the elements in the OverloadedList.
    - Arguments: `self`, `title: str | default: 'Scatter Plot'`, `x_label: str | default: 'Values --->'`, `y_label: str | default: 'Frequencies --->'`, `save_dir: str | default: None`, `file_name: str | default: None`, `size: List[float] | default: [1.25]`, `color: str | default: '#000000'`, `marker: str | default: ','`, `line_width: float | default: 2`, `show: bool | default: False`
    - Process:
        - Shows the generated figure if `show` is set to `True`
        - Saves the generated figure if `save_dir` is provided.
    - Returns: `bool`
    - Example:

        ```python
            fig_check:bool = obj.scatter(show=True, save_dir='figures', file_name='some-figure')
        ```

11. `<class>.len (property)`
    - Finds and returns the length of the current iterable class object as a property.
    - Arguments: `self`
    - Returns: `int`
    - Example:

        ```python
            _l: int = obj.len
        ```

12. `<class>.frequencies (property)`&nbsp;&nbsp;&nbsp;&nbsp;__(OverloadedList only)__
    - Finds the frequencies of all elements of the given `OverloadedList` class and returns a list of unique values with their discovered frequencies.
    - Arguments: `self`
    - Returns: `OverloadedList, OverloadedList`
    - Example:

        ```python
            values: Overloadedlist, frequencies: OverloadedList = obj.frequencies
        ```

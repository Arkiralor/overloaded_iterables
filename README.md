# Overloaded Iterables

Overloaded version of the built-in python classes: `<list>` and `<set>` to include some extra functionalities as an experiment.

The current iteration contains the following classes

## Specifications

1. __Python Version:__ Python v3.8+
2. __Code Coverage:__ ![_code coverage_](media\screenshots\coverage.PNG)
3. __Tests Status:__ ![_test status_](media\screenshots\test_results.PNG)

## Python Package Index

1. [Project Homepage](https://pypi.org/project/overloaded-iterables/)
2. [Contents](https://pypi.org/project/overloaded-iterables/#files)

## Installation

```sh
python -m pip install overloaded-iterables
```

## Classes

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

2. `<class>.sort()`
    - Sorts the contents of the given iterable class object via the [Timsort](https://en.wikipedia.org/wiki/Timsort) sorting algorithm.
    - Arguments: `self`, `reverse:bool | default: False`
    - Returns `object: <list>`
    - Example:

        ```python
            sorted_seq: list = obj.sort()
        ```

3. `<class>.raise_to()`
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

4. `<class>.rms()`
    - Finds the [Root-Mean-Square (RMS)](https://en.wikipedia.org/wiki/Root_mean_square) of the values in the current iterable class object.
    - Arguments: `self`
    - Returns: `float (64-bit)`
    - Example:

        ```python
            _rms: float = obj.rms()
        ```

5. `<class>.median()`
    - Finds the [median](https://en.wikipedia.org/wiki/Median) of the contents of the given iterable class object.
    - Arguments: `self`
    - Returns: `float (64-bit)`
    - Example:

        ```python
            _median:float = obj.median()
        ```

6. `<class>.len (property)`
    - Finds and returns the length of the current iterable class object as a property.
    - Arguments: `self`
    - Returns: `int`
    - Example:

        ```python
            _l: int = obj.len
        ```

7. `<class>.frequencies (property)`&nbsp;&nbsp;&nbsp;&nbsp;__(OverloadedList only)__
    - Finds the frequencies of all elements of the given `OverloadedList` class and returns a list of unique values with their discovered frequencies.
    - Arguments: `self`
    - Returns: `OverloadedList, OverloadedList`
    - Example:

        ```python
            values: Overloadedlist, frequencies: OverloadedList = obj.frequencies
        ```

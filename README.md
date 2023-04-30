# Overloaded Iterables

Overloaded version of the built-in python classes: `<list>` and `<set>` to include some extra functionalities as an experiment.

The current iteration contains the following classes

## Specifications

1. Python Version: Python v3.8+
2. Code Coverage: 91%

## Classes

1. `OverloadedList`
    - A non-datatype constrained, single-dimensional collection of values.
    - Inherits solely from Python's built-in `<list>` class.

    ```python
    
    ```

2. `OverloadedSet`
    - A non-datatype constrained, single-dimensional collection of __unique__ values.
    - Inherits solely from Python's built-in `<set>` class.

## Functions and Methods

1. `<class>.mean()`
    - Find the [mean](https://en.wikipedia.org/wiki/Arithmetic_mean) of the values in the given iterable class object.
    - Arguments: `self`
    - Returns: `float (64-bit)`
2. `<class>.sort()`
    - Sorts the contents of the given iterable class object via the [Timsort](https://en.wikipedia.org/wiki/Timsort) sorting algorithm.
    - Arguments: `self`, `reverse:bool | default: False`
    - Returns `object: <class>`
3. `<class>.raise_to()`
    - Raises each element in the iterable class object to the given power.
    - Arguments: `self`, `power: float (64-bit) | default: 1.0`
    - Returns `object: <class>`
4. `<class>.rms()`
    - Finds the [Root-Mean-Square (RMS)](https://en.wikipedia.org/wiki/Root_mean_square) of the values in the current iterable class object.
    - Arguments: `self`
    - Returns: `float (64-bit)`
5. `<class>.median()`
    - Finds the [median](https://en.wikipedia.org/wiki/Median) of the contents of the given iterable class object.
    - Arguments: `self`
    - Returns: `float (64-bit)`
6. `<class>.len (property)`
    - Finds and returns the length of the current iterable class object as a property.
    - Arguments: `self`
    - Returns: `int`
7. `<class>.frequencies (property)`&nbsp;&nbsp;&nbsp;&nbsp;__(OverloadedList only)__
    - Finds the frequencies of all elements of the given `OverloadedList` class and returns a list of unique values with their discovered frequencies.
    - Arguments: `self`
    - Returns: `OverloadedList, OverloadedList`

# Overloaded Iterables

Overloaded versions of the built-in python classes: `<list>` and `<set>`, to include some extra functionalities as an experiment.

An experimental Python package to extend the methods found in Python's built-in list and set classes to add some extra functionality that I, personally find useful in my day-to-day implementations and was too lazy to keep writing/copy-pasting again and again.

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

### 2. Queue

- A non-datatype constrained, single-dimensional collection of values that follows the _first-in-first-out __(FiFo)___ principle for insertions and deletion i.e, insertions will be made to the end of the sequence while deletions will be made to the beginning of the sequence.
- Inherits solely from the `<OverloadedList>` class.

```python
from overloaded_iterables.classes import Queue

obj = Queue(*args)
```

### 3. Stack

- A non-datatype constrained, single-dimensional collection of values that follows the _first-in-last-out __(FiLo)___ principle for insertions and deletion i.e, insertions and deletions, both will be made to the end of the sequence.
- Inherits solely from the `<OverloadedList>` class.

```python
from overloaded_iterables.classes import Stack

obj = Stack(*args)
```

### 4. OverloadedSet

- A non-datatype constrained, single-dimensional collection of __unique__ values.
- Inherits solely from Python's built-in `<set>` class.

```python
    from overloaded_iterables.classes import OverloadedSet

    obj = OverloadedSet(*args)
```

## Functions and Methods

The functions, methods and properties are categorised into two segments: for the base classes (`OverloadedList` and `OverloadedSet`) and for the
inheriting classes (`Queue` and `Stack`)

### OverloadedList and OverloadedSet

The following are the functions, methods and properties belonging to the base classes.

`OverloadedList` being a daughter of the `<list>` class, inherits all of its associated methods and properties as well, such as `append()`, `extend()`, `count()`, _et cetera_.

`OverloadedSet` being a daughter of the `<set>` class, inherits all of its associated methods and properties as well, such as `add()`, `clear()`, `difference()`, _et cetera_.

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

### Queue and Stack

The following are the functions, methods and properties belonging to the inheriting (daughter) classes.

`Queue` and `Stack` being daughters of the `OverloadedList` class, inherit all of its associated methods and properties as well, such as `mean()`, `rms()`, `frequencies`, _et cetera_.

1. `<class>.insert()`

    - Inserts `value` towards the end of the object.
    - Arguments: `self`, `value: any`
    - Returns: `None` _(is an in-place method)_
    - Example:

        ```python
            queue = Queue(*args)
            stack = Stavk(*args)
            queue.insert(value=value)
            stack.insert(value=value)
        ```

2. `<class>.pop()`

    - Deletes `num` elements from the beginning of the object in case of `Queue` and from the end of the object in case of `Stack`.
    - Arguments: `self`, `num: int | default: 1`
    - Returns: `None` _(is an in-place method)_
    - Example:

        ```python
            queue = Queue(*args)
            stack = Stack(*args)
            queue.pop(num=num)
            stack.pop(num=num)
        ```

## Development Setup

1. `git clone https://<personal-access-token>@github.com/Arkiralor/overloaded_iterables.git`
2. `cd overloaded_aiterables`
3. `python -m venv env`
4. `source env/bin/activate`
   1. `source env/Scripts/activate` for Windows.
5. `chmod +x scripts/*`
6. `sh scripts/install.sh` to install all dependencies.
   1. `sh scripts/uninstall.sh` to uninstall all dependencies (can be very useful if you forgot to activate the `virtualEnvironment` before running `install.sh`).
7. `sh scripts/generate_coverage_report` && `sh scripts/run_tests.sh` to make sure everything is working as intended.

## Contribution

If you choose to contribute to this package by addressing any of the issues or tickets listed, kindly follow the following workflow.

1. Assign yourself of ask an administrator to assign yourself to the issue.
2. Clone/fork the codebase and setup the development environment as shown above.
3. Checkout to your own branch, which should ideally be named what the ticket number is in a url-safe format i.e, if the ticket name is `WEB_003`, then the branch name will be `web-003`.
4. `git push --set-upstream origin <branchName>` to pre-create the necessary branch on github.
5. Make the required changes to the correct files in the `src` directory.
6. Add any testCases required to the correct module/file/class in the `tests` directory.
7. `sh scripts/run_tests.sh` to make sure no breaking changes were made.
   1. __MAKE SURE ALL TESTS PASS BEFORE PROCEEDING TO THE NEXT STEP(S)__
8. Add and commit your changes to your branch with a relevant commit message.
9. `git merge origin/master` to pull from the master branch to your branch.
10. `sh scripts/run_tests.sh` again to make sure nothing was broken by the merge.
    1. __MAKE SURE ALL TESTS PASS BEFORE PROCEEDING TO THE NEXT STEP(S)__
11. `git push` to push the changes to the remote branch.
12. Create a Pull Request from your remote branch to `master`.
    1. If any code changes were requested, execute them as requested and restart from step #6.

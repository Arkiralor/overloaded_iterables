
class OverloadedList(list):
    """
    Overloaded <list> class to add additional methods.
    """
    iZERO: int = 0
    fZERO: float = 0.0

    def mean(self) -> float:
        """
        Returns the arithmetic mean of the values in the OverloadedList.
        """
        return self.sum()/self.len

    def sum(self) -> float:
        """
        Calculates and returns the sum of all the elements in the OverloadedList object.
        """
        if self.len == self.iZERO:
            return self.fZERO

        _sum = self.fZERO
        try:
            for item in self:
                _sum = _sum + item
            return float(_sum)
        except Exception as ex:
            raise ex

    def prod(self) -> float:
        """
        Calculates and returns the product of all the elements in the OverloadedList object.
        """
        if self.len == self.iZERO:
            return self.fZERO

        if self.iZERO in self or self.fZERO in self:
            return self.fZERO
        _prod = 1

        try:
            for item in self:
                _prod = _prod*item
            return float(_prod)
        except Exception as ex:
            raise ex

    def sort(self, key: None = None, reverse: bool = False, *args, **kwargs):
        """
        Sorts the OverloadedList object using python's `sorted()` function which
        uses the `TimSort` sorting algorithm with time complexity of O(n log(n))

        returns:
            OverloadedList
        """
        return self._type(sorted(self, key=key, reverse=reverse))

    def raise_to(self, power: float = 1):
        """
        Creates an OverloadedList where each item is the corresponding item
        in the OverloadedList object raised to the power of `power: float | default: 1.0`
        """
        return self._type([item**power for item in self])

    def rms(self, power: float = 2, root: int = 2, *args, **kwargs) -> float:
        """
        Find the root-mean-square of the values in the OverloadedList object.
        RMS basically means the square-root of the arithmetic mean of the squares of the values in a sequence.
        """
        try:
            return (self._type(self.raise_to(power=power)).mean()**(1/root))
        except Exception:
            return float()

    def median(self) -> float:
        """
        Finds and returns the meadian value of the contents of the OverloadedList object.
        """
        _sorted, _l = self.sort(), self.len
        if _l <= 0:
            return float()
        if _l == 1:
            return _sorted[0]

        if _l > 1 and _l % 2 == 0:
            return ((_sorted[(_l-1)//2])+(_sorted[((_l-1)//2)+1]))/2
        elif _l > 1 and _l % 2 == 1:
            return _sorted[(_l)//2]
        else:
            return float()

    @property
    def _type(self):
        """
        Return the type of the current OverloadedList object, which will of course, always be `OverloadedList`.
        
        This is more for internal use in the object methods than for use in implementations, assuming a property of a
        class object is persistent in memory unless garbage-collected or updated and hence will be cheaper to call than
        a full method/function. 

        I might be grossly mistaken in this however so feel free to correct me (with proof, kindly).
        """
        return type(self)

    @property
    def len(self) -> int:
        """
        Return the length of the current OverloadedList object.

        Assuming a property of a class object is persistent in memory unless garbage-collected or updated and hence will be cheaper to call than
        a full method/function. 

        I might be grossly mistaken in this however so feel free to correct me (with proof, kindly).
        """
        count = 0
        for _ in self:
            count = count + 1
        return count

    @property
    def frequencies(self):
        """
        Finds and returns the frequencies of the values in th `OverloadedList` object.

        Assuming a property of a class object is persistent in memory unless garbage-collected or updated and hence will be cheaper to call than
        a full method/function. 

        I might be grossly mistaken in this however so feel free to correct me (with proof, kindly).
        """
        try:
            values = type(self)(OverloadedSet(self))
            frequencies = type(self)()

            for item in values:
                frequencies.append(self.count(item))

            return values, frequencies
        except Exception:
            return type(self)(), type(self)()


class OverloadedSet(set):
    """
    Overloaded <set> class to add additional methods.
    """
    iZERO: int = 0
    fZERO: float = 0.0

    def mean(self):
        """
        Returns the arithmetic mean of the values in the OverloadedSet object.
        """
        return self.sum()/self.len

    def sum(self):
        """
        Calculates and returns the sum of all the elements in the OverloadedSet object.
        """
        if self.len == self.iZERO:
            return self.fZERO

        _sum = 0
        try:
            for item in self:
                _sum = _sum + item
            return float(_sum)
        except Exception as ex:
            raise ex

    def prod(self):
        """
        Calculates and returns the product of all the elements in the OverloadedSet object.
        """
        if self.len == self.iZERO:
            return self.fZERO

        if self.iZERO in self or self.fZERO in self:
            return self.fZERO

        _prod = 1
        try:
            for item in self:
                _prod = _prod*item
            return float(_prod)
        except Exception as ex:
            raise ex

    def sort(self, reverse: bool = False):
        """
        Sorts the OverloadedSet object using python's `sorted()` function which
        uses the `TimSort` sorting algorithm with time complexity of O(n log(n))

        returns:
            OverloadedList
        """
        return sorted(self, reverse=reverse)

    def raise_to(self, power: float = 1):
        """
        Creates an OverloadedSet where each item is the corresponding item
        in the OverloadedSet object raised to the power of `power: float | default: 1.0`
        """
        return self._type([item**power for item in self])

    def rms(self, power: float = 2, root: int = 2, *args, **kwargs):
        """
        Find the root-mean-square of the values in the OverloadedSet object.
        RMS basically means the square-root of the arithmetic mean of the squares of the values in a sequence.
        """
        try:
            return (self._type(self.raise_to(power=power)).mean()**(1/root))
        except Exception:
            return float()

    def median(self):
        """
        Finds and returns the meadian value of the contents of the OverloadedSet object.
        """
        _sorted, _l = OverloadedList(self.sort()), self.len
        if _l <= 0:
            return float()

        if _l == 1:
            return _sorted[0]

        if _l > 1 and _l % 2 == 0:
            return ((_sorted[(_l-1)//2])+(_sorted[((_l-1)//2)+1]))/2
        elif _l > 1 and _l % 2 == 1:
            return _sorted[(_l)//2]
        else:
            return float()

    @property
    def _type(self):
        """
        Return the type of the current OverloadedSet object, which will of course, always be `OverloadedSet`.
        
        This is more for internal use in the object methods than for use in implementations, assuming a property of a
        class object is persistent in memory unless garbage-collected or updated and hence will be cheaper to call than
        a full method/function. 

        I might be grossly mistaken in this however so feel free to correct me (with proof, kindly).
        """
        return type(self)

    @property
    def len(self):
        """
        Return the length of the current OverloadedSet object.

        Assuming a property of a class object is persistent in memory unless garbage-collected or updated and hence will be cheaper to call than
        a full method/function. 

        I might be grossly mistaken in this however so feel free to correct me (with proof, kindly).
        """
        count = 0
        for _ in self:
            count = count + 1
        return count

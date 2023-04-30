
class OverloadedList(list):
    """
    Overloaded <list> class to add additional methods.
    """

    def mean(self):
        return sum(self)/len(self)

    def sort(self, reverse: bool = False):
        return self._type(sorted(self, reverse=reverse))

    def raise_to(self, power: float = 1):
        return self._type([item**power for item in self])

    def rms(self):
        try:
            return (self._type(self.raise_to(power=2)).mean()**(1/2))
        except Exception:
            return float()

    def median(self):
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
        return type(self)

    @property
    def len(self):
        return len(self)

    @property
    def frequencies(self):
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

    def mean(self):
        return sum(self)/len(self)

    def sort(self, reverse: bool = False):
        return sorted(self, reverse=reverse)

    def raise_to(self, power: float = 1):
        return self._type([item**power for item in self])

    def rms(self):
        try:
            return (self._type(self.raise_to(power=2)).mean()**(1/2))
        except Exception:
            return float()

    def median(self):
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
        return type(self)

    @property
    def len(self):
        return len(self)

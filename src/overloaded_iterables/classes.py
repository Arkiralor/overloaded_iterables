from datetime import datetime
from os import path
from typing import List

import matplotlib.pyplot as plt
from numpy import ndarray, array


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

    def draw(self, fig_type: str = 'hist', **kwargs):
        """
        Draw the frequency distribution graph of the values in the OverloadedList object.

        args:
            fig_type:str = 'hist' | 'plot' | 'scatter'
            kwargs: dict = self.hist.kwargs | self.plot.kwargs | self.scatter.kwargs
        """
        method_exception = Exception(
            message="Could not generate/save graph.",
            code="graph_generation_error"
        )
        if fig_type.lower().strip() == 'hist':
            res = self.hist(**kwargs)
        elif fig_type.lower().strip() == 'plot':
            res = self.plot(**kwargs)
        elif fig_type.lower().strip() == 'scatter':
            res = self.scatter(**kwargs)

        else:
            raise Exception(
                message=f"Unsupported argument 'fig_type': {fig_type}",
                code='unknown_fig_type'
            )

        if not res:
            raise method_exception

        return True

    def hist(
        self,
        bins: int = 10,
        title: str = 'Figure 1',
        x_label: str = 'X-axis --->',
        y_label: str = 'Y-axis --->',
        save_dir: str = None,
        file_name: str = None,
        histtype: str = 'step',
        align: str = 'mid',
        orientation: str = 'vertical',
        log_scale: bool = False,
        *args,
        **kwargs
    ) -> bool:
        """
        Draws and saves if required, the histogram of the frequency distribution of the elements of the OverloadedList object.
        """
        try:
            x_axis = array(self)
            plt.hist(
                x=x_axis,
                bins=bins,
                histtype=histtype,
                align=align,
                orientation=orientation,
                log=log_scale
            )
            plt.title(title)
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.show()

            if save_dir:
                file_name = f"{file_name.lower().strip()}.PNG" if file_name else f"{title.lower().strip()}__hist__{datetime.utcnow()}.PNG"
                save_path = path.join(
                    save_dir, file_name)
                plt.savefig(save_path)

            return True
        except Exception as ex:
            raise ex

    def plot(
            self,
            title: str = 'Figure 1',
            x_label: str = 'X-axis --->',
            y_label: str = 'Y-axis --->',
            save_dir: str = None,
            file_name: str = None,
            color: str = '#ffffff',
            linewidth: float = 1,
            marker: str = ',',
            markerfacecolor: str = '#252525',
            marker_size: float = 1.0,
            *args,
            **kwargs
    ):
        """
        Draws and saves if required, the line-plot of the frequency distribution of the elements of the OverloadedList object.
        """
        try:
            x_axis, y_axis = self.frequencies
            x_axis = array(x_axis)
            y_axis = array(y_axis)
            plt.plot(x_axis, y_axis, color=color, linewidth=linewidth, marker=marker,
                     markerfacecolor=markerfacecolor, markersize=marker_size)
            plt.title(title)
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.show()

            if save_dir:
                file_name = f"{file_name.lower().strip()}.PNG" if file_name else f"{title.lower().strip()}__hist__{datetime.utcnow()}.PNG"
                save_path = path.join(
                    save_dir, file_name)
                plt.savefig(save_path)

            return True
        except Exception as ex:
            raise ex

    def scatter(
            self,
            title: str = 'Figure 1',
            x_label: str = 'X-axis --->',
            y_label: str = 'Y-axis --->',
            save_dir: str = None,
            file_name: str = None,
            size: List[float] = [1.25],
            color: str = '#ffffff',
            marker: str = ',',
            line_width: float = 0.25
    ):
        """
        Draws and saves if required, the scatter-plot of the frequency distribution of the elements of the OverloadedList object.
        """
        try:
            x_axis, y_axis = self.frequencies
            x_axis = array(x_axis)
            y_axis = array(y_axis)
            plt.scatter(x=x_axis, y=y_axis, s=array(size),
                        color=color, marker=marker, linewidths=line_width)
            plt.title(title)
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.show()
            
            if save_dir:
                file_name = f"{file_name.lower().strip()}.PNG" if file_name else f"{title.lower().strip()}__hist__{datetime.utcnow()}.PNG"
                save_path = path.join(
                    save_dir, file_name)
                plt.savefig(save_path)

            return True
        except Exception as ex:
            raise ex

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

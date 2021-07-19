import itertools
import math
# Obtained from https://github.com/tylerburdsall/lazy-cartesian-product-python
from LazyCartesianProduct import LazyCartesianProduct

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
             'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
specialchar = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
               ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']


def scheme_multilist(chartypes):
    return list(itertools.chain(uppercase if "u" in chartypes else [],
                                lowercase if "l" in chartypes else [],
                                numbers if "n" in chartypes else [],
                                specialchar if "s" in chartypes else []))


def parse_scheme(scheme):
    partial = [genfrag.split(":") for genfrag in scheme.split("-")]
    return [[charfrag[0], int(charfrag[1])] for charfrag in partial]


class IterableLCP(LazyCartesianProduct):
    currentIndex = 0
    
    def __init__(self, sets, repeat=1):
        self.sets = sets * repeat
        self.divs = []
        self.mods = []
        self.precompute()
    
    def __len__(self):
        return math.prod([len(i) for i in self.sets])
    
    def __getitem__(self, index):
        return self.entryAt(index)

    def __iter__(self):
        return self
    
    def __next__(self):
        return self.next()
    
    def next(self):
        if self.currentIndex < self.__len__():
            currentVal = self.entryAt(self.currentIndex)
            self.currentIndex += 1
            return currentVal
        raise StopIteration()

    def precompute(self):
        length = len(self.sets)
        factor = 1
        for i in range((length - 1), -1, -1):
            items = len(self.sets[i])
            self.divs.insert(0, factor)
            self.mods.insert(0, items)
            factor = factor * items

    def entryAt(self, n):
        length = len(self.sets)
        if n < 0 or n >= self.__len__():
            raise IndexError
        combination = []
        for i in range(0, length):
            combination.append(
                self.sets[i][int(math.floor(n / self.divs[i])) % self.mods[i]])
        return combination

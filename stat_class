#class stat testing

import math
import random

mydata = [1, 2, 3, 4, 5, 6]
mydatados = [1, 2, 3, 4, 5]

class Dset(object):
    def __init__(self, array):
        self.array = array
    def mean(self):
        return sum(self.array) / len(self.array)
    def stdv(self):
        sqdif = 0
        for i in range(0,len(self.array)):
            sqdif += (self.array[i] - self.mean()) ** 2
        return math.sqrt(sqdif / len(self.array))
    def med(self):
        length = len(self.array)
        sorts = sorted(self.array)
        if length % 2 == 0:
            return (sorts[length / 2] + sorts[(length / 2) - 1]) / 2.0
        else:
            return sorts[length / 2]
    def mode(self):
        length = len(self.array)
        sorts = sorted(self.array)
        return sorts[length - 1]
    def variance(self):
        sqdif = 0
        for i in range(0,len(self.array)):
            sqdif += (self.array[i] - self.mean()) ** 2
        return sqdif / len(self.array)
    

mydata1 = Dset(mydata)
mydata2 = Dset(mydatados)

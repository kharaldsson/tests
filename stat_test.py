#function for finding the standard deviation of an array of numbers

import math
import random


mydata = [1, 2, 3, 4, 5]

def stdv(ds):
    mean = sum(ds)/len(ds)
    sqdif = 0
    for i in range(0,len(ds)):
        sqdif += (ds[i] - mean) ** 2
    return math.sqrt(sqdif / len(ds))

print stdv(mydata)

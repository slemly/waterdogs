'''
@author Samuel Lemly
EGR 361 Analysis of Engineering Data, Water Dogs
'''
import pandas as pd
import numpy as np
import math

def runTTest(data, spefconst):
    mean = np.average(data)
    numerator = (mean - spefconst)
    denominator = (np.std(data))/math.sqrt(len(data))
    return (numerator/denominator)
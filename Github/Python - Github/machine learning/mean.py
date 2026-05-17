
import numpy 
from scipy import stats

grades = [12,67,90,67,45,99,100]

mean = numpy.mean(grades)
median = numpy.median(grades)
mode = stats.mode(grades)
print(mean)
print(median)
print(mode)
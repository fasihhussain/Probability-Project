from matplotlib import pyplot as plt
import numpy as np
import scipy.stats as stats
import pylab as pl
import math

lst = []

with open('l_result_equal.txt') as fle:
    for line in fle:
        lst.append(eval(line))
        

lst = sorted(lst)

fit = stats.norm.pdf(lst, np.mean(lst), np.std(lst))  #this is a fitting indeed

pl.plot(lst,fit,'-o')

pl.hist(lst,normed=True)      #use this to draw histogram of your data

pl.show()
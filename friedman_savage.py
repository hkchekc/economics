import numpy as np
import scipy.stats
from scipy.stats import uniform
import matplotlib.pyplot as plt
import random
import math
import scipy.integrate as integrate


def fs (xl):
    stli = []
    for x in xl:
        res = (x-5) ** 3 + 125
        stli.append(res)
    return stli

plt.plot( fs(np.arange(0,10,0.1)), 'g^')
plt.show()
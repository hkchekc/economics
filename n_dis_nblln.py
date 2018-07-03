import time
from decimal import *
import numpy as np
import scipy.stats as ss
from scipy.special import gamma, factorial
import math
import matplotlib.pyplot as plt

# MLR satisfied
# mean satisfied
# not all in range (0,1)


def ndis(theta = 0.5, episilon = 0.1, beta=np.arange(0, 1, 0.1, float)):
    norm = ss.norm
    x = norm(theta,episilon)
    pdf = x.pdf(beta)
    return pdf

f= ndis(theta=0.5, episilon=0.15)
g= ndis(theta=0.5,episilon=0.2)

mlr = g/f
print(mlr)

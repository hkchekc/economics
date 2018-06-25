import time
from decimal import *
import numpy as np
import scipy
from scipy.special import gamma, factorial
import math
import matplotlib.pyplot as plt


def para_mod_bdis(psi=10, beta=np.arange(0, 1, 0.1, float), theta=0.5):
    a = scipy.special.gamma(psi)
    b = scipy.special.gamma(theta * psi)
    c = scipy.special.gamma((1-theta) * psi)

    gamma_group = a/(b*c)

    fst_beta = beta ** ((theta*psi)-1)
    snd_beta = (1-beta)**(((1-theta)*psi)-1)

    dis = fst_beta*snd_beta*gamma_group
    return dis


print(para_mod_bdis())





import time
from decimal import *
import numpy as np
import scipy.stats as ss
from scipy.special import gamma, factorial
import math
import matplotlib.pyplot as plt


def udis(theta = 0.5, episilon = 0.1, betas=np.arange(0, 1, 0.1, float)):
    pdfs = []
    for beta in betas:
        ulim = theta + episilon
        llim = theta - episilon
        rest = 1- ulim + llim
        cdf_inlim = 0.5
        cdf_rest = 0.5
        if beta <= ulim and beta >= llim:
            pdf = cdf_inlim/(2*episilon)
            pdfs.append(pdf)
        else:
            pdf = cdf_rest/rest
            pdfs.append(pdf)

    np.array(pdfs)
    return pdfs


def udis_cdf(theta = 0.5, episilon = 0.1, betas=np.arange(0, 1, 0.1, float), ulim = 1):
    cdf = 0
    for beta in betas:
        if beta <= ulim:
            pdf = udis(theta, episilon, betas)
            cdf += pdf
    return cdf

print(udis(episilon=1/7))
print(udis(episilon=1/15))
import time
from decimal import *
import numpy as np
import scipy.stats as ss
from scipy.special import gamma, factorial
import math
import matplotlib.pyplot as plt

def udis_sp(theta = 0.5, epsilon = 0.2, betas=np.arange(0, 1, 0.1, float)):
    pdfs = []
    for beta in betas:
        ulim = theta + epsilon
        llim = theta - epsilon
        rest = 1- ulim + llim
        cdf_inlim = 0.8
        cdf_rest = 0.2
        if beta <= ulim and beta >= llim:
            pdf = cdf_inlim/(2*epsilon)
            pdfs.append(pdf)
        else:
            pdf = cdf_rest/rest
            pdfs.append(pdf)

    pdfs = np.array(pdfs)
    return pdfs

def udis(theta = 0.5, epsilon = 0.2, betas=np.arange(0, 1, 0.1, float)):
    pdfs = []
    for beta in betas:
        ulim = theta + epsilon
        llim = theta - epsilon
        if beta <= ulim and beta >= llim:
            pdf = 1/(2*epsilon)
            pdfs.append(pdf)
        else:
            pdf = 0
            pdfs.append(pdf)
    pdfs = np.array(pdfs)
    return pdfs

def udis_cdf(theta = 0.5, epsilon = 0.2, betas=np.arange(0, 1, 0.1, float), ulim = 1.00):
    keep = []
    for beta in betas:
        keep.append(beta <= ulim)
    betas = betas[keep]
    pdf = udis(theta, epsilon, betas)
    cdf = pdf.sum()
    return cdf


def plot_cdf(theta = [0.5], epsilon = 0.2, betas=np.arange(0, 1, 0.1, float)):
    for i, t in enumerate(theta):
        cdf = []
        for beta in betas:
            cdf.append(udis_cdf(betas=betas, ulim= beta, theta=t,epsilon=epsilon))
        cdf = np.array(cdf)
        if i == 0:
            plt.plot(betas, cdf, color="red", label='{}'.format(t))
        else:
            plt.plot(betas, cdf, color="blue", label='{}'.format(t))

    plt.xlabel('Proportion of Heads')
    plt.ylabel('CDF')
    plt.title("CDF Comparison between theta={}".format(theta))
    plt.legend()
    plt.yticks([])
    plt.plot()
    plt.show()
    return


print(udis())

plot_cdf(theta=[0.4, 0.6])
print("cdf is ", udis_cdf(ulim=0.81))
import numpy as np
import scipy.stats
from scipy.stats import uniform
import matplotlib.pyplot as plt
import random
import math
import scipy.integrate as integrate


sigm = [0.1, 0.5,1 , 3, 6, 12, 50]
for sig in sigm:
    gvar = sig*2
    g_dis = scipy.stats.norm(0, math.sqrt(gvar))
    g0 = g_dis.pdf(0)
    print('-------------------------------------------')
    print('var is', sig)
    y0 = 100
    rev_s = -20*y0
    mu = rev_s/(rev_s+sig*math.pi)
    print('mu is ', mu)
    w2 = mu - mu/(2*g0)
    w1 = mu + mu/(2*g0)
    sd = scipy.stats.norm(0,1)
    util = (0.5*(y0 + w1 - (mu**2)/2 -15)**2)*(0.5) + (0.5*(y0 + w2 - (mu**2)/2 -15)**2)*(0.5)
    print(util)








# fig, ax = plt.subplots(1, 1)
#
# mean, var, skew, kurt = uniform.stats(moments='mvsk')
# x = np.linspace(uniform.ppf(0.01), uniform.ppf(0.99), 100)
# y = np.linspace(uniform.ppf(0.01), uniform.ppf(0.99), 100)
# z= []
# for i in range(10000):
#     xr = random.choice(x)
#     yr = random.choice(y)
#     ze = yr-xr
#     z.append(ze)
# ax.plot(z, uniform.pdf(z), 'r-', lw=5, alpha=0.6, label='uniform pdf')
#
# #rv = uniform()
# #ax.plot(z, rv.pdf(z), 'k-', lw=2, label='frozen pdf')
# plt.show()
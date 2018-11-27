import numpy as np
import scipy.stats
from scipy.stats import uniform
import matplotlib.pyplot as plt
import random
import math
import scipy.integrate as integrate

sigm = [0.1, 0.5,1 , 3, 6, 12, 50]
for sig in sigm:
    print('-------------------------------------------')
    print('var is', sig)
    y0 = 100
    a = 2
    b = -15
    rev_s = -20*y0
    mu = rev_s/(rev_s+sig)
    print('mu is ', mu)
    r = rev_s/(rev_s+sig)
    I = sig/(rev_s + sig)**2
    sd = scipy.stats.norm(0,1)

    def drra(ep):
        pdf = sd.pdf(ep)
        if pdf > 0.0000000000000000000001:
            util = 0.5 * (y0 + I + r * mu + r * ep - (mu ** 2) / 2) ** 2
        else:
            util = 0
        final = util*pdf

        return final


    # the param is std
    ste = 0.01
    lin = np.arange(-100, 100, ste)
    result = integrate.quad(drra, -100, 100)
    print('drra eu is', result)
    kkkkk= float(result[0])
    kkkkkkkkkkkkkkkk =kkkkk*0.25
    print('eu is', kkkkkkkkkkkkkkkk)
    su = []
    for i in lin:
        pdf = sd.pdf(i)
        cal = drra(i)
        su.append(cal)
    x =sum(su)* ste
    print(x)




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

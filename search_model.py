import numpy as np
import scipy.stats as stat
import numpy.ma

# structural parameters
alpha = 1/3
lamb = 0.02
beta = 0.99
b =0.75
w_max = 2
w_min = 0
n_max = 1
n_min = -1
s_cost = 0.2

#VFI

n = 1e+4
wage = np.linspace(w_min,w_max,int(n))

crit = 1e-12
metric = 1
ns = np.linspace(n_min, n_max, int(n))
inRate = 0  # people who do not find job
uRate = 0
exp_wage = 0
eRate = 1 - inRate - uRate  # res_wage/
res_wage = 0
res_wage_cdf = (res_wage - w_min)/(w_max-w_min)
# Initial Guesses

U = b
W = wage
S = -s_cost
N = ns
profit = eRate - exp_wage
while metric > crit:
    wage_cdf = (wage - w_min) / (w_max - w_min)
    W_new = wage + beta * (1 - lamb) * W + lamb * beta * U
    uexp = max([np.transpose(W), U*np.ones(1,n)])*[wage_cdf[0],
                                wage_cdf[1:-1]-wage_cdf[0:-2], 1-wage_cdf[-1]]
    U_new = b + beta * alpha *uexp + beta * (1 -alpha) * U
    res_wage = min(w for w in W_new > U_new)
    S_new = alpha* (1 - res_wage_cdf)*W_new +(alpha* res_wage_cdf + (1 - alpha)) * U_new -s_cost
    nexp = max([S*np.ones(1, n), np.transpose(ns)]) * wage_cdf
    N_new = ns + beta *nexp
    res_search = min(s for s in (-N + S) > 0) # company want it reach certain percentage
    avg_wage = (1 / (w_max - res_wage)) * (w_max ^ 2 - res_wage ^ 2) / 2
    inRate = 1 - len([i for i in (-N + S) > 0])/ len(N)
    uRate = lamb/(lamb + alpha*(1-res_wage/(w_max-w_min)))
    eRate = 1 - inRate - uRate  # res_wage/
    Profit_new = eRate - avg_wage # solve for maximizing profit
    res_wage_cdf = (res_wage - w_min) / (w_max - w_min)
    metric = max([abs(W_new - W)/ 1 + abs(W), abs(U_new-U)/1+abs(U),
                abs(N_new - N)/ 1 + abs(N), abs(S_new-S)/1+abs(S), abs(Profit_new-profit)/1+abs(profit)])
    W = W_new
    U = U_new
    N = N_new
    S = S_new
    profit = Profit_new

print(res_wage, res_search)
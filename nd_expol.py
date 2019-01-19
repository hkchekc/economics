import numpy as np
import scipy.stats as stats
import matplotlib as mpl
import matplotlib.pyplot as plt

real_state = 9
realised_sig_mean = 9
lb = 0
ub = 10
state_space = np.arange(lb,ub+1, 1)
action_space = state_space
type = state_space
sigdis = stats.truncnorm(a=(lb - realised_sig_mean),
                         b=(ub - realised_sig_mean), loc=realised_sig_mean, scale=1)
priorb = stats.uniform(lb, ub)
def bay_up(prior, cond_prob, sig_prob):
    posterior = cond_prob*prior/sig_prob
    return posterior
def utility(prob, expected, realise): return -prob*abs(expected - realise)
posterior = []
for state in state_space:
    conp = sigdis.pdf(state)
    pri = priorb.pdf(state)
    sigp = pri
    posterior.append(bay_up(pri, conp, sigp))
norm_post = [float(i)/sum(posterior) for i in posterior] # normalized sum to 1
# for i in range(11):
#     print(i, norm_post[i])
prob_sigb = []
for i, state in enumerate(state_space):
    conprobb = sigdis.pdf(state)
    prob_stateb = norm_post[i]
    e = conprobb*prob_stateb
    prob_sigb.append(e)
print(prob_sigb)
print(norm_post)
# x = np.linspace(sigdis.pdf(0.01),
#                 sigdis.ppf(0.99), 100)
# fig, ax = plt.subplots(1, 1)
# ax.plot(x, sigdis.pdf(x),
#         'r-', lw=5, alpha=0.6, label='truncnorm pdf')
# plt.show()
#

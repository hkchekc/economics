import numpy as np
import matplotlib as mpl
import scipy.stats as st
from itertools import permutations
#
#
def pr(sb): return sb*0.5 + (55- sb)*0.05
# def utility(vote, real_state): return 10 - abs(vote - real_state)
# space_lower_bound = 0
# space_upper_bound = 10
# state_space = np.arange(space_lower_bound, space_upper_bound+1, 1)
# prior_belief = st.uniform(state_space)
# print(prior_belief)
# ori_expected = np.mean(state_space)
#

# total = 55
#
# toli = []
#
# for i in range(11):
#     if i == 9:
#         continue
#     a = pr(i)
#     toli.append(a)
#     print(a, i)
#
# print(toli, len(toli), sum(toli))
# print(pr(9))

sa = 9
ee = 6.8
space = [0, 1 ,2,3,4,5,6,7,8,9,10]
li = []
for i, ele in enumerate(space):
    a  = (55 - ele)*0.05 + ele* 0.5
    li.append(a)
print(li)
def pbss(ss):
    if sa!=ss:
        pbfake = 0.5 * 0.0725
        pbsa = 0.05 * 0.275
        pbother = 0.05 * 0.0725 * 9
        sum = pbsa + pbfake + pbother
        return pbsa, pbfake, pbother, sum, False
    else:
        # pbsa,
        pbsa = 0.5 * 0.275
        pbother = 0.0725 * 0.05 * 10
        sum = pbsa + pbother
        return pbsa, 0, pbother, sum, True

def expected(give):
    pbsa, pbfake, pbother, sum, report_truth = pbss(give)
    u = []
    for i, e in enumerate(space):
        a = abs(e-ee)
        ut = a**0.5
        if e == sa:
            prob = pbsa
        elif e == give:
            if e!= sa:
                prob = pbfake
        else:
            prob = pbother
        ep = prob*ut
        u.append(ep)
    return u


k = expected(6)
print(sum(k))
print(sum(expected(10)))

ha = []
for i, e in enumerate(space):
    sq = (e- ee)**2
    ha.append(sq)
print(sum(ha), ha)



print(0.5/0.275)




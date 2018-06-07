import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import stats


poissonLambdas = np.random.randint(0,100,100, 'int')
xs = np.random.randint(50,100,100)

po = []
[po.append(scipy.stats.distributions.poisson.pmf(x, poissonLambda)) for x in xs for poissonLambda in poissonLambdas]

print(po)
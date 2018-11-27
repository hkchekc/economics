import math

for i, x in enumerate([1, 1.39, 0.11, 0.5]):
    print("======================================")
    for y in (0, 0.1, 0.5, 1, 2):
        z = (x+y)*1000000
        print("The expected payoff is {}, initial wealth is {}"
              " and the EU is {}".format(x, y, math.log(z)))

# the EU theory never assume U() can be add from outside!

# the EU theory never stated at with point of lottery is the utility calculated

# here I assume the EU is calculated with expected value.

# y as the initial wealth, which should be included in the VNM theories

# calculating payoff and risk seperately in a form U(x - v(y))?

mt = lambda x: x % 3
a = mt(2)
print(a)

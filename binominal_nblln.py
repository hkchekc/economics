import math

def nCr(n,r):
    n = int(n)
    r = int(r)
    f = math.factorial
    abc = f(n) / f(r) / f(n-r)
    return abc

def coin(flip=100, head=50):
    x =(1/2)**head
    print(x)
    prob = nCr(flip,head)* x
    return prob


print(coin())
print()
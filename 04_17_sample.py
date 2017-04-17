import numpy as np

def update(u, theta):
    if u - theta >= 0:
        return 1
    else:
        return -1

vupdate = np.vectorize(update)

a = np.zeros(16).reshape(4,4)
b = np.identity(4)






print a
print b




"""
print update(3, 5)
print update(5, 1)
a = np.array([0,1])
print vupdate(a,1)
"""


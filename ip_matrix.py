import numpy as np
import matplotlib as mpl
from mpl_toolkits import mplot3d
import logging

mat = np.ones((3,3), int)

mat = np.multiply(mat, (1,0.75, 0.5))
mat = np.transpose(mat)
mat = np.multiply(mat, (1,0.75, 0.5))
logging.debug("abc")
mat1 = mat.tolist()
print(mat1)
mat2 = np.multiply(mat1, 0.75)
mat2 = mat2.tolist()
print(mat2)
mat3 = np.multiply(mat2, 0.5)
mat3 = mat3.tolist()
print(mat3)
#mat1.append([mat2])
#mat1.append([mat3])
#mat1 = np.array(mat1)

#print(mat1)





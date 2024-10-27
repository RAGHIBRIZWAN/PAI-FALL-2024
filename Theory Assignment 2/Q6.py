import numpy as np

a = np.arange(1,5)
b = a.reshape(2,2)

c = np.linalg.det(b)
d = np.linalg.inv(b)

print('Determinant:',c)
print('Inverse:',d)

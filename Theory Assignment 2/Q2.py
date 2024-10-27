import numpy as np

a = np.random.randint(0,100,9)
b = a.reshape(3,3)
c = b.transpose()
print(b,'\n')
print(c)

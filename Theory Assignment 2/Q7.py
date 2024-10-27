import numpy as np

a = np.random.randint(1,100,50)

print(a)
print('Minimum Index:',a.argmin())
print('Maximum Index:',a.argmax())
print('Maximum Value:',a.min())
print('Maximum Value:',a.max())

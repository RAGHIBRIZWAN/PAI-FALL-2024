import numpy as np

a = np.array([[2, -1, 1],
              [1, 3, 2],
              [1, -1, 2]])

b = np.array([8, 13, 17])

solution = np.linalg.solve(a, b)

print("Solution:", solution)

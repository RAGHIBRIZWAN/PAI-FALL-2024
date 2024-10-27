import numpy as np

A = np.array([[2, -1, 1],
              [1, 3, 2],
              [1, -1, 2]])

B = np.array([8, 13, 17])

solution = np.linalg.solve(A, B)

print("Solution:", solution)

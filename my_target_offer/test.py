import numpy as np

x = np.array([[[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]],

              [[11, 21, 31],
               [41, 51, 61],
               [71, 81, 91]],])

i = np.array([[[0],
               [1]]])

j = np.array([[[0, 1, 2]]])

z = np.array([[0]])

print("x[i, j] = ", x[i, j, z])
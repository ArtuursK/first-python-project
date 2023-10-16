

# y:.3f

import numpy as np

# masiviem ieprieks jazin izmers
# rindas - 5
# kolonnas - 3

# tukss 2D masivs
mas = np.empty((5, 3))
print(mas)

# aizpildits 2D masivs
aizpild_2d_mas = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(aizpild_2d_mas[0][1]) # izvada 2

# papildināt 2D masīvu
aizpild_2d_mas.append([10, 11, 12])
print(aizpild_2d_mas[3][1]) # izvada 11


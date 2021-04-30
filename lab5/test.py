from main import find_max, jacobi, print_self
import numpy as np


print("Тест №1")

test = np.array([(5, 1, 2),
                 (1, 4, 1),
                 (2, 1, 3)])

n = len(test)
values, vectors = jacobi(test, n, 0.0001)
print_self(test, values, vectors, n)

print("Тест №2")

test = np.array([(2, 1),
                 (1, 3)])
n = len(test)

values, vectors = jacobi(test, n, 0.0001)
print_self(test, values, vectors, n)

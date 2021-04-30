import math
import numpy as np


def finding_a_matrix_by_formula():
    k = 0
    while k < 1:
        k = int(input("Enter the variant:"))
    size = 0
    while size < 2:
        size = int(input("Enter the size of matrix:"))
    c = [[float(input("Enter the [{0}][{1}] element for matrix c:".format(i, j)))
          for i in range(size)] for j in range(size)]
    d = [[float(input("Enter the [{0}][{1}] element for matrix D:".format(i, j)))
          for i in range(size)] for j in range(size)]
    a = np.array(c) * k + np.array(d)
    b = [float(
        input("Enter the [{0}]element for matrix B:".format(i))) for i in range(size)]
    return a, b


def simple_iteration_method(a, b):
    for i in range(len(a)):
        q = a[i][i]
        a[i] /= q
        b[i] /= q
    a = np.eye(len(a)) - a
    if np.linalg.norm(a, np.inf) >= 1 and np.linalg.norm(a, 1) >= 1 and np.linalg.norm(a) >= 1:
        print("The system is not solved by this method")
        exit(1)
    copy_b = np.copy(b)
    x = np.matmul(a, copy_b) + b
    num_of_iteration = math.ceil(math.log((1e-4 * (1 - np.linalg.norm(a, np.inf))) / np.linalg.norm(x - copy_b, np.inf), np.linalg.norm(a, np.inf)))
    for i in range(num_of_iteration):
        copy_b = x
        x = np.matmul(a, copy_b) + b
    for i in range(len(a)):
        print("X{0} = {1}".format(i + 1, x[i].__format__(".4f")))


def main():
    C = np.array([[0.01, 0, -0.02, 0, 0],
                  [0.01, 0.01, -0.02, 0, 0],
                  [0, 0.01, 0.01, 0, -0.02],
                  [0, 0, 0.01, 0.01, 0],
                  [0, 0, 0, 0.01, 0.01]])

    D = np.array([[1.33, 0.21, 0.17, 0.12, -0.13],
                  [-0.13, -1.33, 0.11, 0.17, 0.12],
                  [0.12, -0.13, -1.33, 0.11, 0.17],
                  [0.17, 0.12, -0.13, -1.33, 0.11],
                  [0.11, 0.67, 0.12, -0.13, -1.33]])

    b = np.array([1.2, 2.2, 4.0, 0.0, -1.2])
    a = np.array(C) * int(input("Enter the variant:")) + np.array(D)
    simple_iteration_method(a, b)
    #simple_iteration_method(finding_a_matrix_by_formula())


if __name__ == '__main__':
    main()

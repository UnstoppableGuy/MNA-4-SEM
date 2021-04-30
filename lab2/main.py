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


def method_seidel(a, b):
    x = [0.0 for i in range(len(a))]
    convergence = False
    while not convergence:
        z = np.copy(x)
        for i in range(len(a)):
            z[i] = (b[i] - sum(a[i][j] * z[j] for j in range(i)) - sum(a[i][j] * x[j] for j in range(i + 1, len(a)))) / a[i][i]
        convergence = sum(abs(z[i] - x[i]) for i in range(len(a))) < 1e-6
        x = z
    return x


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
    solution = method_seidel(a=a, b=b)
    for i in range(len(solution)):
        print("X{0} = {1}".format(i + 1, solution[i].__format__(".4f")))


if __name__ == '__main__':
    main()

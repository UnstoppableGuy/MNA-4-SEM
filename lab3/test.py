import numpy
import sympy as sym
import matplotlib.pyplot as plt
from matplotlib import pylab
from copy import deepcopy

a = -6.4951
b = -31.2543
c = 23.1782

count = 0


def method_shturman(matrix, input_value):
    matrix.append(input_value)

    vec = []
    j = len(input_value) - 1
    for value in input_value:
        vec.append(value * j)
        j -= 1
    matrix.append(vec)

    for m in range(len(matrix[0]) - 2):
        f0 = matrix[m][:]
        f1 = matrix[m+1][:]
        for i in range(2):
            divider = f0[i] / f1[0]
            for j in range(i, len(f1)):
                f0[j] = f0[j] - f1[j - i] * divider
        for i in range(len(f1)):
            if(i >= 2):
                f0[i] = 0
                continue
            f0[i] = round(f0[2 + i], 4) * (-1)
        matrix.append(f0)

    k = -1
    for vec in matrix:
        k += 1
        if k == 0:
            continue
        for i in list(range(len(vec)))[::-1]:
            if(i < k):
                vec[i] = 0
                continue
            vec[i] = vec[i - k]


def Search_root(matrix):
    root = []
    for i in range(-10, 11):
        storage = []
        for vec in matrix:
            sum = 0
            power = len(vec) - 1
            for j in vec:
                sum += j * i ** power
                power -= 1
            if sum > 0:
                storage.append(1)
            elif sum < 0:
                storage.append(-1)
            else:
                storage.append(0)
        storage.append(i)
        N = 0
        for k in range(len(storage) - 2):
            if storage[k] != storage[k+1]:
                N += 1
        storage.append(N)
        root.append(storage)

    return root


"""Shturman method"""
matrix = []
method_shturman(matrix=matrix, input_value=[1., a, b, c])
print("\nShturman method\n")
for i in range(len(matrix)):
    print(*matrix[i], sep="\t")


def equation(x):
    return x ** 3 + a * x ** 2 + b * x + c


xmin = -10.0
xmax = 10
plt.cla()
dx = 0.01
xlist = numpy.arange(xmin, xmax, dx)
ylist = [equation(x) for x in xlist]
plt.plot(xlist, ylist)
plt.grid()
plt.savefig(f"{count}.png")
count+=1
xmin = -5
xmax = 10
plt.cla()
dx = 0.01
xlist = numpy.arange(xmin, xmax, dx)
ylist = [equation(x) for x in xlist]
plt.plot(xlist, ylist)
plt.grid()
plt.savefig(f"{count}.png")


def chord(p_1, p_2, x):
    return (equation(p_1) - equation(p_2)) * (x - p_2) / (p_1 - p_2) + equation(p_2)


"""Chord solution"""


A = -5
B = -4
num = 1


def show_chord(point_1, point_2):
    plt.cla()
    chord_xlist = numpy.arange(point_1, point_2, dx)
    chord_ylist = [chord(point_1, point_2, x) for x in chord_xlist]
    plt.plot(xlist, ylist)
    plt.plot(chord_xlist, chord_ylist)
    plt.grid()
    global count
    count += 1
    plt.savefig(f"{count}.png")


dx = 0.01
xlist = numpy.arange(A, B, dx)
ylist = [equation(x) for x in xlist]
point_1 = A
point_2 = B
show_chord(point_1, point_2)
current_x = point_1 - \
    equation(point_1) * (point_2 - point_1) / \
    (equation(point_2) - equation(point_1))
prev_point = point_1 if equation(
    current_x) * equation(point_1) < 0 else point_2
prev_x = prev_point
epsilon = 0.00001
show_chord(current_x, prev_point)
while abs(prev_x - current_x) > epsilon:
    num = num+1
    point_1 = prev_point
    point_2 = current_x
    show_chord(point_2, point_1)
    prev_x = current_x
    current_x = point_1 - \
        equation(point_1) * (point_2 - point_1) / \
        (equation(point_2) - equation(point_1))
    prev_point = point_1 if equation(
        current_x) * equation(point_1) < 0 else point_2

print("\nMethod chord\n", current_x, "\nИтераций: ", num)


def Diff(f1):
    f2 = []
    power = len(f1) - 1
    for value in f1:
        f2.append(value ** power)
        power -= 1
    f2.pop(len(f2) - 1)
    f2.insert(0, 0)
    return f2


def Newton_method(vector, f0, f1):
    count = 0
    f2 = Diff(f1)

    for vec in vector:
        while True:
            f0_value_b = 0
            f1_value_b = 0
            f0_value_a = 0
            f1_value_a = 0
            f2_value = 0
            power = len(f0) - 1
            for i in range(len(f0)):
                count += 1
                f0_value_b += f0[i] * vec[1] ** power
                f1_value_b += f1[i] * vec[1] ** power

                f0_value_a += f0[i] * vec[0] ** power
                f1_value_a += f1[i] * vec[0] ** power

                f2_value += f2[i] * vec[1] ** power

                power -= 1
            if f0_value_b * f2_value <= 0:
                vec[1] -= 0.0001
            else:
                vec[1] = vec[1] - f0_value_b / f1_value_b
                vec[0] = vec[0] - f0_value_a / f1_value_a
            if vec[1] - vec[0] < 0.00001:
                break
    return vector, count


def Check(root):
    vector = []
    for i in range(20):
        if root[i][5] != root[i + 1][5]:
            vector.append([root[i][4], root[i + 1][4]])
    return vector


matrix = []
method_shturman(matrix, [1., a, b, c])
root = Search_root(matrix)
vector = Check(root)
vector_Newton, count_Newton = Newton_method(
    deepcopy(vector), [1., a, b, c], matrix[1][:])
print(f"\nNewton method\n{vector_Newton[0][1]}")
print(f"Итераций: {count_Newton}")


def Half_division_method(vector, input_value):
    i = 0
    count = 0

    while True:
        power = len(input_value) - 1
        sum_a = 0
        sum_b = 0
        sum_x3 = 0
        for k in range(len(input_value)):
            count += 1
            sum_a += input_value[k] * vector[i][0] ** power
            sum_b += input_value[k] * vector[i][1] ** power
            sum_x3 += input_value[k] * \
                ((vector[i][0] + vector[i][1]) / 2) ** power
            power -= 1
        if sum_a > 0 and sum_x3 < 0:
            vector[i][1] = (vector[i][0] + vector[i][1]) / 2
        elif sum_a < 0 and sum_x3 > 0:
            vector[i][1] = (vector[i][0] + vector[i][1]) / 2
        elif sum_b > 0 and sum_x3 < 0:
            vector[i][0] = (vector[i][0] + vector[i][1]) / 2
        elif sum_b < 0 and sum_x3 > 0:
            vector[i][0] = (vector[i][0] + vector[i][1]) / 2

        if vector[i][1] - vector[i][0] < 0.0001:
            i += 1
            if i >= len(vector[0]):
                break
    return vector, count


vector_half_division, count_half_division = Half_division_method(
    deepcopy(vector), input_value=[1., a, b, c])
print(f"\nHalf division method\n{vector_half_division[0][1]}")
print(f"Итераций: {count_half_division}")

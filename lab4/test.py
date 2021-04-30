import numpy
import sympy as sym
import matplotlib.pyplot as plt
import math
from matplotlib import pylab

m = 0.3
a = 1


def eq_1(x, y):
    return pylab.tan(x * y + m) - x


def eq_2(x, y):
    return a * x**2 + 2 * y**2 - 1


"""Create plots"""


pylab.cla()
y, x = numpy.ogrid[-2:2:1000j, -2:2:1000j]
pylab.contour(x.ravel(), y.ravel(), eq_1(x, y), [0], colors='blue')
pylab.contour(x.ravel(), y.ravel(), eq_2(x, y), [0], colors='red')
pylab.grid()
pylab.savefig("1.png")
pylab.cla()
y, x = numpy.ogrid[0:2:1000j, 0:2:1000j]
pylab.contour(x.ravel(), y.ravel(), eq_1(x, y), [0], colors='blue')
pylab.contour(x.ravel(), y.ravel(), eq_2(x, y), [0], colors='red')
pylab.grid()
pylab.savefig("2.png")


"""Method of standart iterations"""


epsilon = 0.00001
prev_x, prev_y = 1, 0.25


def fi_1(x, y):
    return (numpy.tan(x*y + m))


def fi_2(x, y):
    return ((1 - a*x**2)/2)**(1/2)


current_x, current_y = fi_1(prev_x, prev_y), fi_2(prev_x, prev_y)
num = 1

while (abs(current_x - prev_x) > epsilon or abs(current_y - prev_y) > epsilon):
    prev_x, prev_y = current_x, current_y
    current_x, current_y = fi_1(prev_x, prev_y), fi_2(prev_x, prev_y)
    num += 1
    #print(f"{num}:\t{current_x}:\t{current_y}")

print("Приближенное решение системы методом простых итераций:", current_x, current_y)
print("Количество итераций:", num)


"""Newton Method"""


def eq_1(x, y):
    return sym.tan(x*y + m) - x


def eq_2(x, y):
    return a*x**2 + 2*y**2 - 1


x, y = sym.Symbol('x'), sym.Symbol('y')
eq_1_x_deriv = sym.diff(eq_1(x, y), x, 1)
eq_1_y_deriv = sym.diff(eq_1(x, y), y, 1)
eq_2_x_deriv = sym.diff(eq_2(x, y), x, 1)
eq_2_y_deriv = sym.diff(eq_2(x, y), y, 1)


def Jakobian(X, Y):
    return numpy.array([[float(eq_1_x_deriv.evalf(subs={x: X, y: Y})), float(eq_1_y_deriv.evalf(subs={x: X, y: Y}))],
                        [float(eq_2_x_deriv.evalf(subs={x: X, y: Y})), float(eq_2_y_deriv.evalf(subs={x: X, y: Y}))]])


epsilon = 0.00001
prev_x, prev_y = 1, 0.25
jak = numpy.linalg.inv(Jakobian(prev_x, prev_y))
current_x, current_y = prev_x - (jak[0][0]*eq_1(prev_x, prev_y) +
                                 jak[0][1]*eq_2(prev_x, prev_y)),\
    prev_y - (jak[1][0]*eq_1(prev_x, prev_y) +
              jak[1][1]*eq_2(prev_x, prev_y))
num = 1
while (abs(current_x - prev_x) > epsilon or abs(current_y - prev_y) > epsilon):
    prev_x, prev_y = current_x, current_y
    jak = numpy.linalg.inv(Jakobian(prev_x, prev_y))
    current_x, current_y = prev_x - (jak[0][0]*eq_1(prev_x, prev_y) +
                                     jak[0][1]*eq_2(prev_x, prev_y)),\
        prev_y - (jak[1][0]*eq_1(prev_x, prev_y) +
                  jak[1][1]*eq_2(prev_x, prev_y))
    num += 1

print("Приближенное решение системы методом Ньютона:", current_x, current_y)
print("Количество итераций:", num)
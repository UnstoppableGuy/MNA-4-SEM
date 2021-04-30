import sympy
import numpy
import matplotlib.pyplot as plt
from matplotlib import pylab
list_x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
f = {list_x[0]: 4, list_x[1]: 4.41, list_x[2]: 4.79,
     list_x[3]: 5.13, list_x[4]: 5.46, list_x[5]: 5.76,
     list_x[6]: 7.04, list_x[7]: 7.3, list_x[8]: 7.55,
     list_x[9]: 7.79, list_x[10]: 8.01}

counter = 2


def show_polynome(polynome, text, n, dots):
    xmin = 0
    xmax = 1
    pylab.cla()
    dx = 0.1
    xlist = numpy.arange(xmin, xmax, dx)
    ylist = [polynome(p, n) for p in xlist]
    pylab.plot(xlist, ylist, label=text)
    if dots:
        for i in range(n):
            pylab.plot([list_x[i]], [f[list_x[i]]],
                       marker='o', markersize=7, color="red")
    pylab.grid(True)
    global counter
    counter += 1
    pylab.legend()
    pylab.savefig(f"{counter}.png")


def divided_differences(x):
    if len(x) == 2:
        return (f[x[1]] - f[x[0]]) / (x[1] - x[0])
    return (divided_differences(x[1:]) - divided_differences(x[:-1])) / (x[-1] - x[0])


def newtone_polynome(x, n):
    polynome = f[list_x[0]]
    for i in range(1, n):
        factor = 1
        for j in range(0, i):
            factor *= (x - list_x[j])
        polynome += divided_differences(list_x[0:i + 1]) * factor
    return sympy.expand(polynome)


n = 11
x = sympy.Symbol('x')
print("Интерполяционный многочлен Ньютона:\n", newtone_polynome(x, n))

show_polynome(newtone_polynome, "Полином Ньютона", n, True)

x = list_x[0] + list_x[1]
pylab.plot([list_x[0] + list_x[1]], [newtone_polynome(x, 10)],
           marker='o', markersize=7, color="red")
show_polynome(newtone_polynome, "Многочлен Ньютона при n = 10", 10, False)

print("L10(x1 + x2) = ", newtone_polynome(x, 10))

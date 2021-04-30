import sympy
import numpy
import matplotlib.pyplot as plt
from matplotlib import pylab
list_x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
f = {list_x[0]: 4, list_x[1]: 4.41, list_x[2]: 4.79,
     list_x[3]: 5.13, list_x[4]: 5.46, list_x[5]: 5.76,
     list_x[6]: 7.04, list_x[7]: 7.3, list_x[8]: 7.55,
     list_x[9]: 7.79, list_x[10]: 8.01}

counter = 0 

def basis_polynome(x, i, n):
    p = 1
    for k in range(n):
        if k != i:
            p *= (x - list_x[k])/(list_x[i] - list_x[k])
    return p


def lagrange_polynome(x, n):
    lagrange = 0
    for i in range(n):
        lagrange += basis_polynome(x, i, n)*f[list_x[i]]
    return sympy.expand(lagrange)


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

    pylab.legend()
    global counter
    counter +=1 
    pylab.savefig(f"{counter}.png")


n = 11
x = sympy.Symbol('x')
print("Многочлен Лагранжа:\n", lagrange_polynome(x, n))

show_polynome(lagrange_polynome, "Многочлен Лагранжа", n, True)

x = list_x[0] + list_x[1]
pylab.plot([list_x[0] + list_x[1]], [lagrange_polynome(x, 10)],
           marker='o', markersize=7, color="red")
show_polynome(lagrange_polynome, "Многочлен Лагранжа при n = 10", 10, False)

print("L10(x1 + x2) = ", lagrange_polynome(x, 10))





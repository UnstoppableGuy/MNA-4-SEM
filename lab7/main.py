import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate


def make_x(a, b, kol):
    x = list(range(kol))
    h = (b-a)/(kol-1)
    for i in range(kol):
        x[i] = a+i*h
    return x


if __name__ == '__main__':
    a = 1
    b = 3
    yzl = 6
    value = 0.5*(b-a)
    x = np.array(make_x(a, b, yzl))
    y = np.log(x)
    tck = interpolate.splrep(x, y, s=0)

    print(f'Значение в точке 0.5*(b-a)={value} (через сплайн):',
          interpolate.splev((b-a)/2, tck, der=0).round(6))
    print(f'Значение в точке 0.5*(b-a)={value} (через непосредственно функцию):',
          np.log((b-a)/2).round(6))
    print('\nЗначение в точке 2 (через сплайн):',
          interpolate.splev(2, tck, der=0).round(6))
    print('Значение в точке 2 (через непосредственно функцию):', np.log(2).round(6))

    xnew = np.arange(1, 3, 1/20)
    ynew = interpolate.splev(xnew, tck, der=0)
    plt.figure()
    plt.plot(x, y, 'x', xnew, ynew, linewidth=3)
    plt.plot(xnew, np.log(xnew), linewidth=1, color='b')
    plt.legend(['Узлы', 'Кубический сплайн', 'Логарифм'])
    plt.title('Интерполяция кубическими сплайнами')
    plt.savefig("plot.png")

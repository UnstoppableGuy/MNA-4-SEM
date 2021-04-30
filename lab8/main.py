import numpy as np
import sympy as sp


def func(x):
    return np.arctan(x)   


def test1_func(x):
    return np.arctan(np.sqrt(x))


def test2_func(x):
    return np.sqrt(x)


def numerical_differentiation(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)


def numerical_differentiation_2(f, x, h):
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h ** 2)


def numerical_integration_rectangle(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    s = 0

    for i in range(1, len(x) + 1):
        s += f(x[i - 1] + h / 2)

    return h * s


def numerical_integration_trapeze(f, a, b, n):
    h = (b - a) / n
    s = h * (f(a) + f(b)) / 2

    for i in range(1, n):
        s += h * f(a + i * h)

    return s


def numerical_integration_simpson(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    s = 0
    for i in range(0, int(n / 2)):
        s += f(x[2 * i + 2]) + 4 * f(x[2 * i + 1]) + f(x[2 * i])

    return (h / 3) * s


def print_diff_res(f, sp_f, x0, h):
    x = sp.Symbol('x')
    print(f"1-я производная в {x0}: {numerical_differentiation(f, x0, h)}\n"
          f"2-я производная в {x0}: {numerical_differentiation_2(f, x0, h)}\n"
          f"Проверка встроенным методом:\n1-я производная в {x0}: {sp_f.diff(x).subs(x, x0)}\n"
          f"2-я производная в {x0}: {sp_f.diff(x).diff(x).subs(x, x0)}")


def print_int_res(f, a, b, n):
    print(f"Метод прямоугольников: {numerical_integration_rectangle(f, a, b, n)}\n"
          f"Метод трапеций: {numerical_integration_trapeze(f, a, b, n)}\n"
          f"Метод Симпсона: {numerical_integration_simpson(f, a, b, n)}")


x = sp.Symbol('x')
print("Задание:")
print_diff_res(func, sp.atan(x), 1, 0.1)
print_int_res(func, 0, 2.0, 10000)

print("\nТест 1:")
print_diff_res(test1_func, sp.atan(sp.sqrt(x)), 1.0, 0.1)
print_int_res(test1_func, 0, 2.0, 10000)

print("\nТест 2:")
print_diff_res(test2_func, sp.sqrt(x), 2.0, 0.1)
print_int_res(test2_func, 0, 4.0, 10000)


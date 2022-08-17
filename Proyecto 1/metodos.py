import math
from sympy import *
import numpy as np


def secante(f, xn, xn1, tol, x):
    n = 0
    fn = f.subs(x, xn).evalf()
    fn1 = f.subs(x, xn1).evalf()
    if abs(fn) < tol:
        return [n, xn]
    else:
        while abs(fn1) >= tol:
            n = n + 1
            xn2 = xn1 - (fn1 * (xn1 - xn)) / (fn1 - fn)
            xn = xn1
            xn1 = xn2
            fn = fn1
            fn1 = f.subs(x, xn1).evalf()
        return [n, xn1]


def punto_fijo(f, xn, tol, x):
    n = 0
    fx = f.subs(x, xn).evalf()

    if abs(fx) < tol:
        return [n, xn]
    else:
        while abs(fx - xn) >= tol and n < 10 ** 3:
            n = n + 1
            xn = fx
            fx = f.subs(x, fx).evalf()
        return [n, xn]


def biyeccion(f, a, b, tol, x):
    fa = f.subs(x, a).evalf()
    fb = f.subs(x, b).evalf()
    n = 0
    c = (a + b) / 2
    fc = f.subs(x, c).evalf()
    if fa * fb > 0:
        print("debe ingresar 2 elementos que se mapeen en distintos signos")
        return [-1, 0]
    elif abs(fa) < tol:
        return [n, a]
    elif abs(fb) < tol:
        return [n, b]
    else:
        while abs(fc) >= tol:
            n = n + 1
            c = (a + b) / 2
            fc = f.subs(x, c).evalf()
            if fc == 0:
                print(str(c) + " es una raiz")
            elif fa * fc > 0:
                a = c
                fa = fc
            else:
                b = c
                fb = fc
        return [n, c]


def Newton(f, tol, xn, x):
    n = 0
    fx = f.subs(x, xn).evalf()
    if abs(fx) < tol:
        return [n, xn]
    else:
        while abs(fx) >= tol:
            df = diff(f, x).subs(x, xn).evalf()
            xn = xn - fx / df
            fx = f.subs(x, xn).evalf()
            n = n + 1
        return [n, xn]


def imprimir(f, tol, s1, s2, p, b1, b2, n, x, root):
    print("Función: ", f, "\nTolerancia: ", tol)
    xn = s1
    xn1 = s2
    res = secante(f, xn, xn1, tol, x)
    T = [['secante', "x_0=" + str(xn) + ", x_1=" + str(xn1), res[0], res[1], f.subs(x, res[1]).evalf(),
          1 - (res[1]) / root]]
    xn = p
    res = punto_fijo(f + x, xn, tol, x)
    if res[0] == 10 ** 3:
        T.append(['punto fijo', "x=" + str(xn), "diverge", "-", "-", "-"])
    else:
        T.append(
            ['punto fijo', "x=" + str(xn), res[0], res[1], str(f.subs(x, res[1]).evalf()), str(1 - (res[1]) / (root))])
    xn = b1
    xn1 = b2
    res = biyeccion(f, xn, xn1, tol, x)
    if res[0] > -1:
        T.append(['bisección', "x_0=" + str(xn) + ", x_1=" + str(xn1), res[0], res[1], str(f.subs(x, res[1]).evalf()),
                  str(1 - (res[1]) / (root))])
    else:
        T.append(['bisección', "x_0=" + str(xn) + ", x_1=" + str(xn1), "inconcluso", "-", "-", "-"])
    xn = n
    res = Newton(f, tol, xn, x)
    # T.append(['Newton',"x="+str(xn),res[0],res[1],f.subs(x, res[1]).evalf(),0])
    T.append(['Newton', "x=" + str(xn), res[0], res[1], str(f.subs(x, res[1]).evalf()), str(1 - (res[1]) / (root))])

    L = "{:<10} {:<18} {:<15} {:<20} {:<22} {:<15} "
    print(L.format('metodo', 'entrada/s', 'repeticiones', 'raiz', 'resultado', 'error'))

    for v in T:
        name, entradas, age, cosa, resultado, error = v
        print(L.format(name, entradas, age, cosa, resultado, error))
    print("")

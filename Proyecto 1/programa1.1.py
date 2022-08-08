import math
from sympy import *
import numpy as np


def secante(f, xn, xn1, tol):
    n = 0
    fn = f.subs(x, xn).evalf()
    fn1 = f.subs(x, xn1).evalf()
    if abs(fn) < tol:
        return [n, xn]
    else:
        while abs(fn1) >= tol:
            n = n + 1
            xn2 = xn1 - ((fn1) * (xn1 - xn)) / (fn1 - fn)
            xn = xn1
            xn1 = xn2
            fn = fn1
            fn1 = f.subs(x, xn1).evalf()
        return [n, xn1]


def punto_fijo(f, xn, tol):
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


def biyeccion(f, a, b, tol):
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


def Newton(f, tol, xn):
    n = 0
    fx = f.subs(x, xn).evalf()
    if abs(fx) < tol:
        return [n, xn]
    else:
        while abs(fx) >= tol:
            df = diff(f, x).subs(x, xn).evalf()
            xn = xn - (fx) / (df)
            fx = f.subs(x, xn).evalf()
            n = n + 1
        return [n, xn]


# funciones preprogramadas (quitar el # a la que se quiera calcular)
x = Symbol('x')
# f= (x-1)*(x+2)
# f= exp(x)-2
# f= log(x+0.1)
# f= exp(x*x)-2
# f= cos(x)
f = 7 * exp(-x) * sin(x) - 1
# f= lambda x: x**3+3*x+9

# tolerancia (error deseado)
n = 10
tol = 10 ** (-n)
# parametros
xn = 0.1
xn1 = 0.3

# resultados
print("Función: ", f, "\nTolerancia: ", tol, "\nx_0: ", xn, "\nx_1: ", xn1)
print("Método: secante")
res = secante(f, xn, xn1, tol)
print("raíz: x=" + str(res[1]) + ",")
print("f(x)=" + str(f.subs(x, res[1]).evalf()) + ",")
print("cantidad de pasos: " + str(res[0]))
print("")
print("Método: punto fijo")
res = punto_fijo(f + x, xn, tol)
if res[0] == 10 ** 3:
    print("diverge")
else:
    print("raíz: x=" + str(res[1]) + ",")
    print("f(x)=" + str(f.subs(x, res[1]).evalf()) + ",")
    print("cantidad de pasos: " + str(res[0]))
print("")
print("Método: biyección")
res = biyeccion(f, xn, xn1, tol)
if res[0] > -1:
    print("raíz: x=" + str(res[1]) + ",")
    print("f(x)=" + str(f.subs(x, res[1]).evalf()) + ",")
    print("cantidad de pasos: " + str(res[0]))
print("")
print("Método: Newton")
res = Newton(f, tol, xn)
print("raíz: x=" + str(res[1]) + ",")
print("f(x)=" + str(f.subs(x, res[1]).evalf()) + ",")
print("cantidad de pasos: " + str(res[0]))

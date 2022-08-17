import metodos as m
import math
from sympy import *
import numpy as np

x = Symbol('x')

# tolerancia (error deseado)
n = 10
tol = 10 ** (-n)
# parametros
xn = 0.1
xn1 = 1.1

# resultados

f = (x - 1) * (x + 2)
m.imprimir(f, tol, xn, xn1, -1, xn, xn1, xn, x, 1)
f = (x - 1) * (x + 2)
m.imprimir(f, tol, -3, -1, 0, -2.5, -1, -3, x, -2)
f = x ** 3 + 3 * x + 9
m.imprimir(f, tol, xn, xn1, xn, xn, -2, xn, x, -1.609695494)
f = exp(x) - 2
m.imprimir(f, tol, xn, xn1, xn, xn, xn1, xn, x, 0.6931471806)
f = log(x + 0.1)
m.imprimir(f, tol, xn, xn1, xn, xn, xn1, xn, x, 0.9)
f = cos(x)
m.imprimir(f, tol, xn, xn1, xn, xn, 2, 1, x, 1.570796327)
f = 7 * exp(-x) * sin(x) - 1
m.imprimir(f, tol, xn, 2, xn, 1, 2, 2, x, 1.89305902942)

import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
from scipy import interpolate


### EJEMPLO ORIGINAL
# x = np . array ([1 ,4 ,8 ,13 ,18])
# y = np . array ([1 ,4 ,8 ,13 ,18])
# z = np . array ([1.1 ,1.5 ,12.8 ,15.3 ,15.5])
# n = x . size
# xi =3
# yi =3
# zi =0


# zi = 0  #### Este es el valor que hay que buscar, cuánto vale zi para xi y yi, luego
#### de construir el polinomio con los valores x,y,z


def Lagrange3D(x, y, z):
    #### METODO 3D ##############
    # Calcula los factores de Lagrange y hace la suma
    X = sym.Symbol('x')
    Y = sym.Symbol('y')
    n = len(x)
    result = 0
    for i in range(0, n):
        for j in range(0, n):
            producto = z[i]
            for k in range(0, n):
                if i != k and x[i] != x[k]:
                    producto = producto * (X - x[k]) / (x[i] - x[k])

                if j != k and y[k] != y[j]:
                    producto = producto * (Y - y[k]) / (y[j] - y[k])
            result += producto

    simple_polynomial = result
    return sym.lambdify((X, Y), simple_polynomial)


def Graph(x, y, z):
    muestras = 10
    min_interval_x = np.min(x)
    max_interval_x = np.max(x)
    points_interval_x = np.linspace(min_interval_x, max_interval_x,
                                    muestras)  # conjunto de puntos a evaluar en el polinomio

    min_interval_y = np.min(y)
    max_interval_y = np.max(y)
    points_interval_y = np.linspace(min_interval_y, max_interval_y, muestras)

    poly = Lagrange3D(x, y, z)
    zi = poly(points_interval_x, points_interval_y)

    fig = plt.figure(figsize=(4, 4))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(points_interval_x, points_interval_y, zi)  # plteao el valor que fue interpolado (un pto)
    ax.plot(x, y, z)  # plotea los valores con los que se construye el polinomio
    plt.show()

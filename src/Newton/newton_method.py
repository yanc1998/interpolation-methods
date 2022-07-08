import numpy as np
import sympy as sym
import matplotlib.pyplot as plt


def newton_method(points_x, points_y):
    table = fill_table(points_x, points_y)  # crear la tabla
    polynomial = create_polinomio(table, len(points_x), points_y, points_x)  # crear el polinomio de interpolacion

    # Puntos para la gráfica
    muestras = 101
    min_interval = np.min(points_x)
    max_interval = np.max(points_x)
    points_interval = np.linspace(min_interval, max_interval, muestras)  # conjunto de puntos a evaluar en el polinomio
    evaluate_points = polynomial(points_interval)  # evaluacion de los puntos en el polinomio

    # Gráfica
    plt.plot(points_x, points_y, 'o', label='Puntos')

    plt.plot(points_interval, evaluate_points, label='Polinomio')
    plt.legend()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Diferencias Divididas - Newton')
    plt.show()


def create_polinomio(tabla, n, points_y, points_x):
    diference_divid = tabla[0, 3:]

    x = sym.Symbol('x')
    polynomial = points_y[0]
    for j in range(1, n, 1):
        factor = diference_divid[j - 1]
        term = 1
        for k in range(0, j):
            term = term * (x - points_x[k])
        polynomial = polynomial + term * factor

    simple_polynomial = polynomial.expand()

    numerical_polynomial = sym.lambdify(x, simple_polynomial)
    return numerical_polynomial


def fill_table(points_x, points_y):
    n = len(points_x)  # cantidad de puntos a interpolar

    # definir la tabla
    ki = np.arange(0, n, 1)
    table = np.concatenate(([ki], [points_x], [points_y]), axis=0)
    table = np.transpose(table)

    dfinite = np.zeros(shape=(n, n), dtype=float)
    table = np.concatenate((table, dfinite), axis=1)

    # Calcul la tabla
    [n, m] = np.shape(table)
    diagonal = n - 1
    for j in range(3, m):
        step = j - 2
        for i in range(diagonal):
            denominator = (points_x[i + step] - points_x[i])
            numerator = table[i + 1, j - 1] - table[i, j - 1]
            table[i, j] = numerator / denominator
        diagonal = diagonal - 1

    return table


xi = np.array([2.2, 5.8, 4.2, 4.5])
fi = np.array([4.12, 8.42, 7.25, 7.85])

newton_method(xi, fi)

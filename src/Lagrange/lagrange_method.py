import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


def lagrange_method_3d(x, y, z):
    X = sym.Symbol('x')
    Y = sym.Symbol('y')
    result = 0
    for i in range(len(x)):
        a = z[i]
        for j in range(len(x)):
            a *= Lij(i, j, x, y, X, Y)
        result += a

    simple_polynomial = result
    return sym.lambdify((X, Y), simple_polynomial)


def Lij(i, j, x, y, var_x, var_y):
    return L(i, x, var_x) * L(j, y, var_y)


def L(i, values, var):
    result = 1
    for s, value in enumerate(values):
        if i != s and values[i] != value:
            result *= (var - value) / (values[i] - value)
    return result

#
# x = np.array([22.9825, 23.0093, 23.0361, 23.063])
# y = np.array([-82.4814, -82.4522, -82.423, -82.3939])
# z = np.array([25.3455, 26.177, 28.5567, 28.1907])
# p = lagrange_method_3d(x, y, z)

# Puntos para la gráfica
# muestras = 101
# min_interval_x = np.min(x)
# max_interval_x = np.max(x)
# points_interval_x = np.linspace(min_interval_x, max_interval_x,
#                                 muestras)  # conjunto de puntos a evaluar en el polinomio
#
# min_interval_y = np.min(y)
# max_interval_y = np.max(y)
# points_interval_y = np.linspace(min_interval_y, max_interval_y, muestras)
# xi = 23.0361
# yi = -82.3939
# evaluate_points = p(x[0], y[0])  # evaluacion de los puntos en el polinomio
#
# print(evaluate_points)

# # Gráfica
# axes = plt.axes(projection='3d')
# axes.scatter3D(x, y, z)
# axes.plot3D(points_interval_x, points_interval_y, evaluate_points)
# axes.set_title('aa')
# axes.set_xlabel('x')
# axes.set_ylabel('y')
# axes.set_zlabel('z')
# plt.show()

# fig = plt.figure(figsize=(4, 4))
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter3D(points_interval_x, points_interval_y, evaluate_points)  # plteao el valor que fue interpolado (un pto)
# ax.plot3D(x, y, z, 'o', label='Puntos')  # plotea los valores con los que se construye el polinomio
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('z')
# plt.show()

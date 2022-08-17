import math
import os
from netCDF4 import Dataset as ncdf
from Lagrange import Graph
import numpy as np
from Lagrange import Lagrange3D


def getInterval(points_x, points_y, value, x, y, e, count):
    close_points_x = []
    close_points_y = []
    close_value = []
    j = 0
    for i in range(min(len(points_x), len(points_y))):
        d = math.sqrt((points_x[i] - x) ** 2 + (points_y[i] - y) ** 2)
        if d < e:
            j += 1
            close_points_x.append(points_x[i])
            close_points_y.append(points_y[i])
            close_value.append(value[i])
        if j >= count:
            break

    return close_points_x, close_points_y, close_value


def main():
    # x = [1, 3, 4]
    # y = [2, 3, 5]
    # z = [4, 7, 8]
    # p = lagrange_method_3d(x, y, z)
    load_data()


def load_data():
    dir = './data/sispi'
    list_file = os.listdir(dir)
    cord_names = ['casa blanca 325', 'florida 350']
    cord_est = [(-82.6167, 22.8667), (-78.23, 21.51)]
    for file in list_file:
        if file.startswith('wrfout_d03_'):
            for i, cord_e in enumerate(cord_est):
                ncFile = ncdf(dir + '/' + file)

                _long = ncFile.variables['XLONG'][:]  # Coordenadas
                _lat = ncFile.variables['XLAT'][:]
                long = np.reshape(_long, 75213)
                lat = np.reshape(_lat, 75213)

                WIN = ncFile.variables['W'][:]  # Variable viento
                win = np.reshape(WIN, 2105964)
                # Temperatura en superficie
                tempK = ncFile.variables['T2'][:]
                _tempC = tempK - 273.15
                tempC = np.reshape(_tempC, 75213)
                close_x, close_y, temp = getInterval(long, lat, tempC, cord_e[0], cord_e[1], 0.2, 4)
                close_xw, close_yw, wind = getInterval(long, lat, win, cord_e[0], cord_e[1], 0.2, 4)
                polyT = Lagrange3D(close_x, close_y, temp)
                polyW = Lagrange3D(close_xw, close_yw, wind)

                print(f'archivo{file}')
                print(f'temperatura interpolada en cordenada {cord_e} estacion {cord_names[i]}')
                print(polyT(cord_e[0], cord_e[1]))
                print(f'viento interpoalado en cordenadas {cord_e} estacion {cord_names[i]}')
                print(polyW(cord_e[0], cord_e[1]))
                Graph(close_x, close_y, temp)
                Graph(close_xw, close_yw, wind)


if __name__ == '__main__':
    main()

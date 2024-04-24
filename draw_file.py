import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def draw_hist(arr1: list[float], arr2: list[float], arr3: list[float], name):

    plt.subplot(1, 3, 1)
    plt.hist(arr1, bins=20, edgecolor='black')
    plt.xlabel('Значение')
    plt.ylabel('Частота')

    plt.subplot(1, 3, 2)
    plt.hist(arr2, bins=20, edgecolor='black')
    plt.title(name)
    plt.xlabel('Значение')
    plt.ylabel('Частота')

    plt.subplot(1, 3, 3)
    plt.hist(arr3, bins=20, edgecolor='black')
    plt.xlabel('Значение')
    plt.ylabel('Частота')

    plt.subplots_adjust(wspace=0.7, hspace=0.3)
    plt.show()


def draw_ecdf(arr1, arr2, arr3, name):
    ecdf_arr1 = stats.ecdf(arr1)
    ecdf_arr2 = stats.ecdf(arr2)
    ecdf_arr3 = stats.ecdf(arr3)
    ax = plt.subplot()
    ecdf_arr1.cdf.plot(ax, label="N=1000")
    ecdf_arr2.cdf.plot(ax, label="N=5000")
    ecdf_arr3.cdf.plot(ax, label="N=10000")
    ax.legend()
    ax.set_xlabel('Значение')
    ax.set_ylabel('ЭФР')
    plt.title(name)
    plt.show()

def draw_graphic_test(arr1, arr2, arr3, name):
    plt.subplot(1, 3, 1)
    plt.scatter(arr1[::2], arr1[1::2])
    plt.xlabel('Четные элементы')
    plt.ylabel('Нечетные элементы')

    plt.subplot(1, 3, 2)
    plt.scatter(arr2[::2], arr2[1::2])
    plt.xlabel('Четные элементы')
    plt.ylabel('Нечетные элементы')
    plt.title(name)

    plt.subplot(1, 3, 3)
    plt.scatter(arr3[::2], arr3[1::2])
    plt.xlabel('Четные элементы')
    plt.ylabel('Нечетные элементы')

    plt.show()



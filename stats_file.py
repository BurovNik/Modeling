import numpy as np
import matplotlib.pyplot as plt

def show_stat(arr1, arr2, arr3, name):
    print("-----------------------------------------")
    print(name.upper())
    print("-----------------------------------------")
    print(f"N = {len(arr1)}")
    print(f"Математическое ожидание: {np.mean(arr1)}")
    print(f"Дисперсия: {np.var(arr1)}")
    print(f"Среднее квадратичное отклонение: {np.std(arr1)} ")

    print("-----------------------------------------")
    print(f"N = {len(arr2)}")
    print(f"Математическое ожидание: {np.mean(arr2)}")
    print(f"Дисперсия: {np.var(arr2)}")
    print(f"Среднее квадратичное отклонение: {np.std(arr2)} ")

    print("-----------------------------------------")
    print(f"N = {len(arr3)}")
    print(f"Математическое ожидание: {np.mean(arr3)}")
    print(f"Дисперсия: {np.var(arr3)}")
    print(f"Среднее квадратичное отклонение: {np.std(arr3)} ")
    print("-----------------------------------------")

def uniform_distribution_stats(a, b):
    mean = (a+b)/2
    variance = (b-a)**2/12
    std = (b-a)/(2 * np.sqrt(3))

    print("-----------------------------------------")
    print(f"Для Равномерного распределения с границами ({a}, {b})")
    print(f"Математическое ожидание: {mean}")
    print(f"Дисперсия: {variance}")
    print(f"Среднее квадратичное отклонение: {std} ")
    print("-----------------------------------------")

    x = np.linspace(a, b, 1000)
    pdf = np.ones_like(x) / (b - a)
    cdf = (x - a) / (b - a)

    plt.figure(figsize=(15, 10))
    plt.subplot(1, 2, 1)
    plt.plot(x, pdf)
    plt.title("Плотность распределения")
    plt.xlabel("x")
    plt.ylabel("f(x)")

    plt.subplot(1, 2, 2)
    plt.plot(x, cdf)
    plt.title("Функция распределения F(X)")
    plt.xlabel("x")
    plt.ylabel("F(X)")
    plt.show()

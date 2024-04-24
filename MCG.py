def multiplicative_congruential_generator(n):
    # задаем константы
    a = 7 ** 5
    c = 0
    p = 53
    m = 2 ** 32 - 1
    Rn = 2 ** ((-1) * p)
    numbers = [Rn]  # результирующий массив чисел
    for i in range(n - 1):
        numbers.append(((a * numbers[-1] + c) % m) % 1)
    return numbers

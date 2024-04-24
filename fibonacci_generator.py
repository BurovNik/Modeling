from MCG import multiplicative_congruential_generator

def fibonacci_generator(n):
    a = 63
    b = 31
    numbers = multiplicative_congruential_generator(max(a, b))
    for i in range(max(a, b)+1, n - 1):
        if numbers[i - a] >= numbers[i - b]:
            numbers.append(numbers[i - a]-numbers[i - b])
        else:
            numbers.append(numbers[i - a]-numbers[i - b] + 1)
    return numbers
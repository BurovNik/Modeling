from MCG import multiplicative_congruential_generator
from fibonacci_generator import fibonacci_generator
from Mersen import Mersen_generator
from draw_file import draw_hist, draw_ecdf, draw_graphic_test
from stats_file import show_stat, uniform_distribution_stats

mcg1 = multiplicative_congruential_generator(1000)
mcg2 = multiplicative_congruential_generator(5000)
mcg3 = multiplicative_congruential_generator(10000)

# draw_hist(mcg1, mcg2, mcg3, "Мультипликативный конгруэнтный генератор")
# draw_ecdf(mcg1, mcg2, mcg3, "Мультипликативный конгруэнтный генератор")
# draw_graphic_test(mcg1, mcg2, mcg3, "Мультипликативный конгруэнтный генератор")
# show_stat(mcg1, mcg2, mcg3, "Мультипликативный конгруэнтный генератор")

fib1 = fibonacci_generator(1000)
fib2 = fibonacci_generator(5000)
fib3 = fibonacci_generator(10000)

# draw_hist(fib1, fib2, fib3, "Генератор Фибоначчи")
# draw_ecdf(fib1, fib2, fib3, "Генератор Фибоначчи")
# draw_graphic_test(fib1, fib2, fib3, "Генератор Фибоначчи")
show_stat(fib1, fib2, fib3, "Генератор Фибоначчи")

merc1 = Mersen_generator(1000)
merc2 = Mersen_generator(5000)
merc3 = Mersen_generator(10000)

# draw_hist(merc1, merc2, merc3, "Вихрь Мерсенна")
# draw_ecdf(merc1, merc2, merc3, "Вихрь Мерсенна")
# draw_graphic_test(merc1, merc2, merc3, "Вихрь Мерсенна")
# show_stat(merc1, merc2, merc3, "Вихрь Мерсенна")

uniform_distribution_stats(0, 1)








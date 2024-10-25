# генерация списка из 10 случайных цифр и вывод их

import random

random_numbers = []

for i in range(10):
	random_numbers.append(random.randint(0, 10))

print(random_numbers)
import random

random_numbers = []

for i in range(10):
	random_numbers.append(random.randint(0, 10))

random_numbers.sort()
min_number = min(random_numbers)
max_number = max(random_numbers)

print(random_numbers)
print(f'Мин: {min_number}, Макс: {max_number}')

# посчитать числа в списке и вывод суммы через For

sum_numbers = 0

for number in random_numbers:
    sum_numbers += number

print(f'Сумма: {sum_numbers}')
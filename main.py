# создание файла и запись в него случайных чисел
import random

my_file = open("file.txt", "w+")

random_numbers = []

for i in range(10):
	my_file.write(f'{random.randint(0, 10)}')

my_file.close()



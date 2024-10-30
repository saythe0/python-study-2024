import random
import statistics

file = open("file.txt", "w+")

for i in range(10):
	file.write(f'{random.randint(0, 10)} ')


# прочитать и вывести среднее из записанных

file.seek(0)

numbers = []
for num in file.read().strip().split():
	numbers.append(int(num))
	
avg = statistics.mean(numbers)
print(numbers)
print(avg)
file.close()
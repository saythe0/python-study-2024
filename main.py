import random
import statistics
import tkinter
import tkinter.filedialog

# добавить выбор файла через проводник
file_path = tkinter.filedialog.askopenfilename(title="Выберите файл", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])


file = open(file_path, "w+")

for i in range(10):
	file.write(f'{random.randint(0, 10)} ')

file.seek(0)

numbers = []
for num in file.read().strip().split():
	numbers.append(int(num))
	
avg = statistics.mean(numbers)
print(numbers)
print(avg)
file.close()
# через tkinter программу и через кнопки сделать все программы которые были раньше

# numbers = [(что мы хотим записать) for (либо _ или переменная) in (откуда, типа массив)]
# numbers = [int(num) for num in file.read().strip().split()]

# краткая форма if, как в php, например: b != 0 ? a / b : 'Ошибка!'
# a / b if b != 0 else 'Ошибка! На ноль делить нельзя.'

import statistics
from tkinter import *
from tkinter import ttk
import tkinter.filedialog
import random

def mathFun():
	a = int(entry_a.get())
	b = int(entry_b.get())
	result_var.set(f"Сумма: {a + b}\n"
					f"Разность: {a - b}\n"
					f"Произведение: {a * b}\n"
					f"Среднее арифметическое: {(a + b) / 2}\n"
					f"Среднее геометрическое: {(a * b) ** 0.5 if a * b >= 0 else 'Не определено'}\n"
					f"Максимальное число: {max(a, b)}\n"
					f"Минимальное число: {min(a, b)}\n"
					f"Деление: {a / b if b != 0 else 'Ошибка! На ноль делить нельзя.'}\n"
					f"Остаток: {a % b if b != 0 else 'Ошибка! На ноль делить нельзя.'}")
	
def randomFun():
	random_numbers = [random.randint(0, 10) for _ in range(10)]
	random_numbers.sort()
	result_var.set(f"Массив: {random_numbers}\n"
					f"Сумма чисел: {sum(random_numbers)}\n"
					f"Минимальное: {max(random_numbers)}\n"
					f"Максимальное: {min(random_numbers)}")
	
class Dog:
	def __init__(self, name):
		self.name = name
	
	def hello_dog(self):
		return f'Привет пёс по кличке {self.name}\n'

class Cat(Dog):
	def hello_cat(self):
		return f'Привет котяра по кличке {self.name}\n'

def classFun():
	cat = Cat('Владислав Фролов')
	line = cat.hello_dog() + cat.hello_cat()
	result_var.set(line)

def fileFun():
	file_path = tkinter.filedialog.askopenfilename(title="Выберите файл", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
	file = open(file_path, "w+")
	# принимает только строку типа
	file.write(' '.join(str(random.randint(0, 10)) for _ in range(10)))
	file.seek(0)
	numbers = [int(num) for num in file.read().strip().split()]
	file.close()
	result_var.set(f"Массив чисел из файла: {numbers}\n"
					f"Среднее арифметическое (вроде так) число: {statistics.mean(numbers)}")

root = Tk()
root.title("Лабораторная 6")
root.geometry("400x600")

label_a = ttk.Label(root, text="Введите первое число:")
label_a.pack(pady=5)
entry_a = ttk.Entry(root)
entry_a.pack(pady=5)

label_b = ttk.Label(root, text="Введите второе число:")
label_b.pack(pady=5)
entry_b = ttk.Entry(root)
entry_b.pack(pady=5)

button = ttk.Button(root, text="Выполнить мат. функции", command=mathFun)
button.pack(pady=10)

button = ttk.Button(root, text="Выполнить функция рандома", command=randomFun)
button.pack(pady=5)

button = ttk.Button(root, text="Вызвать класс и выполнит функции", command=classFun)
button.pack(pady=5)

button = ttk.Button(root, text="Вызвать функцию файла", command=fileFun)
button.pack(pady=5)

result_var = StringVar()
result_label = ttk.Label(root, textvariable=result_var, justify="left")
result_label.pack(pady=5)

root.mainloop()
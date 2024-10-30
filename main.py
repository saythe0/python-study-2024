class Dog:
	def __init__(self, name):
		self.name = name
	
	def hello(self):
		print(f'Привет пёс по кличке {self.name}')

class Cat(Dog):
	def hello_cat(self):
		print(f'Привет котяра по кличке {self.name}')


cat = Cat('Влад Фролов')
cat.hello()
cat.hello_cat()

# через tkinter программу и через кнопки сделать все программы которые были раньше
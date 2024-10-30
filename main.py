class Dog:
	def __init__(self, name):
		self.name = name
	
	def hello(self):
		print(f'Привет пёс по кличке {self.name}')

# создать второй класс и наследовать из первого

class Cat(Dog):
	def hello_cat(self):
		print(f'Привет котяра по кличке {self.name}')


cat = Cat('Влад Фролов')
cat.hello()
cat.hello_cat()

from pick import pick

class Calc:
	def __init__(self, name):
		self.name = name
		self.actions = [
			'Add',
			'Subtract'
		]

		option, index = pick(self.actions, f"Hello {self.name}, what would you like to do?")
		answer = None

		a = int(input('Enter your first number: '))
		b = int(input('Enter your second number: '))

		if index == 0:
			answer = self.add(a, b)

		if index == 1:
			answer = self.subtract(a, b)

		print (f'{self.name} your answer is {answer}')

	def add(self, a, b):
		return a + b

	def subtract(self, a, b):
		return a - b

calc = Calc('John')
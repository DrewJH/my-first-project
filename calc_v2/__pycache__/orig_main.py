from pick import pick

def welcome():
	username = input("Welcome to the calculator, what shall I call you? ")
	return username

class Calc:
	def __init__(self, name):
		self.name = name
		self.actions = [
			'Add',
			'Subtract',
			'Multiply',
			'Divide',
			'Modulus',
			'Exponent',
			'Floor Division'
		]

		option, index = pick(self.actions, f"Hello {self.name}, what would you like to do?")
		answer = None

		a = int(input('Enter your first number: '))
		b = int(input('Enter your second number: '))

		if index == 0:
			answer = self.add(a, b)

		if index == 1:
			answer = self.subtract(a, b)

		if index == 2:
			answer = self.multiply(a, b)

		if index == 3:
			answer = self.divide(a, b)

		if index == 4:
			answer = self.modulus(a, b)

		if index == 5:
			answer = self.exponent(a, b)

		if index == 6:
			answer = self.floor_division(a, b)

		print (f'{self.name}, your answer is {answer}')
		self.more_calc()

	def add(self, a, b):
		return a + b

	def subtract(self, a, b):
		return a - b

	def multiply(self, a, b):
		return a * b

	def divide(self, a, b):
		return a / b

	def modulus(self, a, b):
		return a % b

	def exponent(self, a, b):
		return a ** b

	def floor_division(self, a ,b):
		return a // b
	
	def more_calc(self):
		self.more_calc = input(f"Is there another calculation you need {self.name}?\nEnter Y for YES\nEnter N for NO\n")

		if self.more_calc.upper() == "Y":
			Calc(self.name)

		elif self.more_calc.upper() == "N":
			print("It's been real.")

		else:
			pass

calc = Calc(welcome())

#MyFlag = True
#while MyFlag is True:
    #calc = Calc(welcome())
    #option, index = pick(['Yes', 'No'], 'Do another calc?')
    #if index == 1:
        #MyFlag = False
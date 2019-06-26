from pick import pick

class Calc:
	def __init__(self):
		self.name = None
		self.option = None
		self.index = None
		self.a = None
		self.b = None
		self.answer = None
		self.answers = []
		self.action_titles = [
			'Add',
			'Subtract'
		]

	def welcome(self):
		self.name = input("Welcome to the calculator, what shall I call you? ")
		return 

	def init(self):
		self.select_action()
		self.input_numbers()
		self.perform_action()
		self.add_answers()
		self.answer_message()
		self.ask_repeat()
		return 

	def select_action(self):
		self.option, self.index = pick(self.action_titles, f"Hello {self.name}, what would you like to do?")
		return 

	def input_numbers(self):
		self.a = int(input('Enter your first number: '))
		self.b = int(input('Enter your second number: '))
		return 

	def perform_action(self):
		if self.index == 0:
			self.add()

		if self.index == 1:
			self.subtract()

	def add_answers(self):
		self.answers.append(
			{
				'operation':self.option,
				'num_a':self.a,
				'num_b':self.b,
				'answer':self.answer
			}
		)
		return 

	def answer_message(self):
		print (f'{self.name}, your answer is {self.answer}')
		print (self.answers)
		return 

	def ask_repeat(self):
		user_input = input(f"Is there another calculation you need {self.name}?\nEnter Y for YES\nEnter N for NO\n")

		if user_input.upper() == "Y":
			self.init()
		elif user_input.upper() == "N":
			self.repeat = False

	def add(self):
		self.answer = self.a + self.b
		return 

	def subtract(self):
		self.answer = self.a - self.b
		return 
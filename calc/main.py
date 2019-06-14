def welcome():
	print("Welcome to my calculator.  Select operation:")
	print("1. Add")
	print("2. Subtract")
	print("3. Multiply")
	print("4. Divide")
	print("5. Modulusify!")
	print("6. Exponent")
	print("7. Floor Divide")

def calculate():
	def addition(x, y):
		return x + y

	def subtraction(x, y):
		return x - y

	def multiplication(x, y):
		return x * y

	def division(x, y):
		return x / y

	def modulus(x, y):
		return x % y

	def exponent(x, y):
		return x ** y

	def floor_division(x, y):
		return x // y

	operation = input("Enter operation (1 - 7): ")

	number_x = int(input("Enter first number: "))
	number_y = int(input("Enter second number: "))

	if operation == "1":
		print(f"{number_x} + {number_y} = {addition(number_x, number_y)}")

	elif operation == "2":
		print(f"{number_x} - {number_y} = {subtraction(number_x, number_y)}")

	elif operation == "3":
		print(f"{number_x} * {number_y} = {multiplication(number_x, number_y)}")

	elif operation == "4":
		print(f"{number_x} / {number_y} = {division(number_x, number_y)}")

	elif operation == "5":
		print(f"{number_x} % {number_y} = {modulus(number_x, number_y)}")

	elif operation == "6":
		print(f"{number_x} ** {number_y} = {exponent(number_x, number_y)}")

	elif operation == "7":
		print(f"{number_x} // {number_y} = {floor_division(number_x, number_y)}")

	else:
		print("Are you for real?")

	more()

def more():
	more_calc = input("Are you a bad enough dude to calculate some more?\nPress Y for YUP\nPress N for NAH\n")

	if more_calc.upper() == "Y":
		calculate()

	elif more_calc.upper() == "N":
		print("Later nerd.")

	else:
		more()

welcome()
calculate()
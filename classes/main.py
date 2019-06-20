import random

class Cars:
	def __init__(self, make):
		self.make = make

	def __del__(self):
		print ('hello')

	

	def color(self):
		colors = [
			'red',
			'yellow',
			'black'
		]

		return random.choice(colors)


	def return_data(self):
		return {
			'color':self.color()
		}



ford = Cars('Ford')
data = ford.return_data()
print (data)
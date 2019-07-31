"""
drinks
---
0 - brew
1 - espresso
2 - handcrafted
"""

#api means application programming interface you twit
from pick import pick
import menu

SIZES = [
	{
		'id':0,
		'name':'Tall'
	},
	{
		'id':1,
		'name':'Grande'
	},
	{
		'id':2,
		'name':'Venti'
	}
]

SHOTS = [
	{
		'id':0,
		'name':'Single'
	},
	{
		'id':1,
		'name':'Double'
	},
	{
		'id':2,
		'name':'Triple'
	},
	{
		'id':3,
		'name':'Quad'
	}
]

PRICES = {
	0:{
		0:1.85,
		1:2.10,
		2:2.45
	},
	1:{
		0:1.75,
		1:1.95,
		2:2.25,
		3:2.65
	},
	2:{
		0:2.95,
		1:3.65,
		2:4.15
	}
}

DRINKS = [
	{
		'type':0,
		'name':'Dark Roast'
	},
	{
		'type':0,
		'name':'Blonde Roast'
	},
	{
		'type':1,
		'name':'Espresso'
	},
	{
		'type':2,
		'name':'Caffe Latte'
	},
	{
		'type':2,
		'name':'Cappuccino'
	}
]

class Drink:
	def __init__(self):
		self.name = None
		self.option = None
		self.option2 = None
		self.index = None
		self.index2 = None
		self.drink = None
		self.size = None
		self.price = None
		self.drinks = [
		"Dark Roast",
		"Blonde Roast",
		"Espresso",
		"Caffe Latte",
		"Cappuccino"
		]
		self.size_list = [
		"Tall",
		"Grande",
		"Venti"
		]
		self.shots = [
		"Single",
		"Double",
		"Triple",
		"Quad"
		]
		self.price_brew = [
			1.85,
			2.10,
			2.45
		]
		self.price_esp = [
			1.75,
			1.95,
			2.25,
			2.65
		]
		self.price_lc = [
			2.95,
			3.65,
			4.15
		]

	def welcome(self):
		self.name = input("Welcome to PythonBucks, please enter a name for your order: ")
		return

	def select_drink(self):
		self.option, self.index = pick(self.drinks, f"Alright {self.name}, what'll it be?")
		return

	def select_size(self):
		self.drink = self.drinks[self.index]
		if self.drink == "Espresso":
			self.option2, self.index2 = pick(self.shots, "Espresso?  Excellent choice.  How many shots would you like?")
		else:
			self.option2, self.index2 = pick(self.size_list, f"Okay, you'd like a {self.drink}.  What size would you like?")
		return

	def get_price(self):
		if self.drink == "Espresso":
			self.size = self.shots[self.index2]
			self.price = self.price_esp[self.index2]
		elif self.drink == "Dark Roast" or "Blonde Roast":
			self.size = self.size_list[self.index2]
			self.price = self.price_brew[self.index2]
		else:
			self.size = self.size_list[self.index2]
			self.price = self.price_lc[self.index2]
		print(f"{self.name}, your {self.size} {self.drink} will run you ${self.price}.")
		return

	def init(self):
		self.select_drink()
		self.select_size()
		self.get_price()
		return
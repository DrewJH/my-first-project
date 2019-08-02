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

DRINK_PICKER = [
"Dark Roast",
"Blonde Roast",
"Espresso",
"Caffe Latte",
"Cappuccino"
]

SHOT_PICKER = [
"Single",
"Double",
"Triple",
"Quad"
]

SIZE_PICKER = [
"Tall",
"Grande",
"Venti"
]

class Drink:
	def __init__(self):
		self.name = None
		self.drink_menu = None
		self.drink_selection = None
		self.drink = None
		self.type = None
		self.size_menu = None
		self.size_selection = None
		self.shot_selection = None
		self.size = None
		self.price = None

	def welcome(self):
		self.name = input("Welcome to PythonBucks, please enter a name for your order: ")
		return

	def select_drink(self):
		self.drink_menu, self.drink_selection = pick(DRINK_PICKER, f"Alright {self.name}, what'll it be?")
		return

	def select_size(self):
		self.drink = DRINKS[self.drink_selection]['name']
		self.type = DRINKS[self.drink_selection]['type']
		if self.drink == "Espresso":
			self.size_menu, self.size_selection = pick(SHOT_PICKER, "Espresso?  Excellent choice.  How many shots would you like?")
		else:
			self.size_menu, self.size_selection = pick(SIZE_PICKER, f"Okay, you'd like a {self.drink}.  What size would you like?")
		return

	def get_price(self):
		if self.drink == "Espresso":
			self.size = SHOTS[self.size_selection]['name']
			self.price = PRICES[self.type][self.size_selection]
		else:
			self.size = SIZES[self.size_selection]['name']
			self.price = PRICES[self.type][self.size_selection]
		print(f"{self.name}, your {self.size} {self.drink} will run you ${self.price}.")
		return

	def init(self):
		self.select_drink()
		self.select_size()
		self.get_price()
		return
"""
drinks
---
0 - brew
1 - espresso
2 - handcrafted
3 - special
"""

#api means application programming interface you twit
from pick import pick
import menu

FLAVORS = [
	{
		'name':"No Added Flavor",
		'price':0
	},
	{
		'name':"Vanilla",
		'price':.50
	},
	{
		'name':"Caramel",
		'price':.50
	},
	{
		'name':"Hazelnut",
		'price':.50
	},
	{
		'name':"Cinnamon",
		'price':.50
	}
]

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
	},
	3:{
		0:4.45,
		1:4.95,
		2:5.45
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
	},
	{
		'type':3,
		'name':'Chunky Monkey'
	}	
]

def list_generator(items, key):
	my_list = []
	for item in items:
		my_list.append(item[key])
	return my_list

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
		self.size_id = None
		self.flavor_menu = None
		self.flavor_selection = None
		self.flavor = None
		self.flavor_id = None
		self.flavor_price = 0
		self.price = 0
		self.order_list = []
		self.price_list = []
		self.option = None
		self.add_drinks = None

	def welcome(self):
		self.name = input("Welcome to PythonBucks, please enter a name for your order: ")
		return

	def select_drink(self):
		DRINK_PICKER = list_generator(DRINKS, 'name')
		self.drink_menu, self.drink_selection = pick(DRINK_PICKER, f"Alright {self.name}, what'll it be?")
		return

	def select_size(self):
		self.drink = DRINKS[self.drink_selection]['name']
		self.type = DRINKS[self.drink_selection]['type']
		if self.drink == "Espresso":
			SHOT_PICKER = list_generator(SHOTS, 'name')
			self.size_menu, self.size_selection = pick(SHOT_PICKER, "Espresso?  Excellent choice.  How many shots would you like?")
			self.size_id = SHOTS[self.size_selection]['id']
		else:
			SIZE_PICKER = list_generator(SIZES, 'name')
			self.size_menu, self.size_selection = pick(SIZE_PICKER, f"Okay, you'd like a {self.drink}.  What size would you like?")
			self.size_id = SIZES[self.size_selection]['id']
		return

	def select_flavor(self):
		if self.type == 2:
			FLAVOR_PICKER = list_generator(FLAVORS, 'name')
			self.flavor_menu, self.flavor_selection = pick(FLAVOR_PICKER, f"Would you like to add a flavor to your {self.drink}?")
			self.flavor = FLAVORS[self.flavor_selection]['name']
			self.flavor_price = FLAVORS[self.flavor_selection]['price']
		else:
			self.flavor = "No Added Flavor"
		return

	def get_price(self):
		if self.type == 1:
			self.size = SHOTS[self.size_id]['name']
			self.price = round(PRICES[self.type][self.size_id] * 1.075, 2) #sales tax
		else:
			self.size = SIZES[self.size_id]['name']
			self.price = self.flavor_price + PRICES[self.type][self.size_id]
			self.price = round(self.price * 1.075, 2)
		return

	def generate_order(self):
		self.price_list.append(self.price)
		if self.flavor == "No Added Flavor":
			self.drink = f"{self.size} {self.drink}"
		else:
			self.drink = f"{self.size} {self.flavor} {self.drink}"
		self.order_list.append(self.drink)
		return

	def more_drinks(self):
		y_n = ["Yes", "No"]
		self.option, self.add_drinks = pick(y_n, f"{self.name}, would you like another drink?")
		if self.add_drinks == 0:
			self.init()
		else:
			self.order_total()
		return

	def order_total(self):
		print(f"{self.name}, your {self.order_list} will run you ${self.price_list}.")
		return

	def init(self):
		self.select_drink()
		self.select_size()
		self.select_flavor()
		self.get_price()
		self.generate_order()
		self.more_drinks()
		return
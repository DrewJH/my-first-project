from pick import pick

def dict_to_list(items, key):
	my_list = []

	for item in items:
		my_list.append(item[key])

	return my_list

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


DRINK_OPTIONS = dict_to_list(DRINKS, 'name')
SIZE_OPTIONS = dict_to_list(SIZES, 'name')

option, index = pick(DRINK_OPTIONS, "Pick drink?")
current_drink = DRINKS[index]

print (current_drink)

current_drink_type = current_drink['type']

if current_drink['type'] == 1:
	pass
else:
	option, index = pick(SIZE_OPTIONS, "Pick size?")
	current_size = SIZES[index]

	print (current_size)

	current_size_id = current_size['id']
	current_price = PRICES[current_drink_type][current_size_id]
	print (current_price)
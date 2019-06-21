from pick import pick

MENU = [
	{
		'name':'Dark Roast',
		'sizes':[
			{
				'name':'Tall',
				'value':1.85
			},
			{
				'name':'Grande',
				'value':2.10
			},
			{
				'name':'Venti',
				'value':2.45
			}
		],
		'flavors':[
			{
				'name':'Hazlenut',
				'value':4.99
			}
		]
	},
	{
		'name':'Blonde Roast',
		'sizes':[
			{
				'name':'Tall',
				'value':1.85
			},
			{
				'name':'Grande',
				'value':2.10
			},
			{
				'name':'Venti',
				'value':2.45
			}
		],
		'flavors':[
			{
				'name':'Hazlenut',
				'value':4.99
			}
		]
	}
]

def welcome():
	print("""Thank you for choosing python Starbucks.  What'll it be?\n""")

def beverage():
	def data(index):
		menu_item = MENU[index]
		sizes = menu_item['sizes']

		title = f"{menu_item['name']}  You got it.  Select size:"
		options = []
		for s in menu_item['sizes']:
			options.append(s['name'])

		option, index = pick(options, title)
		value = sizes[index]['value']

		return value

	def ui():
		title = f'Select your beverage (1 - {len(MENU)})'
		options = []
		for menu_item in MENU:
			options.append(menu_item['name'])

		option, index = pick(options, title)

		value = data(index)

		return value

	return ui()

order_total = 0

welcome()
order_total += beverage()
print(order_total)
MENU = [
	{
		'name':'Dark Roast',
		'sizes':{
			'tall':1.85,
			'grande':2.10,
			'venti':2.45
		}
	}
]


dark_roast = {
"tall" : 1.85,
"grande" : 2.10,
"venti" : 2.45
}

blonde_roast = {
"tall" : 1.85,
"grande" : 2.10,
"venti" : 2.45
}

caffe_latte = {
"tall" : 2.95,
"grande" : 3.65,
"venti" : 4.15
}

cappuccino = {
"tall" : 2.95,
"grande" : 3.65,
"venti" : 4.15
}

def answer():
	selection2 = input(" ")
	selection2 = selection2.lower()
	if selection2 == "tall" or selection2 == "t":
			print(dark_roast["tall"])
			return dark_roast["tall"]

def welcome():
	print("""Thank you for choosing python Starbucks.  What'll it be?\n""")

def beverage():
	print ("""
		1. Dark Roast\n
		2. Pike's Place\n
		3. Blonde Roast\n
		4. Caffe Latte\n
		5. Cappuccino\n
	""")
	

Dark Roast?  You got it.  Select size (T/G/V):

selection = input("Select your beverage (1 - 5) ")

	if selection == "1":

		
	if selection == "2":
		print("Pike is hot garbage.  Pick something else.")
		order()

order_total = 0


welcome()
order_total += beverage()
print(order_total)
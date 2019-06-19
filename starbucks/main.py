def welcome():
	print("""Thank you for choosing python Starbucks.  What'll it be?\n
	1. Dark Roast\n
	2. Pike's Place\n
	3. Blonde Roast\n
	4. Caffe Latte\n
	5. Cappuccino\n""")

dark_roast = {
"tall" == 1.85,
"grande" == 2.10,
"venti" == 2.45
}

blonde_roast = {
"tall" == 1.85,
"grande" == 2.10,
"venti" == 2.45
}

caffe_latte = {
"tall" == 2.95,
"grande" == 3.65,
"venti" == 4.15
}

cappuccino = {
"tall" == 2.95,
"grande" == 3.65,
"venti" == 4.15
}

def order():
	selection = input("Select your beverage (1 - 5) ")

	if selection == "1":
		input("Dark Roast?  You got it.  Select size (T/G/V): ")
		if input() == lower("tall" or "t"):
			print(dark_roast, "tall")

		
	if selection == "2":
		print("Pike is hot garbage.  Pick something else.")
		order()


welcome()
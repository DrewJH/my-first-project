list1 = []
list1.append(7)
list1.append("cat")
list1.append(4)
list1.append("Ralph") #append is used to add items to a list
print(list1[1])
print(list1[0]) #you can also print things from specific indexes in a list
for x in list1:
	print(x) #you can use a loop to print the items in order
tuple1 = ("a","b","c","d") #tuples are lists that are unchangeable defined by parentheses instead of brackets
print(len(tuple1))
if "b" in tuple1:
	print("You are the code master.") #you can check for items in lists/tuples
bullshit = ["taxes", "politics", "extended warranties"]
cartridge = ["bullet", "case", "primer", "powder"]
propellent = "powder"
print(bullshit)
print("The chemical propellent in a cartridge is the %s" % propellent)
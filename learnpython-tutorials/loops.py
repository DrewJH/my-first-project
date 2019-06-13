letters = [
	'a',
	'b',
	'c',
	'd',
	'e',
	'f',
	'g',
	'h'
]
print("-EVEN-")
for index, letter in enumerate(letters):
	if index % 2 == 0:
		print(index, letter) #if the remainder of dividing the index by two is 0, it prints (resulting in even indexes)
for index, letter in enumerate(letters):
	if index % 2 == 1:
		continue
	print(index, letter) #same thing using a continue

print("-ODD-")
for index, letter in enumerate(letters):
	if index % 2 == 1:
		print(index, letter) #odd indexes here
for index, DREW in enumerate(letters):
	if index % 2 == 0:
		continue
	print(index, DREW) #just making sure that the thing that I am operating on can be called whatever I want

print("-BACKWARDS-")
for index, letter in enumerate(reversed(letters)):
	print(index, letter)

for letter in range(len(letters)):
	print(letters[letter]) #a way of printing a list using loops

print(*letters, sep = "\n") #a little simpler way of achieving the same thing that I totally looked up and stole
print(*letters, sep = "/") #this can also be used to separate by whatever string I want, but I digress

for index, letter in enumerate(letters):
	print(index, letter)
	if index >= 5: #don't indent this!
			break #stopping printing the list when it reaches a specific index

for index, letter in enumerate(letters):
	if index == 3:
		print("Desired index is %d" % (index))
	elif index == 7:
		print("%d is too high you psycho!" % (index))
	elif index == 0:
		print("%d is an insulting index." % (index))
	else:
		print("Index reached a value of %d" % (index))

#I wasn't able to figure out how to print a specific range of indexes from within my list e.g. if index == range(2, 4) doesn't do what I want it to do.

for index, letter in enumerate(letters):
	while index <= 4:
		index += 1
		print (index)
	else:
		break

random_number = 0.5
while True:
	print("Your floating number is now %.1f" % (random_number))
	random_number += 0.1
	if random_number >= 1.4:
		break
		

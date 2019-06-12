**number1 = 1 + 4 * 3
print(number1) #python follows order of operations
number2 = 17 // 2 #double division signs returns an integer without the remainder
print(number2)
number3 = 17 % 2 #this only returns the remainder
print(number3)
number4 = 3 ** 2 #double multiplication signs are used for exponents
print(number4)
quartz_frequency = 2 ** 15
print(quartz_frequency)
good_numbers = [1, 3, 5, 7]
bad_numbers = [2, 4, 6, 8]
okay_numbers = good_numbers + bad_numbers #operators can be used on lists
print(okay_numbers)
print(3 * good_numbers)
print(okay_numbers[:5]) #lists can be sliced - no value before the colon automatically starts the slice at 0
print(good_numbers[1:3])
print(bad_numbers[-3:]) #a negative value here starts the slice from the right and no value after the colon automatically ends the slice at the end of the list
a, b = 0, 1 #items can be defined in groups
while a < 20:
	print(a)
	a,b = b, a + b #Fibonacci's sequence - illustrating a more complex calculation
x = object()
y = object()
lotta_x = [x] * 5
lotta_y = [y] * 5
lotta_z = lotta_x + lotta_y
print("lotta_x has %d objects." % len(lotta_x))
print("lotta_y has %d objects." % len(lotta_y))
print("lotta_z has %d objects." % len(lotta_z))
if lotta_x.count(x) == 5 and lotta_y.count(y) == 5:
    print("You're pretty okay my guy.")
if lotta_z.count(x) == 5 and lotta_z.count(y) == 5:
    print("Now you've gone and done it.")
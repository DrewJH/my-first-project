myint = 3
print(myint)
myfloat = 3.3
print(myfloat) #python supports integers, floating point numbers, and complex numbers
mystring1 = "heavy"
print(mystring1)
mystring2 = 'metal'
print(mystring2)
mystring3 = 'mom\'s spaghetti' #backslashes can be used to escape quotes or define special characters
print(mystring3)
print(r'C:folder\notporn') #an r before quotes means raw string so special characters are not used in this case \n = new line
print("""The glories of our blood and state are shadows, not substantial things;
	There is no armor against fate;
	Death lays his icy hand on kings""") #triple quotes are used for strings spanning multiple lines
print(3 * "triple" + " " + "dogdareyou") #operators can be used on strings
x = "MyDude"
y = 5.17
z = 9
if x == "MyDude":
	print("Your-String-Is: %s" % x)
if isinstance(y, float) and y == 5.17:
	print("Your-Float-Is: %f" % y)
if isinstance(z, int) and z == 9:
	print("Your-Integer-Is: %d" % z)
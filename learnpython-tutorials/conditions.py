variable = 7
print(variable == 7)
print(variable == 4)
print(variable > 3)
print(variable <= 7)
revolver = "Colt Diamondback"
caliber = ".38 special"
if revolver == "Colt Diamondback" and caliber == ".38 special":
	print("Well are ya gonna pull those pistols or whistle Dixie?")
if revolver in ["S&W Model 10", "Colt Diamondback", "Ruger SP101"]:
	print("Yup.")
if caliber in ("9mm", ".357 Magnum", ".38 special"):
	print("Sure enough.") #you can check for variables in lists or tuples
if revolver is "Colt Diamondback":
	print("Hot.")
if revolver is "Ruger SP101":
	print("Hot.")
elif caliber is ".38 special":
	print("Super Hot.")
if revolver is "S&W Model 10":
	print("Hot.")
elif caliber is ".357 Magnum":
	print("Super Hot.")
else:
	print("The important thing is that you tried.")
handgun = "Colt Diamondback"
print("**STRING RESULTS**")
print(revolver == handgun)
print(revolver is handgun)
print("**LIST RESULTS**")
x = ['a', 'b', 'c']
y = ['a', 'b', 'c']
print(x == y)
print(x is y) #the website says, "the 'is' operator does not match the values of the variables, but the instances themselves" but I don't know why a string works and a list doesn't
a = (1, 2, 3)
b = (1, 2, 3)
print("**TUPLE RESULTS**")
print(a == b)
print(a is b) #but tuples work apparently ¯\ _(ツ)_/¯
if x is not y:
	print("Of course it isn't!")
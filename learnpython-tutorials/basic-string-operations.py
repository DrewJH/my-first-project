string = "That's pretty neat."
print(len(string))
print(string.index("a")) #this is used to find a specific index of a character, starting at 0 including spaces and special characters
print(string.count("t")) #counts the instances of a character, is case sensitive
print(string[3:14])
print(string[33:]) #an index out of range results in a blank, not an error
print(string[3:14:1]) #this is the syntax for slices [start:stop:step] not defining a step is automatically 1
print(string[3:14:2])
print(string[::-1]) #step values can be negative, and no start or stop defaults to the beginning and end of the string respectively
print(string.upper())
print(string.lower())
print(string.startswith("That's"))
print(string.endswith("neat."))
print(string.startswith("Marcus"))
print(string.split(" ")) #splits the string at the inidicated character and puts the pieces into a list
print(string.split("t")) #the character you indicate is omitted in the final list
print('I like' ' ' 'turtles.') #strings that are next to each other are automatically concatenated (my $20 word for the day)
statement = "I like"
print(statement + " " + "turtles.") #string literals are automatic, variables with string literals need operators
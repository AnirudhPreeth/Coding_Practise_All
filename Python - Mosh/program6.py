"""
Formatted Strings.
"""
#Formatted strings are useful when you want to dynamically generate some text with your variables.
first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder'
msg = f'{first} [{last}] is a coder'
#Formatted string is one which is prefix with an 'f'. 
#Curly braces - placeholders in our string. 
#Hole be filled with the value of our variables. 
print(message)
print(msg)
#Prefix your strings, with an f and use curly braces to dynammically insert values into your strings. 




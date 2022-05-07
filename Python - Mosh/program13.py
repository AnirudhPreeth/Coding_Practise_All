"""
Comparision Operators.
"""

"""
if temperature is greater than 30
   it's a hot day 
otherwise if it's less than 10
   it's a cold day
otherwise 
   it's neither hot nor cold

"""
temperature = 30
if temperature > 30:
    print("It's a hot day")
else:
    print("It's not hot day")

temperature = 35
if temperature > 30:
    print("It's a hot day")
else:
    print("It's not hot day")

temperature = 35
if temperature >= 30:
    print("It's a hot day")
else:
    print("It's not hot day")

temperature = 35
if temperature <= 30:
    print("It's a hot day")
else:
    print("It's not hot day")

temperature = 35
if temperature == 30:
    print("It's a hot day")
else:
    print("It's not hot day")

temperature = 35
if temperature != 30:
    print("It's a hot day")
else:
    print("It's not hot day")

#temperature > 30 -> Is a boolean expression. 
#= is not the same as ==. If we use one = sign, it's error. As it is an assignment statement. 
#We are changing the value of the temperature. We are setting the value of the tempurature variable..
#..to 30. We are not comparing it to something else. So we don't have a boolean expression. 
#We are not expressing a boolean value.

"""
Exercise: 

Write a program to implement these rules. 
if name is less than 3 characters long 
   name must be at least 3 characters 
otherwise if it's more than 50 characters long 
   name can be a maximum of 50 characters 
otherwise
   name looks good!

My answer:

name = 50 
if name < 3:
    print("Name must be at least 3 characters long.")
elif name > 50:
    print("Name can be a maximum of 50 characters long.")
else:
    print("Name looks good!")

"""
name = "Jfsdfjslkdfjs"  #print(len(name))
if len(name) < 3:
    print("Name must be at least 3 characters.")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters.")
else:
    print("Name looks good.")







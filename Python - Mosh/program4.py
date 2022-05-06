"""
Type conversion. 
"""
#Python program to ask the year born in, age then print.
birth_year = input("Birth year: ")
print(type(birth_year))
age = 2019 - int(birth_year)
print(type(age))
print(age)

"""
Error. Age = 2019-birth_year. "Unsupported operand type(s) for -: 'int' and 'str'"
This means that we are subtracting string froom integer. 
Convert the 1982 to integer and then we can subtract.
int, float, bool.

Before correcting:
birth_year = input("Birth year: ")
age = 2019 - birth_year
print(age)

After correcting:
birth_year = input("Birth year: ")
age = 2019 - int(birth_year)
print(age)

Whenever we use input function we always get a string. 
If you are expecting a numerical value, convert it to integer or a float.

Exercise:
Ask a user their weight (in pounds), convert it to kilograms and print on the terminal. 

My answer:
weight = input("What is your weight?: ")
kg = int(weight) / 2.2046
print(kg)

"""
weight_lbs = input("Weight(lbs): ")
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)

"""
Error: can't multiply sequence by non-int of type 'float'.
Input function returns string. We cannot return string. 

"""
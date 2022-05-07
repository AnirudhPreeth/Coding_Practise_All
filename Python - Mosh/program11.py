"""
If Statements. 
"""
"""
If it's hot
   It's a hot day
   Drink plenty of water. 
Otherwise if it's cold
   It's a cold day
   Wear warm clothes
Otherwise
   It's a lovely day.

"""

#Original code. 
is_hot = False
is_cold = True
if is_hot: 
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")

#If both false, "It's a lovely day", will be printed out.

#During explanation, different code. 
is_hot = False
if is_hot: 
    print("\nIt's a hot day")
    print("Drink plenty of water")
else:
    print("\nIt's a cold day")
    print("Wear warm clothes")
print("\nEnjoy your day")

#Define a boolean variable.

is_hot = False
if is_hot: 
    print("\nIt's a hot day")
print("\nEnjoy your day")

"""
Exercise: 

Imagine, Price of house is $1M. 
If buyer has good credit, they need to put down 10%. 
Otherwise, they need to put down 20%. 
Print the down payment. 

My answer: 

good_credits = True 
if good_credits: 
    print("Put down the 10%.")
else:
    print("Put down the 20%.")
print("Down payment: ")

Incomplete answer. 

"""
price = 1000000
has_good_credit = True
if has_good_credit:
    down_payment = 0.1*price
else: 
    down_payment = 0.2*price
print(f"\nDown Payment: ${down_payment}")
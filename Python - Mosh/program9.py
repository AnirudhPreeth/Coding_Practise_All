"""
Operator Precedence.
"""
#Question. 
# x = 10+3*2
#The answer is 16. Why? Operator Precedence. 
#The order of operations. 
#Multiplication operator has a higher precedence. So, that is calculated first. 

x = 10 + 3 * 2 
print(x)
x = 10 + 3 * 2 ** 2
print(x)
x = (10 + 3) * 2 ** 2
print(x)
#Exponentiation -> 2**3.
#Multiplication or division. 
#Addition or subtraction. 
#Parenthesis -> Priority. 

"""
Exercise: 

x = (2+3) * 10 - 3

My answer: 

Parenthesis first. That will be 5. Then the multiplication. 5*10 = 50. 
Then at last, subtraction. 
So, 50-3 = 47.  

"""
x = (2+3) * 10 - 3 
print(x)





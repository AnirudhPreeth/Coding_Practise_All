"""
String Methods. 
"""
course = 'Python for Beginners'
print(len(course))
print(course.upper())
print(course)
print(course.lower())
print(course.find('P'))
print(course.find('o'))
print(course.find('O')) #Upper case O.
print(course.find('Beginners'))
print(course.replace('Beginners', 'Absolute Beginners'))
print(course.replace('beginners', 'Absolute Beginners')) #Case sensitive.
print(course.replace('P', 'J'))
print('Python' in course)
print('python' in course)

#Expression which produces a boolean value. We refer to this as boolean expression.

#len function - useful when get input from user. 
#len function - count the number of characters in the string. 
#Limit on no. of characters from user. More characters -> error.  
#len function is built in. General purpose function. 
#Use this function to count the number of items in a list. 

#Dot operator. 
#We refer to all those functions as methods. (Functions specific to strings).
#When a function belongs to something else or is specific to some kind of object we refer to that as method.
#Upper is a method. In contrast, len and print are general purpose functions.
#They don't belong to strings or numbers. Or other kinds of objects. 
#That is the difference between functions and methods. 

#Find method is case sensitive. 
#Replace is also case sensitive. 
#Find method returns the index. 
#in operator produces a boolean value. 




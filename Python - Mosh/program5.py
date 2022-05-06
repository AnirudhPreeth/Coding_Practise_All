"""
Strings.
"""

course = "Python's course for beginners."
print(course)   
course = 'Python for "beginners".'
print(course)
course = 'Python for Beginners'
print(course[0])

#Know when to use '' and "". 
#Triple quotes. '''. This could be single and double. 

course = '''
Hi John, 
Here is our first E-mail to you. 
Thank you, 
The Support team.
'''
print(course)
#It is a multiline string which we have to print out. 

course = 'Python for Beginners'
another = course[:]
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[1:])
print(course[:5])
print(another)
#Negative index is from the end. 
#All the characters from 0 to 2. (3)
#Another variable - return all the characters. 
#Square bracket syntax.

"""
Exercise: 

Define a variable called name and set it to Jennifer. 
When we print name of 1:-1? What do you think we will see on the terminal? Without running code.
name = 'Jennifer'
print(name[1:-1])

My answer :

We will see that ennife. As the first index will be ignored and so will the last index be ignored.
So 1 will give us ennifer. The -1 included will give us ennife. 

"""
#Running program...
name = 'Jennifer'
print(name[1:-1])
#It prints ennife.
#My answer is correct. 



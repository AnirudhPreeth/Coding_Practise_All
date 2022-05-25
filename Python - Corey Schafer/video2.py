"""
Video 2.
"""
message = "Hello, world!" #Or even my_message would be fine, according to the user. 
                          #Single quote and double quotes are fine for string. 

my_message= 'Bobby\'s World.' #One way to use multiple single quotes in string. 
                              #Or you can use double qoutes. 

multiline_string = """Bobby's World was a good
cartoon in the 1900's. """
                   #This """ ...""" represents a multiline string. 

print(message)
print(my_message) 
print(multiline_string)
print(len(message))

print(message[0])
print(message[0:5])
print(message[:5])
print(message[6:])
"""
How many characters in a string -> len function. 
Len (len) stands for "length".

Access our string's character's individually. To do this, we can use the [] after our string and pass...
...in the location of the character that we want. 
The location is called as "index" and it starts at 0. So, to access the first character in the string...
...and then put in index of 0.
Index is basically -> Index = Total length - 1. 

Range of our characters -
If we only wanted to get "Hello" from our string [in message variable], we could say [0:5]... 
...first index is starting point and second index is stopping point. First index is inclusive...
...(which means it's gonna include it) but the second index is not.
Since starting point here is first index (0), we can just leave that off. And it will assume that we...
...want to start from the beginning. If we leave that and just do [:5], we ge the same result.
If we wanted to get only "World" from the string just do [6:], and it just goes to the end. 
This is called Slicing. 

Data types: 
Methods vs Functions -> They are the same. A method is basically a function that belongs to an object. 

"""
class practice:"py"
# strings
print("hello")
# assign string to a variable
a="hey"
print(a)
""" multiline strings.
    you can assign a multiline string to a variable 
    by using by using three quoutes or single qoutes:"""
a=""" you must be the change
      you wish to see in the world.
      accept yourself, love yourself
      and keep moving forward,if you want
      to fly, you have to give up what
      weighs you down."""
print(a)
# strings are arrays
a="hey , Petras!"
print(a[1])
# string length
a="hey,Petras!"
print(len(a))

#slicing strings
b="hey,sweetheart"
print(b[1:5])
# negative index
b="hey,sweetheart"
print(b[-3:-1])
#modify strings
# upper case
a="hello , sweets!"
print(a.upper())
# lower case
a="HELLO,SWEETS"
print(a.lower())
"""  remove whitespace.The strip()method removes 
     any whitespace from the beginning or the end"""
a="hello,sweets!"
print(a.strip())
# replace string
a="Hey, sweets!"
print(a.replace("y","i"))
#split string
a="Hello ,sunshine!"
print(a.split(","))
# concatenate
a="hey"
# list allow duplicate
items=["book"," box of water","wallet"]
print(items)

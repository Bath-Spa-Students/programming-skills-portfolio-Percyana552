
"""Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.
   As they enter each topping,print a message saying you’ll add that topping to their pizza."""


age=int(input("Enter your age: "))
while age:
   if age < 3:
      print("The ticket is free")
      age=int(input("Enter your age: "))
   elif age>=3 and age<12:
      print(" the ticket is $10")
      age=int(input("Enter your age: "))
   elif age>12:
      print("the ticket is $15")
      age=int(input("Enter your age: "))






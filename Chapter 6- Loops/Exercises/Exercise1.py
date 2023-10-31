"""Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. 
   As they enter each topping,print a message saying you’ll add that topping to their pizza. 
   while loop = execute some code while some condition remains true."""

pizza_topping=input("pizza topping: ")
#name = pepperoni
pizza_toppings=[]
#While Loop
while pizza_topping !="quit":
    pizza_toppings.append(pizza_topping)
    pizza_topping=input("another pizza topping (type 'quit' to end):")
for topping in pizza_toppings:
    print(f" the toppings in your pizza is {topping}")
    

# Use a loop to print a sentence about each river, such as The Nile runs through Egypt
watercourse={'nile': 'Egypt', 'yellow river':'china','colombia':'united states, canada'}
for watercourse, country in watercourse.items():
    print(f'The {watercourse} runs through  {country}')
#print the name of each watercouse
watercourse={'nile': 'Egypt', 'yellow river':'china','colombia':'united states, canada'}
print("\nwatercourse:")
for watercourse in watercourse.keys():
    print(watercourse)

 # print the  country of each watercourse
 
watercourse={'nile': 'Egypt', 'yellow river':'china','colombia':'united states, canada'}
print("\ncountries:")
for country in watercourse.values():
    print(country)  

# make several dictionaries where each dictionary represent different pet , include the kind of animal and the owner

Pets=[{'kind':'cat','owner':'Percy'},{'kind': 'dog',  'owner':  'Petronia'},{'kind':'snack','owner':  'Gabriel'}]
for pet in Pets:
    print(f"\n{pet['owner']}'s{pet['kind']}:")
for key , value in pet.items():
    print(f"{key.title()}:{value.title()}")   


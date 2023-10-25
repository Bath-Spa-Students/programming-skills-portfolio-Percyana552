guest = ["peter","luisa","my sister"]
print(f"I would like to invite {guest[0]} to dinner")
print(f"I would like to invite {guest[1]} to dinner")
print(f"I would like to invite {guest[2]} to dinner")

print(f"unforunatley, {guest[2]} cannot go to your dinner")
guest.remove("my sister")
guest.append("my brother")

print(f"I would like to invite {guest[0]} to dinner")
print(f"I would like to invite {guest[1]} to dinner")
print(f"I would like to invite {guest[2]} to dinner")
print()
print("i unfortunatly i have to reduce the guest list because of my new dinner table cannot arrive on time")
guest.pop()

print(f"{guest[0]} is still invited to your dinner")
print(f"{guest[1]} is still invited to your dinner")

del(guest)

print(guest)

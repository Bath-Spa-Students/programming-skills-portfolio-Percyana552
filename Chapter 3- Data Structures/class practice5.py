# tuples
items=("notebook","pen","board")
print(items)
# convert tuple into list to be able to change it
x=("notebook","pen","board")
y=list(x)
y[0]="correction pen"
x=tuple(y)
print(x)
#unpack Tuples
fruits=("banana","orange","apple")
print(fruits)
# create set
clothes={"dress","high-heels","purse"}
print(clothes)
# add item to set
clothes={"dress","high-heels","purse"}
clothes.add("skirt")
print(clothes)

#Vending machine.py
product_drinks=[{'unit':0,
                 'name':'pepsin',
                 'price':8},
                {'unit':1,
                 'name' :'  lancnor',
                 'price':10},
                {'unit':2,
                 'name':'coca cola',
                 'price':6},
                {'unit':3,
                 'name':'cocktails',
                 'price':50},
                {'unit':4,
                 'name':'natural',
                 'price':15},
                {'unit':5,
                 'name':'water',
                 'price':15}]
product_snacks=[{'unit':6,
                 'name':'pringles',
                 'price':18},
                {'unit':7,
                 'name':'salted cashews',
                 'price':25},
                {'unit':8,
                 'name':'chips',
                 'price': 5}]
product_sweet=[{'unit':9,
                'name':'cupcakes',
                'price':3},
               {'unit':10,
                'name':'Donuts',
                'price':15 },
               {'unit':11,
                'name':'cake',
                'price':23},
               {'unit':12,
                'name':'cookies',
                'price':10},
               {'unit':13,
                'name':'Muffins',
                'price':'17'},
               {'unit':14,
                'name':'roll cake',
                'price':20}]

product_coffee=[{'unit':15,
                 'name':'Espresso',
                 'price':14},
                {'unit':16,
                 'name':'Latte',
                 'price':18},
                {'unit':17,
                 'name':'Cappuccino',
                 'price':11},
                {'unit':18,
                 'name':'Americano',
                 'price':19}]
product= False
products=''
while product== False:
    print("Welcome to Petras vending machine")
    for i in products:
        print(f"product name:{i['name']}-price: {i['price']}- unit {i['unit']}")
    product_1=int(input("enter the unit number of the product you would like to geet:"))
    for i in products:
        if product_1==i['unit']:
            products=i
        if products=='':
            print('invalid unit')
        else:
            print(f"wonderful,{product['name']} will cost you {product['price']}AED")
            price=int(input(f"Enter{product['price']}AED to purchase:")) 
        if price== product['price']:
            print(f" Thank you for buying here your {product['name']}")
        else:
            print(f"please enter only {product['price']}AED")
        product_1=input(" to quit the machine enter q and to buy enter any key")
        if product_1=='c':
            product= False
        else:
            product=True
            print('')               
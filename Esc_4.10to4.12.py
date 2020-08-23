# 4.10

pizzanames = ['Pepperoni', 'BBQ', 'Hawaiian', 'Meat_lover', 'Meatball']

print(f"The first 3 items in the list are: {pizzanames[0:3]}")
print(f"The items from the middle of the list are : {pizzanames[1:4]}")
print(f"The last three items in the list are: {pizzanames[-3:]}")

# 4.11

friend_pizza = pizzanames[:]
print(friend_pizza)

pizzanames.append('Ham')
print(pizzanames)

friend_pizza.append('vegetable')
print(friend_pizza)

print("My favorite pizzas are: ")
for my in pizzanames:
    print(my)

print("My friend's favorite pizzas are:")
for friend in friend_pizza:
    print(friend)

# 4.13

buffet = ('noodles', 'rice', 'soup', 'dumplings', 'vegetable')

for basicfood in buffet:
    print(f"Stable food offerings: {basicfood}")

# buffet[0] = 'duck'


buffet = ('duck', 'sushi', 'dimsum', 'dumplings', 'vegetable')
for re_basicfood in buffet:
    print(f"Revised Basic menu items: {re_basicfood}.")

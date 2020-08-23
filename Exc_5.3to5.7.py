# 5.3

alien_color = 'green'

if alien_color == 'green':
    print('You have just earned 5 points.')

if alien_color == 'red':
    print('no output')

# 5.4

if alien_color == 'green':
    print('You have just earned 5 points.')
else:
    print('You have just earned 10 points.')

# 5.5

if alien_color == 'green':
    print('You have just earned 5 points.')

elif alien_color == 'yellow':
    print('You have just earned 10 points')

elif alien_color == 'red':
    print('You have just earned 15 points')

# 5.6

age = 66

if age < 2:
    print('This is a baby.')

elif age >= 2 and age < 4:
    print('this person is a toddler.')

elif age >= 4 and age < 13:
    print('This person is a kid.')

elif age >= 13 and age < 20:
    print('This person is a teenager.')

elif age >= 20 and age < 65:
    print('This person is an adult.')

else:
    print('This person is an elder.')

# favorite_fruits = ['orange', 'watermelon', 'blueberry']
#
# ffruit1 = 'orange'
# ffruit2 = 'watermelon'
# ffruit3 = 'blueberry'
#
# if ffruit1 in favorite_fruits:
#     print(f'I really like {ffruit1}!')
#
# if ffruit2 in favorite_fruits:
#     print(f'I really like {ffruit2}!')
#
# if ffruit3 in favorite_fruits:
#     print(f'I really like {ffruit3}!')

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")

available_fruits = ['orange', 'watermelon', 'blueberry', 'peach', 'mango']

favorite_fruits = ['orange', 'watermelon', 'blueberry', 'banana']

# ffruit1 = 'orange'
# ffruit2 = 'watermelon'
# ffruit3 = 'blueberry'

for favorite_fruit in favorite_fruits:
    if favorite_fruit in available_fruits:
        print(f'I really like {favorite_fruit}!')
    else:
        print(f'I actually do not like {favorite_fruit}')

# 7.1

# cars = input('What car would you like: ')
#
# print(f"Let me see if I can find you a {cars}.")


# 7.2

# seats = int(input('How many people are in your dinner group?:'))
#
# if seats > 8:
#     print(f"You have to wait for a table.")
# else:
#     print("your table is ready.")

# 7.3

# numbers = int(input("What number you want to put in?: "))
#
# if numbers % 10 == 0:
#     print("Your number is multiple of 10")
# else:
#     print("Your number is not multiple of 10")

# 7.4

# messages = "What toppings do you like?: "
#
# toppings = ""
# while toppings.lower() != 'quit':
#     toppings = input(messages)
#     print(toppings)

# 7.5

# message = 'How old are you?: '
# message += '\nEnter quite when you are finished.'
#
# while True:
#     age = input(message)
#     if age.lower() == 'quit':
#         break
#     age = int(age)
#
#     if age < 3:
#         print('The ticket is free!')
#     elif age < 13:
#         print(('The ticket is $10'))
#     else:
#         print("The ticket is $15")


# 7.6

# mesaage = "How old are you?: \nPlease enter quite when you are done."
#
# active = True
#
# while active:
#     age = input(mesaage)
#     if age.lower() == 'quit':
#         active = False
#
#     age = int(age)
#
#     if age < 3:
#         print("Your ticket is FREE!")
#     elif age < 13:
#         print('The price is $5')
#     else:
#         print('The price is $15')

mesaage = "How old are you?: \nPlease enter quite when you are done."

age = ""
while age != 'quit':
    age = int(input(mesaage))

    if age < 3:
        print("Your ticket is FREE!")
    elif age < 13:
        print('The price is $5')
    else:
        print('The price is $15')



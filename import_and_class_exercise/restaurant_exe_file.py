from import_and_class_exercise.restaurant_class import Restaurant

customer1 = Restaurant('tasty castle', 'meatball bun')

customer1.describe_restaurant()
customer1.open_restaurant()
customer1.set_number_served(860)
print(f"We have served {customer1.number_served} customers so far for today.")
print('Closing shop...')
customer1.increment_number_served(160)
print(f'We have served {customer1.number_served} customers for the day!')
print('Have a nice day everyone!')

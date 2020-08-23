# 6.1

friends = {'first_name': 'justin', 'last name': 'ma', 'city': 'new york'}

print(friends)
for key, value in friends.items():
    print(key, value)

# 6.2
favorite_nums = {'Justin': 8, 'Dan': 3, 'Kevin': 46, 'Chel': 99, 'Nikky': 62}
for name, number in favorite_nums.items():
    print(f"{name}'s favorite number is: {number}")

# 6.3

appkeys = {'loop': 'to loops through each elements in the lists or dictionaries',
           'list': 'store items in form of a list',
           'variables': 'to store temporary data',
           'if statement': 'for the if functions',
           'input': 'to let you enter data into the variables'
           }

for key, meaning in appkeys.items():
    print(f"{key}:")
    print(f"\t {meaning}")

# 6.4

appkeys['Max'] = 'max number in the list'
appkeys['Min'] = 'min number in the list'
appkeys['Sum'] = 'total amount'

print('***************Motify*****************')
for key, meaning in appkeys.items():
    print(f"{key}:")
    print(f"\t {meaning}")

# 6.5

rivers = {'nile': 'egypt', 'amazon': 'brazil', 'Yangtze': 'china'}
for river, country in rivers.items():
    print(f"The {river.title()} river runs through {country.title()}.")

for river, country in rivers.items():
    print(f"River name: {river.title()}")
    print(f"Country's name: {country.title()}")

# 6.6

favorite_languages = {'jen': 'python',
                      'sarah': 'c',
                      'edward': 'ruby',
                      'phil': 'python',
                      }

friends_list = ['justin', 'jen', 'sarah', 'sam', 'edward', 'phil']

for friend in friends_list:
    if friend in favorite_languages.keys():
        print(f"{friend.title()} thank you for taking the poll.")
    else:
        print(f"{friend.title()} please register for the poll.")

# 6.7
friends1 = {'first_name': 'justin', 'last_name': 'ma', 'city': 'new york', }
friends2 = {'first_name': 'lydia', 'last_name': 'chen', 'city': 'Shanghai', }
friends3 = {'first_name': 'tony', 'last_name': 'jiang', 'city': 'unknow', }

people = [friends1, friends2, friends3]

for individual in people:
    for key, value in individual.items():
        print(f"{key.upper()}: {value.title()}")

# 6.8

butter = {'animal': 'cat', 'owner': 'justin'}
pepper = {'animal': 'cat', 'owner': 'frehnzel'}
oldlady = {'animal': 'dog', 'owner': 'luis'}

pets = [butter, pepper, oldlady]
for pet in pets:
    for key, value in pet.items():
        print(f"{key.title()}: {value.title()}")

# 6.9
favorite_places = {'justin': 'guangzhou', 'lydia': 'shanghai', 'Kenzy': 'new york'}
for name, place in favorite_places.items():
    print(f"{name.title()}'s favorite place to visit is {place.title()}.")

# 6.10

favorite_nums = {'Justin': [8, 3, 9], 'Dan': [3, 16, 12], 'Kevin': [46, 11, 7], 'Chel': [99, 69, 12],
                 'Nikky': [62, 55, 79]}

for name, value in favorite_nums.items():
    print(f"{name.title()}'s favorite numbers are: \n{value}")

# 6.11
cities = {'shanghai': {'country': 'china', 'population': 24.8, 'facts': 'pearl of the east'},
          'new york': {'country': 'unite states', 'population': 8.39, 'facts': 'big apple'},
          'guangzhou': {'country': 'china', 'population': 14.9, 'facts': 'culinary heaven'}
          }
for city, fact in cities.items():
    print(
        f"{city.title()} is a beautiful city in {fact['country'].title()} with population of {fact['population']} million people."
        f"It is also know as {fact['facts'].title()}")

numbers = list(range(1, 11))

for number in numbers:
    for multi in numbers:
        print(f"{number} X {multi} = {number*multi}")

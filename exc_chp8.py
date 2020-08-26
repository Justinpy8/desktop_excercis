# 8.1
# def display_message():
#     print('I am learning about function in this chapter.')
#
#
# display_message()


# 8.2

# def favorite_book(book_name):
#     print(f"My favorite book is {book_name}")
#
#
# favorite_book('Alice in Wonderland')

# 8.3
# def make_shirt(size):
#     print(f"This shirt is in size: {size}")
#
# 
# make_shirt('medium')

# def make_shirt(size):
#     print(f"This shirt is in size: {size}")
#
#
# make_shirt(size='medium')

# 8.4

# def make_shirt(size='large'):
#     if size in ['large', 'medium']:
#         print('I love Python!')
#     else:
#         print('I still love Python regardless!')
#
#
# make_shirt()
# make_shirt('large')
# make_shirt('medium')
# make_shirt('small')

# 8.5
# def describe_city(city, country='china'):
#     print(f"{city.title()} is in {country.title()}.")
#
#
# describe_city('shanghai')
# describe_city('hong kong', 'china')
# describe_city('tokyo', 'japan')

# def build_person(first_name, last_name, age=''):
#     """Return a dictionary of information about a person."""
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person
#
#
# musician = build_person('jimi', 'hendrix', 27)
# print(musician)

# 8.6
# def city_country(city, country):
#     return city.title() + "," + country.title()
#
#
# cities = city_country('shanghai', 'china')
# cities2 = city_country('hong kong', 'china')
# cities3 = city_country('guangzhou', 'china')
# print(cities)
# print(cities2)
# print(cities3)


# 8.7
# def make_album(name, title, tracks=''):
#     album = {'albumname': name, 'albumtitle': title}
#     if tracks:
#         album['tracknumbers'] = tracks
#     return album
#
#
# songs0 = make_album('mike', 'dance in the floor')
# songs1 = make_album('tim', 'dance in the rain')
# songs2 = make_album('justin', 'dance in the sky', 16)
#
# print(songs0)
# print(songs1)
# print(songs2)

# 8.8
def make_album(name, title):
    album = {'albumname': name, 'albumtitle': title}
    return album


messagealn = 'What album are you looking for?'
messageatn = 'Who is the artist?'

print('Please ENTER q and anytime to quit.')

while True:
    cdname = input(messagealn)
    if cdname == 'q':
        break

    artist = input(messageatn)
    if artist == 'q':
        break

    song1 = make_album(cdname, artist)
    print(song1)

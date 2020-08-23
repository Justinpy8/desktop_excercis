# 5.1

car = ['audi', 'bmw', 'toyota', 'subaru', 'benz', 'honda']
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# # 5.2


if car == 'subaru':
    print("My wife will let me buy this new car!")
else:
    print("Guess I am not getting a new car!")

if car != 'toyota':
    print("My wife won't let me buy this car.")

nums = 21

if nums == 21:
    print('Bingo')

if nums != 1:
    print('oops')

if nums < 25:
    print("too young")

if nums > 20:
    print("old ass")

score1 = 100
score2 = 70
score3 = 80

if score1 > score2:
    print('big bro')
elif score3 > score2:
    print('3rd is a charm')
else:
    print('nothing happens')


if score1 < 200 and score2 < 200:
    print('true son!')

if score1 > 200 or score3 == 80:
    print('oh boy')

super_car = ['audi', 'bmw', 'toyota', 'subaru', 'benz', 'honda']

# my_fav = 'bmw'
if 'benz' in super_car:
    print('I will buy it')

# my_sefav = 'volvo'
if 'honda' not in super_car:
    pass

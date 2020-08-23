# 5.8

# user_names = ['sleepingbeaz', 'singerb', 'skynet', 'karen', 'jma', 'admin']

# for user_name in user_names:
#     print(f"Hello {user_name.title()}, hope you are doing well today!")
#
# for user_name in user_names:
#     if user_name == 'admin':
#         print(f"Hello admin, would you like to see a status report?")
#     else:
#         print(f"Hello {user_name.title()}, thank you for logging in again!")


# 5.9#

# if not user_names:
#     print("We need more users!")
# else:
#     print('We have users in the list')

# 5.10

current_users = ['sleepingbeaz', 'singerb', 'skynet', 'karen', 'jma', 'admin']
new_users = ['sleepingbeaz', 'sob', 'skynet', 'timfly', 'jma', 'admin']

for new_user in new_users:
    if new_user.lower() in current_users:
        print('Please choose a different user name.')
    else:
        print(f'{new_user} is available.')


# 5.11

ordinal_numbers = list(range(1, 10))

for ordinal_number in ordinal_numbers:
    if ordinal_number == 1:
        print(f"{ordinal_number}st")
    elif ordinal_number == 2:
        print(f"{ordinal_number}nd")
    elif ordinal_number == 3:
        print(f"{ordinal_number}rd")
    else:
        print(f"{ordinal_number}st")


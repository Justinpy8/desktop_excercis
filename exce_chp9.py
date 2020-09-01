# 9.1 - 9.2

# class Restaurant():
#     def __init__(self, name, cuisine_type):
#         self.name = name.title()
#         self.cuisine_type = cuisine_type.title()
#
#     def describe_restaurant(self):
#         msg = f"{self.name} makes great {self.cuisine_type}!"
#         print(f'\n {msg}')
#
#     def open_restaurant(self):
#         msg = f"{self.name} is open. Get in here!!!"
#         print(f"\n {msg}")
#
#
# restaurant1 = Restaurant('lucky house', 'cmeat sandwich')
#
# print(restaurant1.name)
# print(restaurant1.cuisine_type)
#
# restaurant1.describe_restaurant()
# restaurant1.open_restaurant()
#
# restaurant2 = Restaurant('spicy kitchen', 'hothot tofu')
#
# print(restaurant2.name)
# print(restaurant2.cuisine_type)
#
# restaurant2.describe_restaurant()
# restaurant2.open_restaurant()
#
# restaurant3 = Restaurant('hometown kitchen', 'bbq duck')
#
# print(restaurant3.name)
# print(restaurant3.cuisine_type)
#
# restaurant3.describe_restaurant()
# restaurant3.open_restaurant()

# 9.3

class User():

    def __init__(self, first, last, sex, grade, gdp):
        self.first = first.title()
        self.last = last.title()
        self.sex = sex
        self.grade = grade
        self.gdp = gdp
        self.login_attempts = int()

    def describe_user(self):
        info = (self.first, self.last, self.sex, self.grade, self.gdp)
        print(
            f"First Name: {self.first} \nLast Name: {self.last} \nSex: {self.sex} \nGrade: {self.grade} \nDGP: {self.gdp}")

    def greet_user(self):
        if self.grade == int(1):
            print(f"{self.first} {self.last} is a {self.sex} in {self.grade}st grade with a GDP of {self.gdp}.")
        elif self.grade == int(2):
            print(f"{self.first} {self.last} is a {self.sex} in {self.grade}nd grade with a GDP of {self.gdp}.")
        elif self.grade == int(3):
            print(f"{self.first} {self.last} is a {self.sex} in {self.grade}rd grade with a GDP of {self.gdp}.")
        else:
            print(f"{self.first} {self.last} is a {self.sex} in {self.grade}th grade with a GDP of {self.gdp}.")

    def increment_login_attempts(self, ):
        self.login_attempts += 1

    def reset_login_attempts(self, reset_login=0):
        self.login_attempts = reset_login


#
# student1 = User('john', 'smith', 'boy', 5, 3.9)
#
# student1.describe_user()
# student1.greet_user()
#
# student2 = User('Mary', 'thompson', 'girl', 1, 3.1)
#
# student2.describe_user()
# student2.greet_user()
#
# student3 = User('jerry', 'chen', 'boy', 2, 3.6)
#
# student3.describe_user()
# student3.greet_user()


# 9.4

class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type.title()
        self.number_served = 0

    def describe_restaurant(self):
        msg = f"{self.name} makes great {self.cuisine_type}!"
        print(f'{msg}')

    def open_restaurant(self):
        msg = f"{self.name} is open. Get in here!!!"
        print(f"{msg}")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment):
        self.number_served += increment


#
#
# restaurant = Restaurant('lucky house', 'meatball sandwich')
#
# restaurant.number_served = 500
# print(f"The restaurant has served {restaurant.number_served} customers today so far! ")
#
# restaurant.number_served = 890
# print(f"The restaurant has served {restaurant.number_served} customers today so far! ")
#
# restaurant.set_number_served(600)
# print(f"The restaurant has served {restaurant.number_served} customers today so far! ")
#
# restaurant.increment_number_served(300)
# print(f"The total number of customers served today: {restaurant.number_served}")

# 9.5

# user1 = User('john', 'smith', 'boy', 5, 3.9)
#
# print("Printing 3 login attempts")
# user1.increment_login_attempts()
# user1.increment_login_attempts()
# user1.increment_login_attempts()
# print(user1.login_attempts)
#
# print("Reset the login to 0")
# user1.reset_login_attempts()
# print(user1.login_attempts)

# 9.6

# class IceCreamStand(Restaurant):
#
#     def __init__(self, name, cuisine_type):
#         super().__init__(name, cuisine_type)
#         self.flavors = []
#
#     def get_flavors(self):
#         print('We server the follow ice cream flavors:')
#         for flavor in self.flavors:
#             print(f" - {flavor.title()}")
#
#
# icecream = IceCreamStand('lucky house', 'ice cream')
# icecream.flavors = ['vanilla', 'chocola', 'blue berry']
#
# icecream.describe_restaurant()
# icecream.get_flavors()

# 9.7

class Admin(User):
    def __init__(self, first, last, sex, grade, gdp):
        super().__init__(first, last, sex, grade, gdp)
        self.privileges = Privileges()


# 9.8
class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print('This admin user have the following privileges:')
        for privilege in self.privileges:
            print(f"- {privilege}")


admin_user = Admin('john', 'smith', 'boy', 5, 3.9)

admin_user.privileges.show_privileges()

admin_user_privileges = ['add', 'delete', 'post', 'ban']
admin_user.privileges.privileges = admin_user_privileges
admin_user.privileges.show_privileges()

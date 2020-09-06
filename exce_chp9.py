# 9.1 - 9.2

class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type.title()

    def describe_restaurant(self):
        msg = f"{self.name} makes great {self.cuisine_type}!"
        print(f'\n {msg}')

    def open_restaurant(self):
        msg = f"{self.name} is open. Get in here!!!"
        print(f"\n {msg}")


restaurant1 = Restaurant('lucky house', 'meatball sandwich')

print(restaurant1.name)
print(restaurant1.cuisine_type)

restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2 = Restaurant('spicy kitchen', 'hothot tofu')

print(restaurant2.name)
print(restaurant2.cuisine_type)

restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3 = Restaurant('hometown kitchen', 'bbq duck')

print(restaurant3.name)
print(restaurant3.cuisine_type)

restaurant3.describe_restaurant()
restaurant3.open_restaurant()

# 9.3

class User():

    def __init__(self, first, last, sex, grade, gdp):
        self.first = first.title()
        self.last = last.title()
        self.sex = sex
        self.grade = grade
        self.gdp = gdp

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


student1 = User('john', 'smith', 'boy', 5, 3.9)

student1.describe_user()
student1.greet_user()

student2 = User('Mary', 'thompson', 'girl', 1, 3.1)

student2.describe_user()
student2.greet_user()

student3 = User('jerry', 'chen', 'boy', 2, 3.6)

student3.describe_user()
student3.greet_user()
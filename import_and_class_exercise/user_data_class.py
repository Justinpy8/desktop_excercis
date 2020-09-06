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
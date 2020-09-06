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

# from import_and_class_exercise.user_data_class import User
#
# class Admin(User):
#     def __init__(self, first, last, sex, grade, gdp):
#         super().__init__(first, last, sex, grade, gdp)
#         self.privileges = Privileges()
#
#
# # 9.8
# class Privileges():
#     def __init__(self, privileges=[]):
#         self.privileges = privileges
#
#     def show_privileges(self):
#         print('This admin user have the following privileges:')
#         for privilege in self.privileges:
#             print(f"- {privilege}")
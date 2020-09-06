from import_and_class_exercise.user_data_class import Admin, Privileges, User

admin_user1 = Admin('john', 'smith', 'boy', 1, 3.9)
privilege_values = ['add', 'remove', 'modify']
admin_user1.privileges.privileges = privilege_values
print(admin_user1.privileges)
admin_user1.privileges.show_privileges()

from import_and_class_exercise.user_data_class import User
# from import_and_class_exercise.restaurant_class import Admin, Privileges
#
# admin_user1 = Admin('john', 'smith', 'boy', 1, 3.9)
# privilege_values = ['add', 'remove', 'modify']
# admin_user1.privileges.privileges = privilege_values
# print(admin_user1.privileges)
# admin_user1.privileges.show_privileges()

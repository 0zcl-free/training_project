"""
username_input = input("input your name:")
userage_input = input("input your age:")
userwork_input = input("input your work:")
print("user input messeges:", username_input, userage_input, userwork_input)
"""


name = input("input your name:")
age = int(input("input your age:"))
job = input("input your job:")

msg = '''
Information of user %s:
---------------------
Name: %s
Age:  %d
Job:  %s
---------END---------
''' %(name, name, age, job)
print(msg)

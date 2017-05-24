age = 21

guess_num = int(input("input your guess age;"))

if guess_num == age:
    print("Luck!you got it.")
elif guess_num > age:
    print("Think is smaller.")
else:
    print("Think is bigger.")
age = 21
for i in range(10):
    if i < 3:
        guess_num = int(input("input your guess age;"))

        if guess_num == age:
            print("Luck!you got it.")
            break
        elif guess_num > age:
            print("Think is smaller.")
        else:
            print("Think is bigger.")
    else:
        continue_flag = input("You want to continue?y or n?")
        if continue_flag == 'y':
            i = 0
        else:
            print("Bye...")
            break
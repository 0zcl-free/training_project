age = 21
count = 0
for i in range(10):
    if count < 3:
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
            count = 0
            continue
        else:
            print("Bye...")
            break

    count += 1
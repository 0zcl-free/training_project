
import sys

if __name__ == "__main__":
    num1_list = []
    final_list = []
    input_num1 = int(raw_input())
    for i in range(input_num1):
        num1_list.append(raw_input())

    input_num2 = int(raw_input())
    for j in range(input_num2):
        input_num = raw_input()
        if input_num in num1_list:
            final_list.append(input_num)

    for num in final_list:
        sys.stdout.write("%s " % num)




import re
import sys

# 将输入的字符串格式统一转换成列表,将数字、符号、括号都成一个独立元素，
# 如: 12+3*(14+5)  ----> ["12","+","3","*","(","14","+","5",")"]
def format_input(input_re_value):
    input_re_value = input_re_value.replace(" ", "")     #去掉输入的空格
    input_re_value = re.split(r'(\D)', input_re_value)
    while True:
        if "" in input_re_value:
          input_re_value.remove("")     #将列表中""去掉
        else:
            break

    return input_re_value


# 计算没有括号的列表的值。加减乘除
def comput(re_value):
    while "*" in re_value or "/" in re_value:
        for i, j in enumerate(re_value):
            if j == "*":
                re_cheng = int(re_value[i - 1]) * int(re_value[i + 1])
                re_value.pop(i - 1)
                re_value.pop(i - 1)
                re_value.pop(i - 1)
                re_value.insert(i - 1, re_cheng)
                break

            if j == "/":
                re_chu = int(re_value[i - 1]) / int(re_value[i + 1])
                re_chu = int(re_chu)
                re_value.pop(i - 1)
                re_value.pop(i - 1)
                re_value.pop(i - 1)
                re_value.insert(i - 1, re_chu)
                break
    while "+" in re_value or "-" in re_value:
        for i, j in enumerate(re_value):
            if j == "+":
                re_jia = int(re_value[i - 1]) + int(re_value[i + 1])
                re_value.pop(i - 1)
                re_value.pop(i - 1)
                re_value.pop(i - 1)
                re_value.insert(i - 1, re_jia)
                break

            if j == "-":
                re_jian = int(re_value[i - 1]) - int(re_value[i + 1])
                re_value.pop(i - 1)
                re_value.pop(i - 1)
                re_value.pop(i - 1)
                re_value.insert(i - 1, re_jian)
                break
    return re_value[0]


def bracket(input_str):
    if not re.search(r'\(([^()]+)\)', input_str):    #若没有括号
        s = format_input(input_str)
        return comput(s)
    else:      #有括号
        li = re.split(r'\(([^()]+)\)', input_str)
        data = re.search(r'\(([^()]+)\)', input_str).group()
        data_strip = data.strip("()")
        inde = li.index(data_strip)  #取得其下标

        ret = comput(format_input(data_strip))   #参数为列表形式
        li.pop(inde)
        li.insert(inde, str(ret))
        re_str = "".join(li)

        if "+" not in re_str and "-" not in re_str and "*" not in re_str \
                              and "/" not in re_str and "(" not in re_str and ")" not in re_str:
            return re_str    #为什么没有return
        else:
            return bracket(re_str)   #迭代


if __name__ == '__main__':
    while True:
        input_str = input("please input(q=quit):")
        if input_str.strip() == "":
            continue
        elif input_str == 'q' or input_str == 'quit':
            sys.exit()
        else:
            bracket_reture = bracket(input_str)
            print("result:",bracket_reture)

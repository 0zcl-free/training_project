
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
                print("re_jia",re_jia)
                print("re_value",re_value)
                break

            if j == "-":
                re_jian = int(re_value[i - 1]) - int(re_value[i + 1])
                re_value.pop(i - 1)
                re_value.pop(i - 1)
                re_value.pop(i - 1)
                re_value.insert(i - 1, re_jian)
                print(re_jian)
                print(re_value)
                break
    return re_value[0]


def bracket(input_str):
    if not re.search(r'\(([^()]+)\)', input_str):    #若没有括号
        s = format_input(input_str)
        print("s_format",s)
        print("comput(s)",comput(s))
        return comput(s)
    else:      #有括号
        li = re.split(r'\(([^()]+)\)', input_str)
        print("li:",li)        #['(', '9+8', '-8)']   输入((9+8)-8)
        data = re.search(r'\(([^()]+)\)', input_str).group()
        print("data:",data)    # 输出:(9+8)
        data_strip = data.strip("()")
        print("data_strip:",data_strip)   #9+8
        inde = li.index(data_strip)  #取得其下标
        print("index:",inde)       # 1

        ret = comput(format_input(data_strip))   #参数为列表形式
        print("ret:",ret)    #17.0
        # 如何把小括号计算后再替换进去
        li.pop(inde)
        li.insert(inde, str(ret))
        print("li:",li)   #['(', '17.0', '-8)']

        re_str = "".join(li)
        print("re_str",re_str)   #(17.0-8)


        if "+" not in re_str and "-" not in re_str and "*" not in re_str \
                and "/" not in re_str and "(" not in re_str and ")" not in re_str:
            print("有没有return ",re_str)
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
            print("result:",bracket_reture,type(bracket_reture))

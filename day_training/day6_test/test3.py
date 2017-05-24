# 将输入的字符串格式统一转换成列表,将数字、符号、括号都成一个独立元素，
# 如: 12+3*(14+5)  ----> ["12","+","3","*","(","14","+","5",")"]
def format_input(input_re_value):
    input_re_value = input_re_value.replace(" ", "")
    format_list = []
    for i in input_re_value:
        format_list.append(i)
    snum = 0
    while 1:
        try:
            if format_list[snum].isnumeric():
                if format_list[snum + 1].isnumeric():
                    format_list[snum] = format_list[snum] + format_list[snum + 1]
                    format_list.pop(snum + 1)
                else:
                    snum += 1
            else:
                snum += 1
        except IndexError:
            return format_list
            break


# 计算没有括号的列表的值。
def comput(re_value):
    while "*" in re_value or "/" in re_value:
        for i, j in enumerate(re_value):
            if j == "*":
                re_cheng = float(re_value[i - 1]) * float(re_value[i + 1])
                re_value.pop(i - 1)
                re_value.pop(i - 1)
                re_value.pop(i - 1)
                re_value.insert(i - 1, re_cheng)

            if j == "/":
                re_chu = float(re_value[i - 1]) / float(re_value[i + 1])
                re_value.pop(i - 1)
                re_value.pop(i - 1)
                re_value.pop(i - 1)
                re_value.insert(i - 1, re_chu)
    while "+" in re_value or "-" in re_value:
        for i, j in enumerate(re_value):
            if j == "+":
                re_jia = float(re_value[i - 1]) + float(re_value[i + 1])
                re_value.pop(i - 1)
                re_value.pop(i - 1)
                re_value.pop(i - 1)
                re_value.insert(i - 1, re_jia)

            if j == "-":
                re_jian = float(re_value[i - 1]) - float(re_value[i + 1])
                re_value.pop(i - 1)
                re_value.pop(i - 1)
                re_value.pop(i - 1)
                re_value.insert(i - 1, re_jian)
    return re_value[0]


# 通过循环，先查找列表的第一个")"，然后在")"位置向列表前找到第一个"("所在位置，
# 并将其中的元素提取出来，生成新的列表，交给comput计算，
# 返回值再插入列表当中，继续循环，直到没有"（"为止
def bracket_filter(list1):
    while "(" in list1:
        i = list1.index(")")
        for m in range(i, -1, -1):
            if list1[m] == "(":
                list_new = list1[(m + 1):i]
                re_res = comput(list_new)
                list1.insert(m, str(re_res))
                for item1 in range(i + 1 - m):
                    list1.pop(m + 1)
                break
    return comput(list1)


input_sn = input("pls input:")
f_re = format_input(input_sn)
result = bracket_filter(f_re)
print("The result is:", result)
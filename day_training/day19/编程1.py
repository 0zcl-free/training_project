#
# def compare(str_1, str_2):
#     ret = True
#     for i in str_1:
#         print(i)
#         if i not in str_2:
#             ret = False
#             return ret
#     for j in str_2:
#         if j not in str_1:
#             ret = False
#             return ret
#     return ret
#
#
# if __name__ == "__main__":
#     list_1 = []
#     list_2 = []
#     input_str = raw_input().split()
#     print(">", input_str)
#     str_1 = input_str[0]
#     str_2 = input_str[1]
#
#     ret = compare(str_1, str_2)
#     print(">>>", ret)

# import sys
#
#
#
# if __name__ == "__main__":
#     line0,line1 = sys.stdin.readline().strip().split()
#     print line0,line1
#     if set(line0) == set(line1):
#         print "true"
#     else:
#         print "false"
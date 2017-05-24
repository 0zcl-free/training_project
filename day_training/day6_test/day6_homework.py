import re

def add_multi(num):
    print(num)
    #6+7+2*2/3-8*9-6/3
    for i in num:
        if re.split(r'(\w\*\w)', num) or re.split(r'(\w//\w)', num):
            pass

    s1 =re.split(r'(\w\*\w)', num)
    s2 = re.split(r'(\w/\w)', num)
    print(s1)
    print(s2)

    result = re.split(r'(\w\*\w)', num)
    print(result)


def bracket():
    pass

def main():
    num = input("please input:")
    add_multi(num)


main()
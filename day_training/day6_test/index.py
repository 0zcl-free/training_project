



def run():
    inp = input("please input:")

    m,f = inp.split('/')
    #obj = __import__(m)     #obj相当于模块名

    obj = __import__("lib." + m, fromlist=True)
    print(obj)
#即以字符串形式导入模块，也以字符串形式，找到模块内的方法
    if hasattr(obj, f):
        func = getattr(obj, f)
        func()
    else:
        print("404")

run()



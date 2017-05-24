
data = {}
names = ["zcl", "cxw"]
try:
    names[3]
    #data['name']
    a = 1
    print(a)
except KeyError as e:   #e为异常的详细信息
    print("没有这个key", e)
except IndexError as e:
    print("列表操作错误",e)
except Exception as e:   #可以用在最后面，抓未知错误
    print("未知错误")


else:     #当没有任何错误时执行
    print("一切正常")

finally:   #不管有没有错，都执行
    print("不管有没有错，都执行")


# except (KeyError, IndexError) as e:  #keyerror或者indexerror
#     #虽然省代码，但具体不知道是那里出错，不建议用
#     #当出错时，进行统一处理，可以用
#     print("没有这个key", e)

# except Exception as e:    #抓住所有错误，也可以省代码，但出具代的错误得分析
#     #一般不用，不能定位
#     print("出错了", e)
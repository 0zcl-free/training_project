#coding:utf-8
from wsgiref.simple_server import make_server
import time
from jinja2 import Template


def f1():
    f = open("templates/t1.html")
    data = f.read()
    f.close()
    db_str = str(time.time())
    data = data.replace("((x))", db_str)
    return data


def f2():
    f = open('templates/t2.html')
    result = f.read()
    template = Template(result)
    # 接收值，进行特殊的替换
    data = template.render(name='John Doe', user_list=['alex', 'eric'])
    return data.encode('utf-8')
routers = {
    "/index/": f1,
    "/news/": f2,
}

# environ包含用户请求的所有信息，是wsgi封装好的
def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    url = environ["PATH_INFO"]

    if url in routers.keys():
        func_name = routers[url]
        return func_name()
    else:
        return "404"


if __name__ == '__main__':
    # 创建socket server对象(参数可查看源码构造函数，如果找不到可往父类找直至找到)
    httpd = make_server('', 8000, RunServer)
    print("Serving HTTP on port 8000...")
    # while循环，等待用户请求到来
    # 只要有请求进来，执行RunServer函数
    httpd.serve_forever()

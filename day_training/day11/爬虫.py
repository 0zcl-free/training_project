
from urllib import request
import gevent
import time
from gevent import monkey

monkey.patch_all()  #把当前程序的所有IO操作给单独做上标记


def f(url):
    print('GET: %s' % url)
    resp = request.urlopen(url)
    data = resp.read()
    f = open("url.html", "wb")
    f.write(data)
    f.close()
    print('%d bytes received from %s.' % (len(data), url))

urls = ['https://www.python.org/',
        'https://www.yahoo.com/',
        'https://github.com/',
]


time_start = time.time()
for url in urls:
    f(url)
print("同步cost", time.time() - time_start)

async_time_start = time.time()
gevent.joinall([
        gevent.spawn(f, 'https://www.python.org/'),
        gevent.spawn(f, 'https://www.yahoo.com/'),
        gevent.spawn(f, 'https://github.com/'),
])        #启动三个协程
print("异步cost", time.time() - async_time_start)
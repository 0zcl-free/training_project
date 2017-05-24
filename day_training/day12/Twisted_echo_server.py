# -*- coding:utf-8

from twisted.internet import protocol
from twisted.internet import reactor


class Echo(protocol.Protocol):
    #只要twisted一收到数据就调用此方法
    def dataReceived(self, data):  #把收到的数据返回给客户端
        self.transport.write(data)


def main():
    #定义基础工厂类
    factory = protocol.ServerFactory()
    factory.protocol = Echo  #socket server中的handle

    reactor.listenTCP(9000, factory)   #不能写IP，默认应该是0.0.0.0
    reactor.run()


if __name__ == '__main__':
    main()
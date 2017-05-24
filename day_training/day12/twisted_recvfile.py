# -*- coding:utf-8
# This is the Twisted Get Poetry Now! client, version 3.0.

# NOTE: This should not be used as the basis for production code.

import optparse

from twisted.internet.protocol import Protocol, ClientFactory


def parse_args():
    usage = """usage: %prog [options] [hostname]:port ...

This is the Get Poetry Now! client, Twisted version 3.0
Run it like this:

  python get-poetry-1.py port1 port2 port3 ...
"""
    #parser实例
    parser = optparse.OptionParser(usage)
    #('-->addr:', <Values at 0x371e648: {}>, [])
    _, addresses = parser.parse_args() #前者为parser实例本身,后者为端口号
    print("-->addr:", _,addresses)
    if not addresses:
        print parser.format_help()
        parser.exit()

    def parse_address(addr):
        if ':' not in addr:  #有"："说明有IP地址
            host = '127.0.0.1'
            port = addr
        else:
            host, port = addr.split(':', 1)

        if not port.isdigit():
            parser.error('Ports must be integers.')

        return host, int(port)

    return map(parse_address, addresses)


class PoetryProtocol(Protocol):
    poem = ''

    def dataReceived(self, data):
        self.poem += data  #拼接数据
        print("[%s] recv:[%s]" % (self.transport.getPeer(),len(self.poem)))

    def connectionLost(self, reason):
        self.poemReceived(self.poem)

    def poemReceived(self, poem):  #如果连接断开则调用
        self.factory.poem_finished(poem) #self.factory相当于子类调用父类的东西固定格式


class PoetryClientFactory(ClientFactory):  #基类
    protocol = PoetryProtocol  #PoetryProtocol＝handle方法

    def __init__(self, callback):
        self.callback = callback

    def poem_finished(self, poem):
        self.callback(poem) #相当于self.get_poem(poem)


def get_poetry(host, port, callback):
    """
    Download a poem from the given host and port and invoke
      callback(poem)
    when the poem is complete.
    """
    from twisted.internet import reactor
    factory = PoetryClientFactory(callback)
    reactor.connectTCP(host, port, factory)


def poetry_main():
    addresses = parse_args() #((127.0.0.1,9000),(...))

    from twisted.internet import reactor

    poems = []

    def got_poem(poem):
        poems.append(poem)  #poem收回来的数据
        if len(poems) == len(addresses):  #相等则数据收完
            reactor.stop()

    for address in addresses:
        host, port = address
        get_poetry(host, port, got_poem) #传IP,port,got_poem函数

    reactor.run()

    # for poem in poems:
    #     print poem
    print("main loop done...")

if __name__ == '__main__':
    poetry_main()
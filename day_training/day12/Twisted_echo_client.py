# -*- coding:utf-8

from twisted.internet import reactor, protocol
# a client protocol

class EchoClient(protocol.Protocol):
    """Once connected, send a message, then print the result."""
    #连接一建立成功，就会自动调用此方法
    def connectionMade(self):
        print("connection is build, sending data...")
        self.transport.write("hello alex!")

    def dataReceived(self, data):
        "As soon as any data is received, write it back."
        print("Server said:", data)
        self.transport.loseConnection()  #自动调用下面的connectionLost,再调用clientConnectionLost

    def connectionLost(self, reason):
        print("connection lost")


class EchoFactory(protocol.ClientFactory):
    protocol = EchoClient   #相当于handle方法
    #连接失败，则调用下面方法
    def clientConnectionFailed(self, connector, reason):
        print("Connection failed - goodbye!")
        reactor.stop()    #连接关闭
    #连接过程中断开，则调用下面方法
    def clientConnectionLost(self, connector, reason):
        print("Connection lost - goodbye!")
        reactor.stop()


# this connects the protocol to a server running on port 8000
def main():
    f = EchoFactory()
    reactor.connectTCP("localhost", 9000, f)
    reactor.run()


# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()
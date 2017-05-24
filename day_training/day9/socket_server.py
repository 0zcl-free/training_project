
import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):  #继承

    def handle(self):  #和客户端所有的交互都在handle()完成,执行结束客户端就断开
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address[0]))
                print(self.data)
                self.request.sendall(self.data.upper())
            except ConnectionResetError as e:
                print("客户端断开",e)
                break


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    #每来一个请求，服务端就开启一个新的线程
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)  #实例化
    server.serve_forever()
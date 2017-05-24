import pika
import uuid


class FibonacciRpcClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

        self.channel = self.connection.channel()
        #随机建立一个queue，为了监听返回的结果
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue   ##队列名

        self.channel.basic_consume(self.on_response,  #一接收客户端发来的指令就调用回调函数on_response
                                   no_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):  #回调
        #每条指令执行的速度可能不一样，指令１比指令２先发送，但可能指令２的执行结果比指令１先返回到客户端，
        #此时如果没有下面的判断，客户端就会把指令２的结果误认为指令１执行的结果
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None    ##指令执行后返回的消息
        self.corr_id = str(uuid.uuid4())   ##可用来标识指令(顺序)
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue', #client发送指令，发到rpc_queue
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue, #将指令执行结果返回到reply_to队列
                                       correlation_id=self.corr_id,
                                   ),
                                   body=str(n))
        while self.response is None:
            self.connection.process_data_events() #去queue接收数据(不阻塞)
        return int(self.response)


fibonacci_rpc = FibonacciRpcClient()

print(" [x] Requesting fib(30)")
response = fibonacci_rpc.call(30)
print(" [.] Got %r" % response)
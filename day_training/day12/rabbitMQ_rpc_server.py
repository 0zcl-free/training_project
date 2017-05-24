import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='rpc_queue')


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def on_request(ch, method, props, body):
    n = int(body)

    print(" [.] fib(%s)" % n)
    response = fib(n)  #从客户端收到的消息

    ch.basic_publish(exchange='',   ##服务端发送返回的数据到props.reply_to队列(客户端发送指令时声明)
                     routing_key=props.reply_to,  #correlation_id (随机数)每条指令都有随机独立的标识符
                     properties=pika.BasicProperties(correlation_id= \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)  #客户端持久化


channel.basic_qos(prefetch_count=1)  #公平分发
channel.basic_consume(on_request,    #一接收到消息就调用on_request
                      queue='rpc_queue')

print(" [x] Awaiting RPC requests")
channel.start_consuming()
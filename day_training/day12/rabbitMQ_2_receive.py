import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# You may ask why we declare the queue again ‒ we have already declared it in our previous code.
# We could avoid that if we were sure that the queue already exists. For example if send.py program
# was run before. But we're not yet sure which program to run first. In such cases it's a good
# practice to repeat declaring the queue in both programs.
#channel.queue_declare(queue='task_q',durable=True)   #声明队列，保证程序不出错


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    #ch.basic_ack(delivery_tag=method.delivery_tag)



channel.basic_consume(callback,    #回调函数，
                      queue='task_q',
                      no_ack=True,
                      )  #消费完毕后向服务端发送一个确认
channel.basic_qos(prefetch_count=1)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
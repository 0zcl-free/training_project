import pika
#连上rabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()  #生成管道，在管道里跑不同的队列

# 声明queue
#channel.queue_declare(queue='task_q',durable=True)

# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
#向队列里发数据
channel.basic_publish(exchange='',    #先把数据发给exchange交换器,exchage再发给相应队列
                      routing_key='task_q',  #向"hello'队列发数据
                      body='Hello World34345', #发的消息
                      properties=pika.BasicProperties(
                          delivery_mode=2,
                      )
                      )
print(" [x] Sent 'Hello World!'")
connection.close()
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',  #defining exchange as logs - logs are pushed from app to exchange and exchange will push to all queue
                         type='fanout')

result = channel.queue_declare(exclusive=True)     #declaring a random queue and exclusive=true flag will delete it after we close the connection
queue_name = result.method.queue

channel.queue_bind(exchange='logs',
                   queue=queue_name)          #we already created a queue, now binding is use to tell the exchange to send messages to our queue

print('[*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):  #receiving messages from exchange works by subscribing a callback function [pika library]
    print(body)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)         #telling rabbitmq that callback should consume messages from exchange

channel.start_consuming()    #never-ending loop that waits for data and runs callback whenever necessary

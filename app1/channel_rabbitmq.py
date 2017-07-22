import pika  #imported a python client recommended for using rabbitmq

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))  #connection to localhost
channel = connection.channel()  #connection via making a channel

channel.exchange_declare(exchange='logs',
                         type='fanout')    #declaring queue, fanout exchange will broadcasts all the messages it receives to all known queues.

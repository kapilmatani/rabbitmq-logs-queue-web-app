from flask import Flask
import flask
import pika
import threading
import subprocess
import time

app = Flask(__name__)
@app.route('/')
def index():
    def inner():
        proc = subprocess.Popen(
            ['tail -f log_file.txt'],
            shell=True,
            stdout=subprocess.PIPE
        )

        for line in iter(proc.stdout.readline,''):
            time.sleep(1)
            yield str(line.rstrip()) + '<br/>\n'

    return flask.Response(inner(), mimetype='text/html')

def call_logs():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='logs',
                             type='fanout')

    result = channel.queue_declare(queue='rabbit_queue')
    queue_name = result.method.queue

    channel.queue_bind(exchange='logs',
                       queue=queue_name)

    print('Application Started')

    def callback(ch, method, properties, body):
        print(body)
        with open("log_file.txt", "a") as myfile:
            myfile.write(str(body)+"\n")


    channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

    channel.start_consuming()

def run_flask():
    global app
    app.run(host='0.0.0.0',port='3000')


if __name__ == '__main__':
    t1=threading.Thread(target=call_logs)
    t1.start()
    t2=threading.Thread(target=run_flask)
    t2.start()
    t1.join()
    t2.join()

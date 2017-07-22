from flask import Flask
from flask import render_template
from flask import request
from channel_rabbitmq import channel,connection
import time
from flask import redirect
from datetime import datetime

def log_rabbitmq(log):
    channel.basic_publish(exchange='logs',
                          routing_key='',
                          body=log)
    return

def log_format(loglevel,message):
    return str(datetime.now())[:-3] + ' [' + loglevel + '] ContactPageService - ' + message

app = Flask(__name__)

@app.route('/')
def index():
    log_rabbitmq(log_format("INFO", "User landed on Contact Us Page"))
    return render_template('contact_us.html')
    
@app.route('/login', methods=['POST','GET'])
def login():
    error = None
    if request.method == 'POST':
	log_rabbitmq(log_format("INFO", "User entered Full name: %r" % str(request.form['name'])))	
	log_rabbitmq(log_format("INFO", "User entered Email: %r" % str(request.form['email'])))
        
	mobile = str(request.form['mobile'])
 	if len(mobile)!=10 or not mobile.isdigit():
	    print 'hi'
	    log_rabbitmq(log_format("ERROR", "User entered Invalid Mobile no: %r" % mobile))
	else:
	    log_rabbitmq(log_format("INFO", "User entered Mobile no: %r" % str(request.form['mobile'])))	
	
	log_rabbitmq(log_format("INFO", "User entered Reviews: %r" % str(request.form['reviews'])))
	log_rabbitmq(log_format("INFO", "User Successfully submitted the contact form."))

	return render_template('submit.html')

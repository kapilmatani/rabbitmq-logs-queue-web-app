from flask import Flask
from flask import render_template
from flask import request
from channel_rabbitmq import channel,connection
import time
from flask import redirect
from datetime import datetime

def log_rabbitmq(log):                      # python function to publish logs whenever called to a exchange named 'logs'
    channel.basic_publish(exchange='logs',  # exchange program will push logs to a exchange named logs  
                          routing_key='',
                          body=log)
    return

def log_format(loglevel,message):           #python function to return the specified logformat given message input
    return str(datetime.now())[:-3] + ' [' + loglevel + '] ContactPageService - ' + message

app = Flask(__name__)  #initialized flask app

@app.route('/') #default route of flask app i.e. index page
def index():
    log_rabbitmq(log_format("INFO", "User landed on Contact Us Page")) #publishing logs when user landed on contact page.
    return render_template('contact_us.html')  #returning rendered html page
    
@app.route('/login', methods=['POST','GET'])   #user will be redirected to /login while submitting contact form.
def login():
    error = None
    if request.method == 'POST':   #handling post request
	log_rabbitmq(log_format("INFO", "User entered Full name: %r" % str(request.form['name'])))   #adding whatever user entered in logs
	log_rabbitmq(log_format("INFO", "User entered Email: %r" % str(request.form['email'])))
        
	mobile = str(request.form['mobile'])
 	if len(mobile)!=10 or not mobile.isdigit():        #checking mobile no format 
	    log_rabbitmq(log_format("ERROR", "User entered Invalid Mobile no: %r" % mobile))
	else:
	    log_rabbitmq(log_format("INFO", "User entered Mobile no: %r" % str(request.form['mobile'])))	
	
	log_rabbitmq(log_format("INFO", "User entered Reviews: %r" % str(request.form['reviews'])))
	log_rabbitmq(log_format("INFO", "User Successfully submitted the contact form."))

	return render_template('submit.html')  #returning another template

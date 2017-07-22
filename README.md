This project mainly concentrate on building a web app that generate logs and pushes to a rabbitmq queue and another python script to fetches logs from that queue.<br />

Requirements to run the project:<br />
&nbsp; 1. Install rabbitmq-server - https://www.rabbitmq.com/download.html <br />
&nbsp; 2. Start and Stop server by using commands: sudo service rabbitmq-server start or sudo service rabbitmq-server stop <br />
&nbsp; 3. Install flask - http://flask.pocoo.org/docs/0.12/installation/ <br />

How to run the project: <br />
&nbsp; 1. sudo service rabbitmq-server start <br />
&nbsp; 2. go to directory rabbitmq-logs-queue-web-app/app1/ <br />
&nbsp; 3. export FLASK_APP=flask_app.py <br />
&nbsp; 4. flask run <br />
&nbsp; 5. Open your browser and go to: http://localhost:5000 <br />
&nbsp; 6. For checking logs on terminal go to directory rabbitmq-logs-queue-web-app/app2/ <br />

```
python receive_logs.py                               #for checking logs on terminal.
python receive_logs.py > log_file.txt                #to output all logs to a file.
Submit the contact form on browser and check logs.
```

Happy Coding!!

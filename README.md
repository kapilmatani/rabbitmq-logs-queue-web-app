This project mainly concentrate on building a web app that generate logs and pushes to a rabbitmq queue and another web app to fetch logs from the queue via exchange. <br />

Requirements to run the project:<br />
&nbsp; 1. Install rabbitmq-server - https://www.rabbitmq.com/download.html <br />
&nbsp; 2. Start and Stop server by using commands: sudo service rabbitmq-server start or sudo service rabbitmq-server stop <br />
&nbsp; 3. Install flask - http://flask.pocoo.org/docs/0.12/installation/ <br />

How to run the project: <br />
&nbsp; 1. sudo service rabbitmq-server start <br />
&nbsp; 2. go to directory rabbitmq-logs-queue-web-app/app1/ <br />
&nbsp; 3. export FLASK_APP=flask_app.py <br />
&nbsp; 4. flask run -h 0.0.0.0 -p 5000<br />
&nbsp; 5. Open your browser and go to: http://0.0.0.0:5000 <br />
&nbsp; 6. For running another app which shows logs in browser:
&nbsp; 7. go to directory rabbitmq-logs-web-app/app2/ <br />
&nbsp; 8. python3 flask_receive.py <br />
&nbsp; 9. open your browser and go to: http://0.0.0.0:3000 <br />

```
Submit the contact form on browser and check logs.
Log file will be generated in app2.
```

Happy Coding!!

This project mainly concentrate on building a web app that generate logs and pushes to a rabbitmq queue and another python script to fetches logs from that queue.<br />

Requirements to run the project:<br />
i. Install rabbitmq-server - https://www.rabbitmq.com/download.html <br />
ii. Start and Stop server by using commands: sudo service rabbitmq-server start or sudo service rabbitmq-server stop <br />
iii. Install flask - http://flask.pocoo.org/docs/0.12/installation/ <br />

How to run the project: <br />
i. sudo service rabbitmq-server start <br />
ii. go to directory rabbitmq-logs-queue-web-app/app1/ <br />
iii. export FLASK_APP=flask_app.py <br />
iv. flask run <br />
v. Open your browser and go to: http://localhost:5000 <br />
vi. For checking logs on terminal go to directory rabbitmq-logs-queue-web-app/app2/ <br />
vii. python receive_logs.py  #for checking logs on terminal. <br />
     python receive_logs.py > log_file.txt #to output all logs to a file. <br />
viii. Submit the contact form on the browser and check logs. <br />

Happy Coding!!

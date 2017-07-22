This project mainly concentrate on building a web app that generate logs and pushes to a rabbitmq queue and another python script to fetches logs from that queue.

Requirements to run the project:
i. Install rabbitmq-server - https://www.rabbitmq.com/download.html
ii. Start and Stop server by using commands: sudo service rabbitmq-server start or sudo service rabbitmq-server stop
iii. Install flask - http://flask.pocoo.org/docs/0.12/installation/

How to run the project:
i. sudo service rabbitmq-server start
ii. go to directory rabbitmq-logs-queue-web-app/app1/
iii. export FLASK_APP=flask_app.py
iv. flask run
v. Open your browser and go to: http://localhost:5000
vi. For checking logs on terminal go to directory rabbitmq-logs-queue-web-app/app2/
vii. python receive_logs.py  #for checking logs on terminal.
     python receive_logs.py > log_file.txt #to output all logs to a file.
viii. Submit the contact form on the browser and check logs.

Happy Coding!!

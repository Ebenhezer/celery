This application uses celery to create background tasks and quick when done. 

Ensure that RabbitMQ is installed. 
Use the requirements.txt file to install the required packages

Run the following command to start up the worker. 
celery -A tasks worker -l info -P eventlet

Then run the test.py app. 
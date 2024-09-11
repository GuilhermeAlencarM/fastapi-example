from dotenv import load_dotenv
from celery import Celery

import os

load_dotenv()

user = os.getenv('RABBITMQ_DEFAULT_USER')
password = os.getenv('RABBITMQ_DEFAULT_PASS')
host = os.getenv('RABBITMQ_DEFAULT_HOST')
port = os.getenv('RABBITMQ_DEFAULT_PORT')

broker_url = f'amqp://{user}:{password}@{host}:{port}//'

app = Celery(
    'celery_app',
    broker=broker_url,
    backend='rpc://',
    include=['celery_app.tasks']
)

app.conf.update(
    result_expires=3600,
)

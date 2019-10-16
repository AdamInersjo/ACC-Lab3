from celery import Celery
from parser import parse_data

# celery_app = Celery('tasks', backend='redis://localhost', broker='redis://localhost:6379')
celery_app = Celery('tasks', backend='rpc://', broker='amqp://localhost')

@celery_app.task
def count_words(words):
    return parse_data(words)
from math import sqrt
from celery_app import app

@app.task
def square_root(value):
    return sqrt(value)

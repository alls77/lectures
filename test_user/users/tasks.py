from math import sqrt
import datetime
from myproj.celery_app import app
from users.models import Users
import datetime

@app.task(name="square_root")
def square_root(value):
    return sqrt(value)


@app.task(name="deactivate_user")
def deactivate_user():
    inactive_period = datetime.datetime.now() - datetime.timedelta(days=30)
    users = Users.objects.filter(user__last_login__lte=inactive_period)
    for user in users:
        user.is_active = False
        user.save()

from celery_app import app

def manage_sqrt_task(value):
    result = app.send_task('tasks.square_root', args=(value,))
    print(result.ready())
    print(result.ready())
    print(result.get(timeout=2))

manage_sqrt_task(4)

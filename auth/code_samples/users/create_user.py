"""
>>> from django.contrib.auth.models import User
>>> user = User.objects.create_user('akimov_mike', 'akimov@light-it.net', 'mysecretpassword')

# At this point, user is a User object that has already been saved
# to the database. You can continue to change its attributes
# if you want to change other fields.
>>> user.last_name = 'New'
>>> user.save()
"""
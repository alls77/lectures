from django.contrib.auth import authenticate
user = authenticate(username='akimov_mike', password='123qwe')
if user is not None:
    # the password verified for the user
    print("User is valid, active and authenticated")
else:
    # the authentication system was unable to verify the username and password
    print("The username and password were incorrect.")



"""
Request

if request.user.is_authenticated:
    # Do something for authenticated users.
    ...
else:
    # Do something for anonymous users.
    …

"""

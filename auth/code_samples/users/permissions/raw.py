from django.conf import settings
from django.shortcuts import redirect, render


def my_view(request):
    if not request.user.is_authenticated():
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        # or just show an error
        # return render(request, 'myapp/login_error.html')
    # further logic


from django.contrib.auth.decorators import login_required


@login_required
# @login_required(login_url='some/url/login')
def my_view(request):
    pass


"""

test.com/product/2

test.com/login?next=product/2

"""

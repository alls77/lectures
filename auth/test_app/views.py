from django.http import HttpResponse
from django.contrib.auth import authenticate

from .models import Comment, Member


def post_comment(request, new_comment):
    """ 1st example """
    has_commented = request.session.get('has_commented', False)
    if has_commented:
        return HttpResponse("You've already commented.")
    c = Comment(comment=new_comment)
    c.save()
    request.session['has_commented'] = True
    return HttpResponse('Thanks for your comment!')


def login(request):
    """ 2nd example """
    m = Member.objects.get(username=request.POST['username'])
    if m.password == request.POST['password']:
        request.session['member_id'] = m.id
        return HttpResponse("You're logged in.")
    else:
        return HttpResponse("Your username and password didn't match.")


def logout(request):
    """ 3rd example """
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")

def auth(request):
    user = authenticate(username='name', password='ali4a208')
    if user is not None:
        return HttpResponse('user is valid')
    else:
        return HttpResponse('user were incorrect')
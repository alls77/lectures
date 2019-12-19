import logging
import json

from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, View

from .forms import RegistrationForm, ProfileForm, AuthForm
from .models import Users
from myproj.celery_app import app
from users.tasks import deactivate_user

logger = logging.getLogger('custom_logger')

def get_current_user(request):
    return render(request, 'users/loggedin.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/index/')

def block_login_page(request):
    if request.user.is_authenticated:
        logger.debug("User %s is authenticated", request.user)
        return HttpResponseRedirect('/index/')
    else:
        logger.info("User is not authenticated")
        return LoginView(**{"request": request, "template_name":'users/login.html',
                            "authentication_form": AuthForm}).post(request)


def register_user(request):
    if request.POST:
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            logger.debug("New user registered.")
            form.save()
            return HttpResponseRedirect(reverse_lazy('index:index'))
        else:
            return render(request, 'users/registration.html', context={
                'form': form
            })
    else:
        return render(request, 'users/registration.html', context={
            'form': RegistrationForm()
        })


@login_required(login_url='/index/login/')
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES,
                              instance=request.user)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('index:index'))
        else:
            return render(request, 'users/profile.html', context={
                'form': form
            })
    else:
        return render(request, 'users/profile.html', context={
            'form': ProfileForm(instance=request.user),
        })


class UsersView(ListView):
    template_name = 'users/index.html'
    context_object_name = 'users_list'
    model = Users

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(object_list=object_list, **kwargs)
        logger.debug("context: %s", context_data['page_obj'])
        result = app.send_task('square_root', args=(4,))
        print(result.ready())
        print(result.ready())
        print(result.get(timeout=5))
        # result = deactivate_user.apply_async()
        # print(result.ready())
        return context_data


class Log(View):
    def post(self, request):
        print (request.POST.get('log', False))
        return render(request, 'users/loggedin.html')

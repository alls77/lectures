from django.urls import path, include

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
]


"""
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('change-password/', auth_views.PasswordChangeView.as_view()),
]
"""

"""
urlpatterns = [
    path(
        'change-password/', 
        auth_views.PasswordChangeView.as_view(template_name='change-password.html'),
    ),
]

"""



"""
accounts/login/ [name='login']
accounts/logout/ [name='logout']
accounts/password_change/ [name='password_change']
accounts/password_change/done/ [name='password_change_done']
accounts/password_reset/ [name='password_reset']
accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/ [name='password_reset_complete']
"""


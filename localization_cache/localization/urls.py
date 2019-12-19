from django.urls import path

from localization.views import first, date_view

urlpatterns = [
    path('', first),
    path('date/', date_view),

]

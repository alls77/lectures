from django.contrib import admin
from django.urls import path, include
from django.views.generic import View, TemplateView, RedirectView

from . import views

app_name = 'book'
urlpatterns = [
    # path('', TemplateView.as_view(template_name='book/index.html'))#for static pages
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailsView.as_view(), name='detail')
]

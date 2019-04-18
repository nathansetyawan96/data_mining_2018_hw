from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='apbuster_website'),
    path('test', views.test, name='test')
]

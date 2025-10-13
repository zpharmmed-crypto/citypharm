from django.urls import path
from . import views

urlpatterns = [
    path('', views.branches_list, name='branches_list'),
]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContestView.as_view(), name='contest'),
]
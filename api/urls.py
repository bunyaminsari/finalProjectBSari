# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # URL for the index page
    path('query/', views.query, name='query'),
    path('accounts/profile/', views.profile_view, name='profile'),

]

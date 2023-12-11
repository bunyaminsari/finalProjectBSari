# myapp/urls.py

from django.urls import path
from . import views
from .views import ApiLoginView

urlpatterns = [
    path('', views.index, name='index'),  # URL for the index page
    path('query/', views.query, name='query'),
    path('accounts/profile/', views.profile_view, name='profile'),  # Default auth paths from Django.
    path('accounts/login/', ApiLoginView.as_view(), name='login'),
    path('accounts/logout/', views.logout, name='logout'),  # Default auth paths from Django.
    path('signup/', views.signup, name='signup'),


]

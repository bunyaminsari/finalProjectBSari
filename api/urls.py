# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # URL for the index page
    path('detail/<int:item_id>/', views.detail, name='detail'),  # URL for item detail with its ID
    path('query/', views.query, name='query'),
]

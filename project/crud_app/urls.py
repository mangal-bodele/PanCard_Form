from django.urls import path
from .views import create_pan,show_pan,delete_pan,update_pan
urlpatterns = [
    path('create/',create_pan,name='create_url'),
    path('show/',show_pan,name='show_url'),
    path('update/<int:pk>/',update_pan,name='update_url'),
    path('delete/<int:pk>/',delete_pan,name='delete_url')
]
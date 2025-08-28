from django.urls import path
from . import views

#Url configuration
urlpatterns = [
    #path('main', )
    path('hello/', views.say_hello, name='hello')
]

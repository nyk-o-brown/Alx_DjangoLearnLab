from django.urls import path
from . import views
from .views import list_books
from django.views.generic.detail import DetailView
from .views import UserLoginView, UserLogoutView, register
from .views import list_books
from django.urls import path
from .views import CustomLoginView, CustomLogoutView, register, list_books
from . import views




urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('books/', list_books, name='list_books'),
]
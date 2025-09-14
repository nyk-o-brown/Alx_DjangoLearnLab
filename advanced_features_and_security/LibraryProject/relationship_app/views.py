from django.shortcuts import render
from .models import Book, Library, UserProfile, CustomUser
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseForbidden
from django import forms
from django.contrib.auth.forms import UserCreationForm

# Custom Registration Form for CustomUser
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    date_of_birth = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    profile_photo = forms.ImageField(required=False)
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'date_of_birth', 'profile_photo', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.date_of_birth = self.cleaned_data['date_of_birth']
        user.profile_photo = self.cleaned_data['profile_photo']
        if commit:
            user.save()
        return user




def list_books(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'




class UserLoginView(LoginView):
    template_name = 'relationship_app/login.html'
    redirect_authenticated_user = True

class UserLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Role-based access control functions
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == 'Member'

# Role-based views
@user_passes_test(is_admin)
def admin_view(request):
    context = {
        'user': request.user,
        'role': request.user.profile.role,
        'books_count': Book.objects.count(),
        'libraries_count': Library.objects.count(),
        'users_count': UserProfile.objects.count(),
    }
    return render(request, 'relationship_app/admin_view.html', context)

@user_passes_test(is_librarian)
def librarian_view(request):
    context = {
        'user': request.user,
        'role': request.user.profile.role,
        'books': Book.objects.all()[:10],  # Show recent books
        'libraries': Library.objects.all(),
    }
    return render(request, 'relationship_app/librarian_view.html', context)

@user_passes_test(is_member)
def member_view(request):
    context = {
        'user': request.user,
        'role': request.user.profile.role,
        'books': Book.objects.all(),
        'libraries': Library.objects.all(),
    }
    return render(request, 'relationship_app/member_view.html', context)
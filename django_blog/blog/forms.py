from django import forms
from .models import Post
from .models import Comment
from taggit.forms import TagWidget 

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'tags': TagWidget()(attrs={'placeholder': 'Add tags separated by commas'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your comment...'})
        }        

from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'content_md', 'is_published']
        widgets = {
            'content_md': forms.Textarea(attrs={'rows': 20}),
        }

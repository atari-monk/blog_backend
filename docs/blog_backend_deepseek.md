# Blog Backend Design Document

## Overview

This document outlines the design and implementation steps for creating a blog backend using Django. The initial focus will be on creating CRUD (Create, Read, Update, Delete) functionality for blog posts stored in Markdown format.

## Project Structure

1. **Project Name**: blog_backend (already created)
2. **App Name**: `posts` (to handle blog post functionality)

## Implementation Steps

### 1. Create the Posts App

```bash
python manage.py startapp posts
```

### 2. Define the Post Model

File: `posts/models.py`

```python
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
import markdown

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content_md = models.TextField()  # Markdown content
    content_html = models.TextField(editable=False)  # HTML rendered version
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)
    is_published = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Convert markdown to HTML before saving
        self.content_html = markdown.markdown(self.content_md)
        if self.is_published and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
```

### 3. Install Required Packages

```bash
pip install markdown
```

### 4. Update Settings

File: `blog_backend/settings.py`

```python
INSTALLED_APPS = [
    ...
    'posts.apps.PostsConfig',
]
```

### 5. Create and Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Admin Interface

File: `posts/admin.py`

```python
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'is_published')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'content_md')
    prepopulated_fields = {'slug': ('title',)}
```

### 7. Create Serializers (for API)

File: `posts/serializers.py`

```python
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'content_md', 'content_html',
                 'author', 'created_at', 'updated_at', 'published_at', 'is_published']
        read_only_fields = ['content_html', 'author', 'created_at', 'updated_at']
```

### 8. Create Views (API Views)

File: `posts/views.py`

```python
from rest_framework import viewsets, permissions
from .models import Post
from .serializers import PostSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
```

### 9. Set Up URLs

File: `posts/urls.py`

```python
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='post')

urlpatterns = router.urls
```

File: `blog_backend/urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('posts.urls')),
]
```

### 10. Test the Implementation

1. Create superuser:

```bash
python manage.py createsuperuser
```

2. Run development server:

```bash
python manage.py runserver
```

3. Access:

- Admin interface: http://localhost:8000/admin/
- API endpoints: http://localhost:8000/api/posts/

## Next Steps (Future Enhancements)

1. Add user authentication API endpoints
2. Implement tags/categories for posts
3. Add comments functionality
4. Implement image uploads for posts
5. Add search functionality
6. Implement caching for better performance
7. Add pagination to API
8. Implement proper permission classes for different actions

Would you like me to elaborate on any of these steps or suggest any modifications to the initial design?

Alright! You're off to a solid start with your Django project `blog_backend`. Let's shape this into a clean design doc so you have a roadmap. I’ll help you break it down into clear steps for your blog CRUD backend with Markdown-based blog posts.

---

# 📘 **Design Document: blog_backend**

## 🗓️ Date

**2025-04-05**

## 📌 Purpose

Learning Django by building a backend for a blog. The goal is to support CRUD (Create, Read, Update, Delete) operations for blog posts, where each post is written in **Markdown**.

---

## 📦 Project Overview

- **Project Name**: `blog_backend`
- **Primary App**: `blog` (to be created)
- **Main Feature**: CRUD for blog posts stored as Markdown

---

## ✅ Initial Setup (Already Done)

- ✅ Django project created: `blog_backend`

---

## 🛠️ Next Steps

### 1. **Create App**

```bash
python manage.py startapp blog
```

### 2. **Define Blog Post Model**

We'll use a `Post` model. For now, keep it simple:

```python
# blog/models.py

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()  # Markdown content
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```

> Later, we can render `content` into HTML using a Markdown parser like `markdown2` or `mistune`.

### 3. **Register App**

In `settings.py`, add `'blog'` to `INSTALLED_APPS`.

---

## 🔁 CRUD Flow

### Views (Options)

- Use **Django generic class-based views** or **DRF (Django REST Framework)** if you want an API-style backend.
- For now, if you're learning, keep it vanilla Django.

### Routes (`urls.py`)

```python
# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<slug:slug>/edit/', views.post_edit, name='post_edit'),
    path('post/<slug:slug>/delete/', views.post_delete, name='post_delete'),
]
```

### Sample View (Function-based)

```python
# blog/views.py

from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})
```

---

## 🧪 Admin Access

Register model in admin:

```python
# blog/admin.py

from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

---

## 📝 Templates (Later Step)

Keep your Markdown files as content, or just store them in DB for now. You can parse them in the view like this:

```python
import markdown2

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    html_content = markdown2.markdown(post.content)
    return render(request, 'blog/post_detail.html', {'post': post, 'html_content': html_content})
```

---

## 🧱 Folder Structure (after setup)

```
blog_backend/
├── blog/
│   ├── migrations/
│   ├── templates/
│   │   └── blog/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── blog_backend/
│   ├── settings.py
│   └── urls.py
└── manage.py
```

---

## 🔮 Later Ideas

- Add Markdown editor in admin with live preview.
- Add tags or categories.
- Add user auth for post creation.
- Add comments feature.

---

Want me to generate the model and views as Python code scripts for copy-pasting? Or make it DRF-style for a modern API approach?

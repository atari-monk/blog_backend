# Django Blog Post Model Documentation

## Define the Post Model

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
    content_md = models.TextField()
    content_html = models.TextField(editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)
    is_published = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.content_html = markdown.markdown(self.content_md)
        if self.is_published and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
```

## Install Required Packages

```bash
pip install markdown
```

## Create and Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## Overview

This document explains the `Post` model in a Django-based blog application. Even if you're not familiar with Django, this guide will help you understand how blog posts are structured and managed in the database.

## Model Components

### 1. Basic Post Information

- **title**: The title of the blog post (maximum 200 characters)
- **slug**: A URL-friendly version of the title (unique for each post)
  - Example: "My First Post" becomes "my-first-post" in URLs
- **author**: The user who created the post (links to Django's user system)

### 2. Content Handling

- **content_md**: The post content written in Markdown format
  - Markdown is a simple text formatting syntax (like `# Heading` or `**bold**`)
- **content_html**: Automatically generated HTML version of the content
  - This is created from the Markdown when the post is saved

### 3. Timestamps

- **created_at**: When the post was first created (auto-set)
- **updated_at**: When the post was last modified (auto-updated)
- **published_at**: When the post was published (can be blank)

### 4. Publication Status

- **is_published**: Whether the post is public (defaults to False/draft)

## Automatic Behaviors

1. **Markdown Conversion**:

   - When a post is saved, the system automatically converts the Markdown content to HTML
   - Example: `**bold**` becomes `<strong>bold</strong>`

2. **Publication Date**:
   - When a post is marked as published (`is_published=True`) and doesn't have a publication date yet, it automatically sets the current time as the publication date

## Technical Details for Developers

### Field Types

- **CharField**: For short text (with max_length)
- **SlugField**: For URL-friendly strings
- **TextField**: For long text content
- **ForeignKey**: Links to another model (User in this case)
- **DateTimeField**: Stores date and time
- **BooleanField**: True/False value

### Special Attributes

- `auto_now_add=True`: Sets field to current time when first created
- `auto_now=True`: Updates field to current time on each save
- `editable=False`: Field can't be edited in admin forms
- `null=True, blank=True`: Field can be empty in database/forms

### Methods

- `save()`: Custom logic that runs before saving
- `__str__()`: How the post appears in admin/database listings

## Example Usage

1. **Creating a post**:

   ```python
   new_post = Post(
       title="My First Post",
       slug="my-first-post",
       content_md="# Welcome\nThis is my first blog post!",
       author=some_user,
       is_published=True
   )
   new_post.save()
   ```

2. **Resulting HTML**:
   ```html
   <h1>Welcome</h1>
   <p>This is my first blog post!</p>
   ```

This model provides a complete solution for managing blog posts with Markdown support, publication controls, and automatic timestamp tracking.

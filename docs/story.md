# Story of blog_backend

Leanring django by generating blog_backend with python scripts.

## 2025-04-05

## Design Document

Need for design document to speciffy setps i need  
I want blog post to be a md, just post for now

- [Design Document Chatgpt](blog_backend_chatgpt.md)
- [Design Document Deepseek](blog_backend_deepseek.md)

## Generate Project

Project Name: blog_backend

```sh
python -m django_scripts.generate_project C:\atari-monk\code blog_backend --gitignore-template C:\atari-monk\code\py-scripting\data\django_gitignore.txt
```

## Generate App

App Name: posts

```sh
python -m django_scripts.generate_app -p blog_backend -a posts -r C:\atari-monk\code\blog_backend
```

## Generate Model

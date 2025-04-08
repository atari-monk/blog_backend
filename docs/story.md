# Story of blog_backend

Leanring django by generating blog_backend with python scripts.

## Generate Project blog_backend, 2025-04-05

```sh
python -m django_scripts.generate_project C:\atari-monk\code blog_backend --gitignore-template C:\atari-monk\code\py-scripting\data\django_gitignore.txt
```

## Generate App posts

```sh
python -m django_scripts.generate_app -p blog_backend -a posts -r C:\atari-monk\code\blog_backend
```

[Concept of django app](django_app.md)

## Generate [Post Model](post_model.md), 2025-04-06

## Generate [Views, URLs, and templates for Posts](post_views.md)

Implemented and testing.  
Getting login error saving post form.

## Generate [Login](login.md), 2025-04-07

## [Basic cli commands](cli.md), 2025-04-08

## [Removing posts](post_delete.md)

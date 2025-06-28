# django.md

## About
**Name:** Django (named after Django Reinhardt, a famous jazz guitarist, reflecting the creators' admiration for his improvisational skill and creativity)

**Created:** Released in 2005 by Adrian Holovaty and Simon Willison, Django was created to help developers build web applications quickly and with less code. Its purpose is to provide a high-level Python web framework that encourages rapid development and clean, pragmatic design.

**Similar Technologies:** Flask, FastAPI, Ruby on Rails, Laravel, Express.js, Spring

**Plain Language Definition:**
Django is a toolkit for building websites and web apps using Python. It handles much of the hassle of web development, so you can focus on writing your app instead of reinventing the wheel.

---

## Project Setup

```bash
django-admin startproject myproject  # Create new project
cd myproject
python manage.py startapp myapp     # Create new app
python manage.py runserver           # Start development server
python manage.py runserver 8080     # Run on specific port
```

## Database Operations

```bash
python manage.py makemigrations     # Create migration files
python manage.py migrate            # Apply migrations
python manage.py showmigrations     # Show migration status
python manage.py sqlmigrate app 0001 # Show SQL for migration
python manage.py createsuperuser    # Create admin user
```

## Models

```python
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published = models.BooleanField(default=False)
```

## Views

```python
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.generic import ListView

def post_list(request):
    posts = Post.objects.filter(published=True)
    return render(request, 'posts/list.html', {'posts': posts})

class PostListView(ListView):
    model = Post
    template_name = 'posts/list.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        return Post.objects.filter(published=True)
```

## URLs

```python
# urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('posts/', include('posts.urls')),
    path('api/posts/', views.PostListView.as_view()),
]
```

## Management Commands

```bash
python manage.py shell              # Django shell
python manage.py collectstatic      # Collect static files
python manage.py test               # Run tests
python manage.py loaddata fixture   # Load fixture data
python manage.py dumpdata app       # Export data
```
# Online Food App

### Basic Setup

```python
> mkdir online_food
> cd online_food
> python3 -m venv venv
> source venv/bin/activate
> deactivate

> pip list || pip freeze
> python -m pip install django
> python -m django --version
# Create Project
> django-admin startproject project_name
# Create App
python manage.py startapp blog

# Run the project
> python manage.py runserver
# To use specific setting and port
> python manage.py runserver 127.0.0.1:8001 --settings=mysite.settings

# Admin Panel Setup
python manage.py migrate
python manage.py createsuperuser
python manage.py makemigrations blog
```

Collect Static files before production

### Problem

### Port Problem

**Error**: That port is already in use.
**Solution**: `sudo lsof -t -i tcp:8000 | xargs kill -9`

### Vs Code HTML Extension

Install djlint using pip and vscode extension then Configure vscode setting file:

```json
"files.associations": {
    "*.tsx": "typescriptreact",
    "**/templates/*/*.html": "django-html",
    "**/templates/*": "django-txt",
    "**/requirements{/**,*}.{txt,in}": "pip-requirements"
  },
  "[html][django-html][handlebars][hbs][mustache][jinja][jinja-html][nj][njk][nunjucks][twig]": {
    "editor.defaultFormatter": "monosans.djlint"
  },
```

## Basics

### MTV (Model-Template-View)

Django follows MTV pattern.

Model: Defines the logical data structure.

Template: Defines the presentation layer.

View: Communicates with the database.

> Django 5 comes with Asynchronous Server Gatewat Interface (ASGI) support.

### Basic CRUD Commands

```python
>>> python manage.py shell
>>> from django.contrib.auth.models import User
>>> from blog.models import Post
>>> user = User.objects.get(username='sandeep')
>>> post = Post(title='Post from shell', slug='post-from-shell', body='Post body', author=user)
>>> post.save()

# Creates the post and commit to db.
>>> Post.object.create()

# Get or create
user, created = User.objects.get_or_create(username='cherry')

# updating
post.title = 'New title'
post.save()

# Retrive
all_posts = Post.objects.all()

# Retrive with filters
Post.objects.filter(title='Who are you?')

# Lookup fields
# __ defines the lookup type
# Other eg. id__exact=1, title__contains='Django', id__in=[1,3]
# author__username__startswith='sa'
Post.objects.filter(id__exact=1)
Post.objects.filter(id=1)

# exclude
Post.objects.filter(publish__year=2024).exclude(title__startswith='why')

# Order by
Post.objects.order_by('title')

# Limiting querysets
Post.objects.all()[:5]
Post.objects.all()[3:6]

# Delete
post = Post.objects.get(id=1)
post.delete()

# Lookups with Q objects.
>>> from django.db.models import Q
>>> starts_why = Q(title__istartswith='why')
>>> starts_who = Q(title__istartswith='who')
>>> Post.objects.filter(starts_who | starts_why)

```

### Templates

Tags: `{% tag %}`
Variables: `{{ var }}`
Filters: `{{ variable|filter }}`

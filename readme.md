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

### Canonical URL

A canonical URL refers to the preferred, absolute URL for a specific resource or object within your application. This is particularly important for Search Engine Optimization (SEO) to prevent duplicate content issues when the same content might be accessible via multiple URLs.

### Sending Email

Sending email is straightforward in Django. We need to have SMTP server or access to an external SMTP server.

**Python Decouple:** Library simplifies the use of envirnment variables in the project. Also facilitates the separation of configuration from code.

Install

`python -m pip install python-decouple`

Create a file inside root dir, named it `.env`

### Tagging

python -m pip install django-taggit

### Retrieving posts by similarity (pg. 116) ❌

### Custom Templates

simple_tag: Processes the given data and returns a string
inclusion_tag: Processes the given data and returns a rendered template

### Markdown Templates Filter

Writing post with Markdown editor
`python -m pip install markdown`

### Adding a sitemap to the site (pg. 134) ❌

### Creating feeds for blog posts (pg. 139) ❌

### Setting up PostgreSQL

**Install docker**

**Install postgres**

`docker pull postgres:16.2`

**Start docker container**

```
docker run --name=blog_db -e POSRGRES_DB=blog -e POSTGRES_USER=blog -e POSTGRES_PASSWORD=Sandeep123@ -p 5432:5432 -d postgres:16.2
```

name: name of the container.

e: environment variable.

d: detach mode, docker runs in a background.

POSTGRES_DB: Name of the PostgreSQL database. If not defined, the value of POSTGRES_USER is used for the database name.

POSTGRES_USER: Used in conjunction with POSTGRES_PASSWORD to define a username and password. The user is created with superuser power.

POSTGRES_PASSWORD: Sets the superuser password for PostgreSQL.

**Install PostgreSQL adapter**

`python -m pip install psycopg==3.1.18` OR `psycopg2-binary`

**Dump exiting data**

We need to download data from SQLite DB.

`python manage.py dumpdata --indent=2 --output=mysite_data.json`

**Switch DB**

```json
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
    }
}
```

**Migrate to new DB**
`python manage.py migrate`

**Load previous data**
`python manage.py loaddata mysite_data.json`

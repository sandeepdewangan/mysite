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

**Error**: That port is already in use.
**Solution**: `sudo lsof -t -i tcp:8000 | xargs kill -9`

## Basics

### MTV (Model-Template-View)

Django follows MTV pattern.

Model: Defines the logical data structure.

Template: Defines the presentation layer.

View: Communicates with the database.

> Django 5 comes with Asynchronous Server Gatewat Interface (ASGI) support.

from django.urls import path
from .import views

app_name = 'blog'

urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),
    path('<int:id>/', views.post_detail, name='post_detail'),
    # if path converters like <int:id>/ is not sufficient,
    # we can use re_path() for complex URL patterns with Regex.
]

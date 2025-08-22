from django.db import models
from django.utils import timezone
from django.db.models.functions import Now

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()

    # As timezone aware format, python generated default time.
    publish = models.DateTimeField(default=timezone.now)

    # DB current date and time, db generated default time.
    # publish = models.DateTimeField(db_default=Now())

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # While return data, sort the data
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title
    
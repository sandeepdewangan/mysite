from django.db import models
from django.utils import timezone
from django.db.models.functions import Now
from django.conf import settings
from django.urls import reverse


# Default manager is the object manager
# Earlier -> Post.objects.all();
# Access -> Post.published.all()
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    class Status(models.TextChoices):
        # > Post.Status.choices
        #     [('DF', 'Draft'), ('PB', 'Published')]
        # > Post.Status.labels
        #     ['Draft', 'Published']
        # > Post.Status.values
        #     ['DF', 'PB']
        # > Post.Status.names
        #     ['DRAFT', 'PUBLISHED']
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date="publish")
    # related_name establishes reverse realtionship from User to Post.
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="blog_posts"
    )
    body = models.TextField()

    # As timezone aware format, python generated default time.
    publish = models.DateTimeField(default=timezone.now)

    # DB current date and time, db generated default time.
    # publish = models.DateTimeField(db_default=Now())

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status, default=Status.DRAFT)

    # Managers
    objects = models.Manager()  # default
    published = PublishedManager()  # custom manager

    # While return data, sort the data
    class Meta:
        ordering = ["-publish"]
        indexes = [
            models.Index(fields=["-publish"]),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "blog:post_detail",
            args=[self.publish.year, self.publish.month, self.publish.day, self.slug],
        )

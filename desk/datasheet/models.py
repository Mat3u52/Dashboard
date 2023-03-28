from django.db import models
from django.utils import timezone


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='certified')


class Guideline(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('certified', 'Certified'),
    )
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # CASCADE: When the referenced object is deleted, also delete the objects that have references to it.
    # when you remove a blog post for instance, you might want to delete comments as well.
    title = models.CharField(max_length=250)
    version = models.CharField(max_length=250, default="0.0")
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    objects = models.Manager() # Default manager
    certified = PublishedManager() # Extraordinary manager
    # python3 manage.py shell
    # from datasheet.models import Guideline
    # Guideline.certified.filter(title__startswith='Trial')

    class Meta:
        ordering = ('-publish_date',)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

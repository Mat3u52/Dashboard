from django.db import models
from django.utils import timezone


class Guideline(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # CASCADE: When the referenced object is deleted, also delete the objects that have references to it.
    # when you remove a blog post for instance, you might want to delete comments as well.
    title = models.CharField(max_length=250)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

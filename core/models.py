from django.db import models


class Gallery(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    author = models.CharField(max_length=100, blank=True, default='')
    page_count = models.IntegerField()

    class Meta:
        ordering = ('created',)

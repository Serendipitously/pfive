from django.db import models


class Gallery(models.Model):
    CATEGORIES = (
        (1, 'Non-H'),
        (2, 'Game CG'),
        (3, 'Doujinshi'),
        (4, 'Manga'),
        (5, 'Artist CG'),
        (6, 'Artist'),
        (7, 'Cosplay'),
        (8, 'Misc')
    )

    gid = models.IntegerField(default=-1)
    token = models.CharField(max_length=30, default='')
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    title_jpn = models.CharField(max_length=100, blank=True, default='')
    category = models.IntegerField(choices=CATEGORIES, default=8)
    filecount = models.IntegerField(default=0)
    expunged = models.BooleanField(default=False)
    # TODO: add tags to this model

    class Meta:
        ordering = ('created',)

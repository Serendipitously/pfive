from django.db import models


class Gallery(models.Model):
    CATEGORIES = (
        (1, 'Doujinshi'),
        (2, 'Manga'),
        (3, 'Game CG'),
        (4, 'Artist CG'),
        (5, 'Western'),
        (6, 'Non-H'),
        (7, 'Image Set'),
        (8, 'Cosplay'),
        (9, 'Asian Porn'),
        (0, 'Misc')
    )

    gid = models.IntegerField(default=-1)
    token = models.CharField(max_length=30, default='')
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    title_jpn = models.CharField(max_length=100, blank=True, default='')
    category = models.IntegerField(choices=CATEGORIES, default=0)
    filecount = models.IntegerField(default=0)
    expunged = models.BooleanField(default=False)
    # TODO: add tags to this model

    class Meta:
        ordering = ('created',)

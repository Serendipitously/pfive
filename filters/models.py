from django.db import models


class Criteria(models.Model):
    CRITERIA_TYPES = (
        ('HI', 'Hard Include'),
        ('SI', 'Soft Include'),
        ('SE', 'Soft Exclude'),
        ('HE', 'Hard Exclude')
    )
    # Wonder if exclude should be SX/HX, because, as exhentai says themselves
    # "The X makes it sound cool"
    type = models.CharField(max_length=2, choices=CRITERIA_TYPES)
    query_param = models.CharField(max_length=100, blank=False)
    weight = models.IntegerField(default=1)

    class Meta:
        ordering = ('type',)


class Filter(models.Model):
    name = models.CharField(max_length=100, blank=True, default=str(id))
    user = models.CharField(max_length=100, blank=True, default='')
    # Max length seems to be something we should standardise for all similar
    # fields with a global variable
    # Arbitrarily using 100 here to match previous work in Gallery.py

    description = models.CharField(max_length=1000, blank=True, default='')
    # description can be longer

    subscribed = models.BooleanField(default=False)

    criteria = models.ManyToManyField(Criteria)
    # Data Model says OTM but OTM does not exist
    # The Django tutorial uses MTM for Pizza/toppings

    class Meta:
        ordering = ('name',)

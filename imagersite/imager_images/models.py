# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings


PHOTO_CAT = [
    ('', 'Portrait'),
    ('', 'Landscape'),
    ('', 'Nature'),
    ('', 'Sport'),
    ('', 'Food'),
    ('', 'Art'),
    ('', 'Fantasy'),
    ('', 'Science Fiction'),
    ('', 'Science'),
    ('', ''),
    ('', ''),
]

US_REGIONS = [
    ('0', 'Hidden'),
    ('1', 'Alaska'),
    ('2', 'Hawaii'),
    ('3', 'Mid-Atlantic'),
    ('4', 'Midwest'),
    ('5', 'New England'),
    # ('ne', 'Northeast'),
    ('6', 'Northwest'),
    ('7', 'Southeast'),
    ('8', 'SouthWest'),
]


@python_2_unicode_compatible
class Albumn(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='albumns',
                             # null=true,
                             )
    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Photo(models.Model):
    title = models.CharField(max_length=30)
    category = models.CharField(max_length=30, choices=PHOTO_CAT)
    location = models.CharField(max_length=30, choices=US_REGIONS)
    image = models.ImageField(upload_to='images/%Y-%m-%d')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='photos',
                             )
    date_uploaded = models.DateField(auto_now=True)
    date_published = models.DateField(auto_now=True)
    date_modified = models.DateField(auto_now=True)
    albumns = models.ManyToManyField(Albumn, related_name='photos')

    def __str__(self):
        return self.title

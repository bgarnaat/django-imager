# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible

PRIVACY = (
    ('private', 'Private'),
    ('shared', 'Shared'),
    ('public', 'Public'),
)

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
    ('3', 'Midwest'),
    ('4', 'Northeast'),
    ('5', 'Northwest'),
    ('6', 'Southeast'),
    ('7', 'SouthWest'),
]


@python_2_unicode_compatible
class Albumn(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='albumns',
    )
    cover = models.ForeignKey(
        'Photo',
        on_delete=models.CASCADE,
        related_name='cover_photo',
        null=True,
        default=None,
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(null=True)
    published = models.CharField(
        max_length=10,
        choices=PRIVACY,
        default='public',
    )

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Photo(models.Model):
    title = models.CharField(max_length=30)
    category = models.CharField(max_length=30, choices=PHOTO_CAT)
    location = models.CharField(max_length=30, choices=US_REGIONS)
    image = models.ImageField(upload_to='images/%Y-%m-%d')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='photos',
    )
    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_published = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(null=True)
    published = models.CharField(
        max_length=10,
        choices=PRIVACY,
        default='public',
    )
    albumns = models.ManyToManyField('Albumn', related_name='photos')

    def __str__(self):
        return self.title

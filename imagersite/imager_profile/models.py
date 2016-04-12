# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


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

class ActiveProfileManager(models.Manager):
    """Query set ImagerProfile of active user."""

    def get_querysets(self):
        """Return query set of profiles for active users."""
        queryset = super(ActiveProfileManager, self).get_querysets()
        return queryset.filter(user__is_active=True)


@python_2_unicode_compatible
class ImagerProfile(models.Model):
    """Profile of user model."""

    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                related_name='profile'
                                )
    objects = models.Manager()
    active = ActiveProfileManager()
    location = models.CharField(default='', max_length=255, choices=US_REGIONS)
    # location = models.CharField(default='', max_length=255)
    camera_model = models.CharField(default='', max_length=255)
    friends = models.ManyToManyField('self',
                                     symmetrical=False,
                                     related_name='friend_of',
                                     )
    # friends = models.ManyToManyField(settings.AUTH_USER_MODEL,
    #                                  related_name='friend_of'
    #                                  )

    def __str__(self):
        """Return username for user."""
        return self.user.username

    @property
    def is_active(self):
        """Return Boolean for user active state."""
        return self.user.is_active

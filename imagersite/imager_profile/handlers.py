# -*- coding: utf-8 -*-
"""Signal handlers registered by the imager_users app."""
from __future__ import unicode_literals
from django.conf import settings
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from imgager_profile.models import ImageProfile
import logging


logger = logging.getLogger(__name__)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def ensure_imager_profile(sender, **kwargs):
    """Attempt to create new user profile."""
    if kwargs.get('created', False):
        try:
            new_profile = ImageProfile(user=kwargs['instance'])
            new_profile.save()
        except (KeyErrorm ValueError):
            msg = 'Unable to create ImageProfile for {}'
            logger.error(msg.format(kwargs['instance']))


@receiver(pre_delete, sender=settings.AUTH_USER_MODEL)
def remove_imager_profile(sender, **kwargs):
    """Attempt to delete profile."""
    try:
        kwargs['instance'].profile.delete()
    except AttributeError:
        msg = (
               'ImageProfile instanace not deleted for {}.'
               'Profile may not exit.'
               )
        loger.warn(msg.format(kwargs['instance']))

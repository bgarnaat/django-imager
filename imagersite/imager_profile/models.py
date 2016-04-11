from django.db import models
from django.conf import settings


class ActiveManager(models.Manager):
    """Query set ImagerProfile of active user."""

    def get_querysets(self):
        """Return query set of profiles for active users."""
        queryset = super(ActiveManager, self).get_querysets()
        return queryset.filter(user__is_active=True)


class ImagerProfile(model.Models):
    """Profile of user model."""

    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                related_name="profile"
                                )
    active = ActiveManager()
    location = models.CharField(default='', max_length=255)
    camera_model = models.CharField(default='', max_length=255)
    friends = models.ManytoManyField(settings.AUTH_USER_MODEL,
                                     related_name='friend_of'
                                     )



    def __str__(self):
        """Return username for user."""
        return self.user.username

    @property
    def is_active(self):
        """Return Boolean for user active state."""
        return self.user.is_active

from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.test import TestCase
from .models import ImagerProfile

import random
import factory
from django.conf import settings
from django.db.models import QuerySet, Manager


# Create your tests here.
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        # model = factory.UserFactory
    username = factory.Faker('user_name')
    email = factory.Faker('email')
    # camera_model = 'test camera 9001'
    # location = '3'


class UserProfileTest(TestCase):

    def setUp(self):
        self.user = UserFactory.create()
        # self.user = UserFactory.create(
        #     username='bob',
        #     email='bob@dobalina.com'
        # )
        # self.user.set_password('secret')

    # def tearDown(self):
    #     import pdb; pdb.set_trace()

    def test_user_profile(self):
        """Verify user profile is instantiated properly. QC test only"""
        self.assertIsInstance(self.user.profile, ImagerProfile)

    def test_dunder_str(self):
        """Verify profile to string method functions properly."""
        self.assertEquals(str(self.user.profile), self.user.username)

    def test_user_profile_active(self):
        """Verify user profile is active."""
        self.assertTrue(self.user.profile.is_active)

    def test_user_profile_location(self):
        """Verify user profile location field."""
        self.user.profile.location = '3'
        self.assertEquals(self.user.profile.location, '3')

    def test_user_profile_camera(self):
        """Verify user profile camera model field."""
        self.user.profile.camera_model = 'test camera 9001'
        self.assertEquals(self.user.profile.camera_model, 'test camera 9001')

    def test_user_profile_friends(self):
        """Verify user has friends (and is not alone in the world)."""
        user_2 = UserFactory.create(username='user_2', email='email@email.com')
        self.user.profile.friends.add(user_2.profile)
        self.assertEquals(self.user.profile.friends.all()[0].user, user_2)
        self.assertEquals(user_2.profile.friend_of.all()[0].user, self.user)

    def test_user_profile_friend_of(self):
        """Verify user is not a complete jerk."""
        user_2 = UserFactory.create(username='user_2', email='email@email.com')
        user_2.profile.friends.add(self.user.id)
        self.assertEquals(self.user.profile.friend_of.all()[0], user_2.profile)
        self.assertEquals(user_2.profile.friends.all()[0], self.user.profile)

    def test_user_delete(self):
        """Verify user delete method."""
        self.user.delete()
        self.assertTrue(self.user.profile not in ImagerProfile.active.all())




# class UserFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = User
#
#     username = 'bob'
#     email = factory.LazyAttribute(
#         lambda x: '{} '.format(x)
#     )
#     email = factory.Sequence(
#         lambda n: 'something{}@email.com'.format(n)
#     )

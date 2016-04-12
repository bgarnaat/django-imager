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


class UserTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.create(
            username='bob',
            email='bob@dobalina.com'
        )
        self.user.set_password('secret')

    # def tearDown(self):
    #     import pdb; pdb.set_trace()

    def test_foo(self):
        pass




class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = 'bob'
    email = factory.LazyAttribute(
        lambda x: '{} '.format(x)
    )
    email = factory.Sequence(
        lambda n: 'something{}@email.com'.format(n)
    )

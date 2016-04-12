from django.test import TestCase
from imager_profile.tests import UserFactory

# Create your tests here.


class PhotoFactory(factory.django.DjangoModelFactory):



class AlbunnFactory(factory.django.DjangoModelFactory):
    class = Meta:
        model = albumn


class PhotoTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.create(
            username='bob',
            email='bob@bob.com',
        )
        self.user.set_password('secret')

        self.albumn = AlbumnFactory.create(
            name='test_albumn',
            user=self.user,
        )

        self.photo = PhotoFactory.create(
            title='test_image',
            user=self.user,
            # self.alumn is a MANAGER!  USE .add
            # albumns = self.photo.albumn.add(self.albumn)
        )

        # self.photo.albumns = self.albumn

    # GET RID OF THIS TEST.  IT IS A TAUTOLOGY.
    def test_photo_exists(self):
        self.assertTrue(self.photo)
        # check that image has an ID or PK (primary key)
        # self.assertTrue(modelinstance.pk)

    def test_image_has_image(self):
        self.assertIsInstance(self.photo.image, ImageFieldFile)

    def test_photo_has_user(self):
        self.assertEquals(self.photo.user, self.user)

    def test_photo_has_albumn(self):
        self.assertEquals(self.photo.albumns, self.alumn)

    def test_creation(self):
        # test photo unsaved:
            # has no id, created, modified
        # test photo saved:
            # has id, created, modified


class AlbumnTestCase(TestCase):

    def setUp(self):

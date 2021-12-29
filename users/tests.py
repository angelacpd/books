from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.password = 'This154test'

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='angela',
            email='angela@email.com',
            password=self.password
        )
        self.assertEqual(user.username, 'angela')
        self.assertEqual(user.email, 'angela@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='superadmin',
            email='superadmin@email.com',
            password=self.password
        )
        self.assertEqual(user.username, 'superadmin')
        self.assertEqual(user.email, 'superadmin@email.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

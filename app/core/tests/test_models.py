from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='test@test.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successul(self):
        """Testing creating new user with email succesful"""
        email = 'test@test.com'
        password = 'thisisatest'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_noralized(self):
        """Test the email for a new user is normalized"""
        email = 'test@test.com'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test creating new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@test.com',
            '12345test'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_taf_str(self):
        """Test the tsg string reprezentation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Something'
        )

        self.assertEqual(str(tag), tag.name)

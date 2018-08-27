from django.test import TestCase

from django.contrib.auth.models import User, Permission
from django.contrib.auth import authenticate, logout
from django.contrib.contenttypes.models import ContentType
from signin.models import Superhero

from django.shortcuts import get_object_or_404

def create_test_user(username='test@mctestersonandco.com', password='test1234'):
    user_ = User.objects.create_user(username=username, password=password)
    user_.save()
    return user_

def create_read_only_permission(content_type):
    return Permission.objects.create(
        codename='read_only',
        name='Has Read-only access to database',
        content_type=content_type,
    )

class AuthenticationTests(TestCase):
    def test_can_create_and_assign_permissions_to_users(self):
        user_ = create_test_user()
        self.assertFalse(user_.has_perm('signin.read_only'))

        superhero_content_type = ContentType.objects.get_for_model(Superhero)
        read_only_perm = create_read_only_permission(superhero_content_type)
        self.assertEqual(read_only_perm.codename, 'read_only', msg='read_only_perm should have been created with codename read_only')

        user_.user_permissions.add(read_only_perm)     # or alternatively permissions.set if you have a list,        
        same_user = get_object_or_404(User, pk=user_.id)     # Request new instance of user, since Django caches permissions and the next assertion will fail without reloading form database. Won't be a problem in production environment, since you will never check permissions immediately after assigning them. You'll always re-load from database before using it.
        self.assertTrue(same_user.has_perm('signin.read_only'))

    def test_create_authentication_session(self):
        username = 'tester@testerson.com'
        password = 'asdf1234'
        user_ = create_test_user(username=username, password=password)

        # test login
        user_ = authenticate(username=username, password="wrong password")
        self.assertIsNone(user_, msg='User was able to authenticate with wrong password')   

        user_ = authenticate(username=username, password=password)
        self.assertIsNotNone(user_, msg='Authenticating user did not work')

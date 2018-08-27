from django.test import TestCase

from django.contrib.auth.models import User, Permission, Group
from django.contrib.auth import authenticate
from django.contrib.contenttypes.models import ContentType
from signin.models import Superhero

from django.shortcuts import get_object_or_404

def create_test_user(username='test@mctestersonandco.com', password='test1234'):
    user_ = User.objects.create_user(username=username, password=password)
    user_.save()
    return user_

def create_a_test_permission(content_type, codename='test_perm'):
    return Permission.objects.create(
        codename=codename,
        name='Description of test permission',
        content_type=content_type,
    )


## A lot of these tests below, they do test core django functionality, which is unncessary. It is however still useful because it documents the syntax required to do certain jobs, eg in the command line, or in views
class AuthenticationTests(TestCase):
    def test_can_create_and_assign_permissions_to_users(self):
        user_ = create_test_user()
        self.assertFalse(user_.has_perm('signin.test_perm'))

        superhero_content_type = ContentType.objects.get_for_model(Superhero)
        test_permission = create_a_test_permission(superhero_content_type)
        self.assertEqual(test_permission.codename, 'test_perm', msg='test_perm should have been created with codename read_only')

        user_.user_permissions.add(test_permission)     # or alternatively permissions.set if you have a list,        
        same_user = get_object_or_404(User, pk=user_.id)     # Request new instance of user, since Django caches permissions and the next assertion will fail without reloading form database. Won't be a problem in production environment, since you will never check permissions immediately after assigning them. You'll always re-load from database before using it.
        self.assertTrue(same_user.has_perm('signin.test_perm'))

    def test_can_create_and_assign_group_to_users(self):
        user_ = create_test_user()
        self.assertFalse(user_.user_permissions.all().exists(), msg='user_permissions.all() should be empty')

        # create two permissions to be added to a group
        superhero_content_type = ContentType.objects.get_for_model(Superhero)        
        test_permission_one = create_a_test_permission(superhero_content_type, codename='test_one')   
        test_permission_two = create_a_test_permission(superhero_content_type, codename='test_two')

        # create a group of permissions
        test_group = Group.objects.create(
            name='Group with two permissions'
        )          
        test_group.permissions.add(test_permission_one)
        test_group.permissions.add(test_permission_two)

        #  test that the permissions made it into the group
        self.assertIn(test_permission_one, test_group.permissions.all())

        # assign the group to a user and test that it made it into the group
        user_.groups.add(test_group)
        same_user = get_object_or_404(User, pk=user_.id)
        self.assertTrue(same_user.has_perm('signin.test_one'))
        self.assertTrue(same_user.has_perm('signin.test_two'))

    def test_check_default_permissions_created_by_django(self):
        superhero_content_type = ContentType.objects.get_for_model(Superhero)
        perms = Permission.objects.filter(content_type=superhero_content_type)
        read_only = Permission.objects.get(codename='add_superhero')
        self.assertIn(read_only, perms)

    def test_create_authentication_session(self):
        username = 'tester@testerson.com'
        password = 'asdf1234'
        user_ = create_test_user(username=username, password=password)

        # test login
        user_ = authenticate(username=username, password="wrong password")
        self.assertIsNone(user_, msg='User was able to authenticate with wrong password')   

        user_ = authenticate(username=username, password=password)
        self.assertIsNotNone(user_, msg='Authenticating user did not work')

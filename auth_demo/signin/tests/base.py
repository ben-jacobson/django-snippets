from django.contrib.auth.models import User, Permission
from signin.models import Superhero

def create_test_user(username='test@mctestersonandco.com', password='test1234'):
    user_ = User.objects.create_user(username=username, password=password)
    user_.save()
    return user_

def create_test_user_and_login(client, username='test@mctestersonandco.com', password='test1234'):
    create_test_user(username=username, password=password)
    client.login(username=username, password=password)

def create_a_test_permission(content_type, codename='test_perm'):
    return Permission.objects.create(
        codename=codename,
        name='Description of test permission',
        content_type=content_type,
    )

def create_test_superhero(name='Superman', bio='asdf', picture_url='www.test.com'):
    superhero_ = Superhero.objects.create(
        name = name,
        bio = bio,
        picture = picture_url
    )
    superhero_.save()
    return superhero_

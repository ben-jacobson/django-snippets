from django.contrib.auth.models import User, Permission

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
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user
from .base import create_test_user, create_test_superhero, create_test_user_and_login
from signin.models import Superhero
from django.contrib.auth.models import Permission

class LoginFormTests(TestCase): 
    def test_post_invalid_username_andor_password(self):
        # deliberately don't create any users 
        #user_ = create_test_user(username='test@test.com.au', password='asdf1234') # If you want to ensure this test can fail, uncomment below

        test_login_data = {
            'email_username': 'test@test.com.au',
            'password': 'asdf1234',
        }        
        response = self.client.post(reverse('home_page'), test_login_data)
        #self.asserFalse(user_.is_authenticated) 
        self.assertEqual(response.status_code, 200, msg='If form is invalid, it shouldnt redirect')
        self.assertContains(response, 'login-error') # Page should have atleast one invalid form message on page

    def test_post_valid_login_data_and_logout(self):
        username = 'test@mctestersonandco.com.au'
        password = 'test1234'
        user_ = create_test_user(username=username, password=password)
        response = self.client.post(reverse('home_page'), {'username': username, 'password': password}) # do we need to use double stars?
        user_ = get_user(self.client)
        self.assertTrue(user_.is_authenticated, msg='Posting login details to home page should authenticate user')

        # page will now redirect to superhero listview
        self.assertRedirects(response, expected_url=reverse('superhero_listview')) # redirection happens too early for this test to pass. Instead we'll just make sure we're on the right page based on it's template

        try:
            self.client.logout()
        except: 
            self.fail('Could not log out, unsure why')
        finally:
            user_ = get_user(self.client)  # need to read the state of the object once more cause caching
            self.assertFalse(user_.is_authenticated, msg='User should now be logged out')

    def test_form_sets_required_fields_as(self):
        response = self.client.get(reverse('home_page'))
        self.assertEqual(response.status_code, 200, msg='Home page should load correctly')
        self.assertContains(response, 'required') # Page should have atleast one invalid form message on page

'''class SuperheroForm(ModelForm):     # normally would define this in forms.py, however this is only used for testing. Our production code uses a CreateView which automatically generates the same ModelForm for us 
    class Meta:
        model = Superhero
        fields = '__all__'   '''  

class SuperheroEditTest(TestCase):
    def test_post_page_edits(self):
        # simulates posting the form data to the home page, just like the form would, then asserts that it lands in the database
        hero = create_test_superhero(name='Batman')    
        hero_modifications = {
            'name': 'Fatman',
            'bio': 'Batman, except fat',
            'picture': 'www.google.com',
        }
        user_ = create_test_user_and_login(client=self.client) # first login as an autheticated user
        user_.user_permissions.add(Permission.objects.get(codename='change_superhero'))
        response = self.client.post(reverse('superhero_editview', kwargs={'slug': hero.slug}), hero_modifications)   
        self.assertEqual(response.status_code, 302, msg='edit page should redirect  if correct permissions have been assigned')
        test_hero = Superhero.objects.get(name='Fatman')  # retrieve object from database to test that posting on page can edit 
        self.assertRedirects(response, expected_url=reverse('superhero_editview', kwargs={'slug': test_hero.slug}))
        self.assertEqual(test_hero.bio, 'Batman, except fat')

    def test_post_validation_check(self):
        hero = create_test_superhero(name='Batman')    
        invalid_data = {
            'name': '',
            'bio': '', 
            'picture': '',  # so far just blank data
        }
        user_ = create_test_user_and_login(client=self.client) # first login as an autheticated user
        user_.user_permissions.add(Permission.objects.get(codename='change_superhero'))
        response = self.client.post(reverse('superhero_editview', kwargs={'slug': hero.slug}), invalid_data)   
        self.assertEqual(response.status_code, 200, msg='If form is invalid, it wont redirect')
        
    def test_form_has_required_fields(self):
        # this test doesn't actually work for testing the form validation, simply only tests whether or not one or more fields are marked with the 'required'
        hero = create_test_superhero(name='Batman')    
        user_ = create_test_user_and_login(client=self.client) # first login as an autheticated user
        user_.user_permissions.add(Permission.objects.get(codename='change_superhero'))
        response = self.client.get(reverse('superhero_editview', kwargs={'slug': hero.slug}))
        self.assertEqual(response.status_code, 200, msg='edit page should load correctly if correct permissions have been assigned')
        self.assertContains(response, 'required') # Page should have atleast one invalid form message on page

    def test_post_duplicate_data(self):
        hero_one = create_test_superhero(name='Batman')    
        create_test_superhero(name='Superman')    
        hero_one_modifications = {
            'name': 'Superman',
            'bio': 'Duplicate guy',
            'picture': 'www.google.com',
        }
        user_ = create_test_user_and_login(client=self.client) # first login as an autheticated user
        user_.user_permissions.add(Permission.objects.get(codename='change_superhero'))
        response = self.client.post(reverse('superhero_editview', kwargs={'slug': hero_one.slug}), hero_one_modifications)  
        self.assertContains(response, 'Superhero with this Hero Name already exists.') # Page should have atleast one invalid form message on page
        
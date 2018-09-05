from django.test import TestCase
from django.urls import reverse
from .base import create_test_user_and_login, create_test_superhero
from django.contrib.auth.models import Permission
from signin.models import Superhero

class ViewTests(TestCase):
    def test_home_page_renders_template(self):
        response = self.client.get(reverse('home_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_superhero_listView_renders_template(self):
        create_test_user_and_login(client=self.client)
        response = self.client.get(reverse('superhero_listview'))
        self.assertEqual(response.status_code, 200)        
        self.assertTemplateUsed(response, 'superhero_listview.html')

    def test_superhero_detailView_renders_template(self):
        hero = create_test_superhero(name='Batman')
        create_test_user_and_login(client=self.client)
        response = self.client.get(reverse('superhero_detailview', kwargs={'slug': hero.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'superhero_detailview.html')

    def test_superhero_editView_renders_template(self):
        hero = create_test_superhero(name='Batman')
        user_ = create_test_user_and_login(client=self.client) # first login as an autheticated user
        user_.user_permissions.add(Permission.objects.get(codename='change_superhero')) # ensure they have the correct permissions to view
        response = self.client.get(reverse('superhero_editview', kwargs={'slug': hero.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'superhero_editview.html')            

    def test_home_page_uses_login_form(self):
        response = self.client.get(reverse('home_page'))
        self.assertContains(response, '<form')

    def test_superhero_listView_contains_test_data(self):
        hero_one = create_test_superhero(name='Batman')
        hero_two = create_test_superhero(name='Iron Man')
        hero_three = create_test_superhero(name='Spiderman')

        create_test_user_and_login(client=self.client)
        response = self.client.get(reverse('superhero_listview'))
        self.assertContains(response, hero_one.name)
        self.assertContains(response, hero_two.name)
        self.assertContains(response, hero_three.name)

    def test_superhero_detailView_contains_test_data(self):
        hero = create_test_superhero(name='Batman')
        create_test_user_and_login(client=self.client)
        response = self.client.get(reverse('superhero_detailview', kwargs={'slug': hero.slug}))
        self.assertContains(response, hero.name)

    def test_superhero_detailview_redirects_to_updateview_with_edit_permissions(self):
        #if you have edit or delete permissions, instead of simply viewing the data, you'll be able to edit the data. The app achieves this by testing for permissions, then redirecting to an edit page if you have the right permissions
        hero = create_test_superhero(name='Batman')
        user_ = create_test_user_and_login(client=self.client) # first login as an autheticated user
        user_.user_permissions.add(Permission.objects.get(codename='change_superhero'))
        response = self.client.get(reverse('superhero_detailview', kwargs={'slug': hero.slug}))
        self.assertRedirects(response, expected_url=reverse('superhero_editview', kwargs={'slug': hero.slug}))

    def test_edit_superhero_page_redirects_if_not_correct_permissions(self):
        hero = create_test_superhero(name='Batman')
        create_test_user_and_login(client=self.client) # first login as an autheticated user
        # deliberately don't create correct permissions
        response = self.client.get(reverse('superhero_editview', kwargs={'slug': hero.slug}))
        self.assertEqual(response.status_code, 403) # should be forbidden for such a user

    def test_superhero_editView_has_prepopulated_data(self):
        hero = create_test_superhero(name='Batman')
        user_ = create_test_user_and_login(client=self.client) # first login as an autheticated user
        user_.user_permissions.add(Permission.objects.get(codename='change_superhero'))
        response = self.client.get(reverse('superhero_editview', kwargs={'slug': hero.slug}))
        self.assertContains(response, 'Batman')        

    def test_edit_superhero_page_has_form_with_correct_permissions(self):
        hero = create_test_superhero(name='Batman')
        user_ = create_test_user_and_login(client=self.client) # first login as an autheticated user
        user_.user_permissions.add(Permission.objects.get(codename='change_superhero'))
        response = self.client.get(reverse('superhero_editview', kwargs={'slug': hero.slug}))
        self.assertContains(response, '<form')

    def test_superhero_delete_view(self):
        # since these permissions aren't coupled to eachother, theoretically you could have 'delete' permissions 
        # without 'edit' permissions. This app doesn't allow you to press any delete buttons without the 'change' 
        # permission, but they should just be able to go directly to the url and successfully delete an instance
        user_ = create_test_user_and_login(client=self.client) # first login as an autheticated user
        user_.user_permissions.add(Permission.objects.get(codename='delete_superhero'))

        superheroes = []
        superheroes.append(create_test_superhero(name='Batman'))
        superheroes.append(create_test_superhero(name='Spiderman'))
        superheroes.append(create_test_superhero(name='Superman'))
        
        superheroes_in_db = Superhero.objects.all()
        self.assertEqual(superheroes, [hero for hero in superheroes_in_db]) 

        slug_of_hero_to_delete = superheroes[-1].slug
        superheroes.pop()    
         
        get_response = self.client.get(reverse('superhero_deleteview', kwargs={'slug': slug_of_hero_to_delete}), follow=True) # follow=True allows the page to redirect and update the response accordingly
        self.assertContains(get_response, 'Are you sure you want to delete')

        post_response = self.client.post(reverse('superhero_deleteview', kwargs={'slug': slug_of_hero_to_delete}), follow=True)
        self.assertRedirects(post_response, reverse('superhero_listview'))   

        superheroes_in_db = Superhero.objects.all()
        self.assertEqual(superheroes, [hero for hero in superheroes_in_db])  # compare new popped list with what we just re-read from database
        
    def test_delete_button_appears_on_page_with_delete_permissions(self):
        hero = create_test_superhero(name='Batman')
        user_ = create_test_user_and_login(client=self.client) # first login as an autheticated user
        user_.user_permissions.add(Permission.objects.get(codename='change_superhero')) # only add change permission so as to get access to page, but don't add delete permission
        user_.user_permissions.add(Permission.objects.get(codename='delete_superhero')) # now add the delete permission
        response = self.client.get(reverse('superhero_editview', kwargs={'slug': hero.slug}))
        self.assertContains(response, 'delete-button')

    def test_delete_button_doesnt_appear_on_page_without_delete_permissions(self):
        hero = create_test_superhero(name='Batman')
        user_ = create_test_user_and_login(client=self.client) # first login as an autheticated user
        user_.user_permissions.add(Permission.objects.get(codename='change_superhero')) # only add change permission so as to get access to page, but don't add delete permission
        response = self.client.get(reverse('superhero_editview', kwargs={'slug': hero.slug}))
        self.assertNotContains(response, 'delete-button')
# django-snippets
Code snippets for use in future Django projects

August 2018 - Ben Jacobson

In this repo are various code snippets for use in future Django projects. These are mini projects that I had used to learn Django and it's various features before attempting anything serious with it. Where possible, functional and unit tests are included too.

Included in this repo:

- pizza_shop_models - In it's current form, its a demonstration of Django's ManyToMany database relationships and appropriate model testing methods. Similar to an example seen in the official documentation, it builds a Pizza model, and a Topping model and defines a many to many relationship between them. The purpose of this is to easily repurpose this code for real-world use. Unit tests are included and can also be refactored into future projects. 
- small_site_with_blog - This is a demonstration of Django's class based generic views and simple templates. This is a simple blog system, however there are much better ones out there. 
- signup_form - Some demo code demonstrating Forms, in particular ModelForms, and their generic views such as CreateView. Some test code can easily be repurposed for later projects. Potentially may later change to include some Javascript form validation, but for now just uses Django's default validation


Todo list:

- Build something to demonstrate customizing the admin page, eg adding buttons that interface with model methods
- Build a demo app that uses Django's built-in authentication system, eg a page for creating a username & password, then use those login details to access pages that aren't accessible to the public

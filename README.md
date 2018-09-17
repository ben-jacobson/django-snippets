# django-snippets
Code snippets for use in future Django projects

Requirements - Python 3.6, then run "pip install -r requirements.txt" for all others

August 2018 - Ben Jacobson

In this repo are various code snippets for reuse in future Django projects. These mini projects were really helpful to me in learning Django.
The aim is that when working on something bigger, I can easily just drop in one of these snippets and refactor it into the project to save time. 
Where possible, functional and unit tests are included too.

Included in this repo:

- pizza_shop_models - Creating this helped me to learn Django's ManyToMany database relationships and appropriate model testing methods. Similar to an example seen in the official documentation, it builds a Pizza model, and a Topping model and defines a many to many relationship between them. 
- small_site_with_blog - This was to help me learn about Django's class based generic views and simple templates. This is a simple blog system, however there are much better ones out there for real world use.  
- signup_form - Some demo code demonstrating how to use in-built Forms, in particular ModelForms, and their generic views such as CreateView. At some point it would be good to revisit this to see how some Javascript form validation can be implemented on top.
- auth_demo - Created this to learn about Djangos Authentication system. When logged in, this lets you see a secret database. Also, depending on your given permissions allows you to edit and delete data. 

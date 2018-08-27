from django.views.generic.base import TemplateView

class home_page(TemplateView):
    template_name = 'home.html'

class superhero_listView(TemplateView):
    template_name = 'superhero_listview.html'
    
class superhero_detailView(TemplateView):
    template_name = 'superhero_detailview.html'
    
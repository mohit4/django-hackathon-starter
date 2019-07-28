from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from django.views.generic import TemplateView

from .models import Entity

# Create your views here.
class IndexView(ListView):
    '''
    Listing all the entities
    '''
    template_name = 'app/index.html'
    context_object_name = 'entity'
    model = Entity

class EntityListView(ListView):
    '''
    Listing all the entities
    '''
    template_name = 'app/entity_list.html'
    context_object_name = 'entity'
    model = Entity

class EntityDetailView(DetailView):
    '''
    Detail view of a single entity
    '''
    template_name = 'app/entity_detail.html'
    context_object_name = 'entity'
    model = Entity

class EntityCreateView(CreateView):
    '''
    Creating an entity
    '''
    template_name = 'app/entity_form.html'
    fields = ('title','description','points','cost','category','active','email','user')
    model = Entity

class EntityUpdateView(UpdateView):
    '''
    Updating an entity
    '''
    template_name = 'app/entity_form.html'
    fields = ('title','description','points','cost','category','active','email')
    model = Entity
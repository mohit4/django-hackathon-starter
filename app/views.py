from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from .models import Entity

# Create your views here.
class IndexView(ListView):
    '''
    Listing all the entities
    '''
    template_name = 'app/index.html'
    context_object_name = 'entities'
    model = Entity
    paginate_by = 5

class EntityListView(ListView):
    '''
    Listing all the entities
    '''
    template_name = 'app/entity_list.html'
    context_object_name = 'entities'
    model = Entity
    paginate_by = 5

class EntityDetailView(DetailView):
    '''
    Detail view of a single entity
    '''
    template_name = 'app/entity_detail.html'
    context_object_name = 'entity'
    model = Entity

class EntityCreateView(SuccessMessageMixin, CreateView):
    '''
    Creating an entity
    '''
    template_name = 'app/entity_form.html'
    fields = ('title','description','points','cost','category','active','email','user')
    model = Entity
    success_message = "New entity created!"

class EntityUpdateView(SuccessMessageMixin, UpdateView):
    '''
    Updating an entity
    '''
    template_name = 'app/entity_form.html'
    fields = ('title','description','points','cost','category','active','email')
    model = Entity
    success_message = "Entity updated successfully!"

class EntityDeleteView(DeleteView):
    '''
    Deleting an entity
    '''
    model = Entity
    success_url = reverse_lazy('app:index')
    template_name = 'app/entity_detail.html'
    success_message = "Entity deleted successfully!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(EntityDeleteView, self).delete(request, *args, **kwargs)
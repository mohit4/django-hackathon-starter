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
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from .forms import CommentForm

from .models import Entity
from .models import Comment

# Create your views here.
class IndexView(LoginRequiredMixin, ListView):
    '''
    Listing all the entities
    '''
    template_name = 'app/index.html'
    context_object_name = 'entities'
    model = Entity
    paginate_by = 5

class EntityListView(LoginRequiredMixin, ListView):
    '''
    Listing all the entities
    '''
    template_name = 'app/entity_list.html'
    context_object_name = 'entities'
    model = Entity
    paginate_by = 5

class EntityDetailView(LoginRequiredMixin, DetailView):
    '''
    Detail view of a single entity
    '''
    template_name = 'app/entity_detail.html'
    context_object_name = 'entity'
    model = Entity

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.filter(entity=self.object)
        context["form"] = CommentForm
        return context

class EntityCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    '''
    Creating an entity
    '''
    template_name = 'app/entity_form.html'
    fields = ('title','description','points','cost','category','active','email', 'profile_image', 'cover_image')
    model = Entity
    success_message = "New entity created!"

    def form_valid(self, form):
        '''
        Beforing saving, assign the user id to entity
        '''
        model = form.save(commit=False)
        model.user = self.request.user
        model.save()
        return super(EntityCreateView, self).form_valid(form)

class EntityUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    '''
    Updating an entity
    '''
    template_name = 'app/entity_form.html'
    fields = ('title','description','points','cost','category','active','email', 'profile_image', 'cover_image')
    model = Entity
    success_message = "Entity updated successfully!"

class EntityDeleteView(LoginRequiredMixin, DeleteView):
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

class AddCommentView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    '''
    Add a comment
    '''
    model = Comment
    success_message = 'Comment added!'
    fields = ('title',)
    template_name = 'app/entity_detail.html'

    def dispatch(self, request, *args, **kwargs):
        '''
        Overridden, in order to make the entity object exist
        before we go any further
        '''
        self.entity = get_object_or_404(Entity, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        '''
        Beforing saving, assign the user and entity to comment
        '''
        model = form.save(commit=False)
        model.user = self.request.user
        model.entity = self.entity
        model.save()
        return super(AddCommentView, self).form_valid(form)
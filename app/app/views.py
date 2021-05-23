from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Object


def index(request):
    """
    Index view for listing the search results
    """
    search_object = request.GET.get('search')

    if search_object:
        objects = Object.objects.filter(
            Q(title__icontains=search_object)
            | Q(description__icontains=search_object)
        )
    else:
        objects = Object.objects.all().order_by("-title")
    
    context = {
        'objects': objects,
        'heading': f'Showing search results for : "{search_object}"'
    }

    return render(request, "app/object_list.html", context)


class ObjectCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Creating a new object
    """
    template_name = "app/object_form.html"
    model = Object
    fields = ('title', 'description', 'credits', 'value', 'category', 'weblink',)
    success_message = 'Added new object!'

    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["heading"] = "Create new Object"
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ObjectUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Updating an existing object
    """
    template_name = "app/object_form.html"
    model = Object
    fields = ('description', 'credits', 'value', 'category', 'weblink',)
    success_message = 'Object updated!'

    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["heading"] = "Update Object"
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ObjectListView(LoginRequiredMixin, ListView):
    """
    Listing all the objects present in database
    """
    template_name = "app/object_list.html"
    model = Object
    context_object_name = "objects"

    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["heading"] = "Listing all object(s)"
        return context


class ObjectDetailView(LoginRequiredMixin, DetailView):
    """
    Printing details of a single object
    """
    template_name = "app/object_detail.html"
    model = Object
    context_object_name = "object"

    login_url = '/'


class ObjectDeleteView(LoginRequiredMixin, DeleteView):
    """
    Deleting an existing object
    """
    template_name = "app/object_detail.html"
    model = Object
    context_object_name = "object"
    success_url = reverse_lazy("app:object-list")
    success_message = 'Object deleted!'

    login_url = '/'

    def delete(self, request, *args, **kwargs):
        messages.error(self.request, self.success_message)
        return super(ObjectDeleteView, self).delete(request, *args, **kwargs)

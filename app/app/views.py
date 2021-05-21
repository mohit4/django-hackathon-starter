from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Object


class ObjectCreateView(CreateView):
    """
    Creating a new object
    """
    template_name = "app/object_form.html"
    model = Object
    fields = ('title', 'description',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["heading"] = "Create new Object"
        return context


class ObjectUpdateView(UpdateView):
    """
    Updating an existing object
    """
    template_name = "app/object_form.html"
    model = Object
    fields = ('description',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["heading"] = "Update Object"
        return context


class ObjectListView(ListView):
    """
    Listing all the objects present in database
    """
    template_name = "app/object_list.html"
    model = Object
    context_object_name = "objects"


class ObjectDetailView(DetailView):
    """
    Printing details of a single object
    """
    template_name = "app/object_detail.html"
    model = Object
    context_object_name = "object"


class ObjectDeleteView(DeleteView):
    """
    Deleting an existing object
    """
    template_name = "app/object_detail.html"
    model = Object
    context_object_name = "object"
    success_url = reverse_lazy("app:object-list")

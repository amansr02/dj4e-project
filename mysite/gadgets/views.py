from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from gadgets.models import Gadget,Type

# Create your views here.

class MainView(LoginRequiredMixin, View) :
    def get(self, request):
        mc = Type.objects.all().count();
        al = Gadget.objects.all();

        ctx = { 'type_count': mc, 'gadget_list': al };
        return render(request, 'gadgets/gadget_list.html', ctx)

class TypeView(LoginRequiredMixin,View) :
    def get(self, request):
        ml = Type.objects.all();
        ctx = { 'type_list': ml };
        return render(request, 'gadgets/type_list.html', ctx)

# We use reverse_lazy() because we are in "constructor attribute" code
# that is run before urls.py is completely loaded
class TypeCreate(LoginRequiredMixin, CreateView):
    model = Type
    fields = '__all__'
    success_url = reverse_lazy('gadgets:all')

# TypeUpdate has code to implement the get/post/validate/store flow
# GadgetUpdate (below) is doing the same thing with no code
# and no form by extending UpdateView
class TypeUpdate(LoginRequiredMixin, UpdateView):
    model = Type
    fields = '__all__'
    success_url = reverse_lazy('gadgets:all')


class TypeDelete(LoginRequiredMixin, DeleteView):
    model = Type
    fields = '__all__'
    success_url = reverse_lazy('gadgets:all')


# Take the easy way out on the main table
# These views do not need a form because CreateView, etc.
# Build a form object dynamically based on the fields
# value in the constructor attributes

class GadgetCreate(LoginRequiredMixin,CreateView):
    model = Gadget
    fields = '__all__'
    success_url = reverse_lazy('gadgets:all')

class GadgetUpdate(LoginRequiredMixin, UpdateView):
    model = Gadget
    fields = '__all__'
    success_url = reverse_lazy('gadgets:all')

class GadgetDelete(LoginRequiredMixin, DeleteView):
    model = Gadget
    fields = '__all__'
    success_url = reverse_lazy('gadgets:all')

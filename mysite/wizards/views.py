from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from wizards.models import Wizard, House

# Create your views here.

class MainView(LoginRequiredMixin, View) :
    def get(self, request):
        mc = House.objects.all().count();
        al = Wizard.objects.all();

        ctx = { 'house_count': mc, 'wizard_list': al };
        return render(request, 'wizards/wizard_list.html', ctx)

class HouseView(LoginRequiredMixin,View) :
    def get(self, request):
        ml = House.objects.all();
        ctx = { 'house_list': ml };
        return render(request, 'wizards/house_list.html', ctx)

# We use reverse_lazy() because we are in "constructor attribute" code
# that is run before urls.py is completely loaded
class HouseCreate(LoginRequiredMixin, CreateView):
    model = House
    fields = '__all__'
    success_url = reverse_lazy('wizards:all')

# HouseUpdate has code to implement the get/post/validate/store flow
# WizardUpdate (below) is doing the same thing with no code
# and no form by extending UpdateView
class HouseUpdate(LoginRequiredMixin, UpdateView):
    model = House
    fields = '__all__'
    success_url = reverse_lazy('wizards:all')


class HouseDelete(LoginRequiredMixin, DeleteView):
    model = House
    fields = '__all__'
    success_url = reverse_lazy('wizards:all')


# Take the easy way out on the main table
# These views do not need a form because CreateView, etc.
# Build a form object dynamically based on the fields
# value in the constructor attributes
class WizardCreate(LoginRequiredMixin,CreateView):
    model = Wizard
    fields = '__all__'
    success_url = reverse_lazy('wizards:all')

class WizardUpdate(LoginRequiredMixin, UpdateView):
    model = Wizard
    fields = '__all__'
    success_url = reverse_lazy('wizards:all')

class WizardDelete(LoginRequiredMixin, DeleteView):
    model = Wizard
    fields = '__all__'
    success_url = reverse_lazy('wizards:all')

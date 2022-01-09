from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic

from django.urls import reverse_lazy
from purchase.forms import ProviderForm

from purchase.models import Provider


# Create your views here.


class ProviderView(LoginRequiredMixin, generic.ListView):
    model = Provider
    template_name = "purchase/provider_list.html"
    context_object_name= "obj"
    login_url='bases:login'


class NewProvider(LoginRequiredMixin, generic.CreateView):
    model=Provider
    template_name = 'purchase/provider_form.html'
    context_object_name='obj'
    form_class=ProviderForm
    success_url=reverse_lazy("purchase:provider_list")
    login_url='bases:login'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class EditProvider(LoginRequiredMixin, generic.UpdateView):
    model=Provider
    template_name = 'purchase/provider_form.html'
    context_object_name='obj'
    form_class=ProviderForm
    success_url=reverse_lazy("purchase:provider_list")
    login_url='bases:login'

    def form_valid(self, form):
        form.instance.modified_by = self.request.user.id
        return super().form_valid(form)


def deactivate_provider(request, id):
    provider = Provider.objects.filter(pk=id).first()
    context={}
    template_name='purchase/deactivate_provider.html'

    if not provider:
        return HttpResponse('Provider does not exist' + '  ' + str(id))

    if request.method == 'GET':
        context = {'obj': provider }

    if request.method == 'POST':
        provider.is_active = False
        provider.save()
        context = {'obj': 'OK' }
        return HttpResponse("Provider has been deactivated")    

    return render(request, template_name, context)   
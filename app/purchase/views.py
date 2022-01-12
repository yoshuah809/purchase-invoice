from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic

from django.urls import reverse_lazy
from bases.views import NoProvileges
from purchase.forms import ProviderForm

from purchase.models import Provider


# Create your views here.


class ProviderView(NoProvileges, generic.ListView):
    permission_required='inv.view_provider'
    model = Provider
    template_name = "purchase/provider_list.html"
    context_object_name= "obj"
    

class NewProvider(NoProvileges, generic.CreateView):
    permission_required='inv.new_provider'
    model=Provider    
    template_name = 'purchase/provider_form.html'
    context_object_name='obj'
    form_class=ProviderForm
    success_url=reverse_lazy("purchase:provider_list")
    

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class EditProvider(NoProvileges, generic.UpdateView):
    permission_required='inv.edit_provider'
    model=Provider
    template_name = 'purchase/provider_form.html'
    context_object_name='obj'
    form_class=ProviderForm
    success_url=reverse_lazy("purchase:provider_list")
    login_url='bases:login'

    def form_valid(self, form):
        form.instance.modified_by = self.request.user.id
        return super().form_valid(form)

@login_required(login_url='/login/')
@permission_required('inv.change_provider', login_url='bases:no_privileges')
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
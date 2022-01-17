from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.aggregates import Sum
from django.forms.fields import DateTimeField
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
import datetime

from django.urls import reverse_lazy
from bases.views import NoProvileges
from purchase.forms import ProviderForm, PurchaseHeaderForm

from purchase.models import Provider, PurchaseDetail, PurchaseHeader

from inv.models import Product


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


class PurchaseView(NoProvileges, generic.ListView):
    permission_required='inv.view_purchase_header'
    model = PurchaseHeader
    template_name = "purchase/purchase_list.html"
    context_object_name= "obj" 



@login_required(login_url='/login/')
@permission_required('purchase.view_PurchaseHeader', login_url='bases:no_privileges')
def purchase(request,purchase_id=None):
    template_name="purchase/purchase.html"
    prod=Product.objects.filter(is_active=True)
    purchase_form={}
    context={}

    if request.method=='GET':
        purchase_form=PurchaseHeaderForm()
        header = PurchaseHeader.objects.filter(pk=purchase_id).first()

        if header:
            detail = PurchaseDetail.objects.filter(purchase=header)
            purchase_date = datetime.date.isoformat(header.invoice_date)
            invoice_date = datetime.date.isoformat(header.purchase_date)
            e = {
                'purchase_date':purchase_date,
                'provider': header.provider,
                'observation': header.observation,
                'invoice_no': header.invoice_no,
                'invoice_date': invoice_date,
                'sub_total': header.sub_total,
                'discount': header.discount,
                'total':header.total
            }
            purchase_form = PurchaseHeaderForm(e)
        else:
            detail=None
        
        context={'products':prod,'header':header,'detail':detail,'header_form':purchase_form}

    if request.method=='POST':
        purchase_date = request.POST.get("purchase_date")
        observation = request.POST.get("observation")
        invoice_no = request.POST.get("invoice_no")
        invoice_date = request.POST.get("invoice_date")
        provider = request.POST.get("provider")
        sub_total = 0
        discount = 0
        total = 0

        if not purchase_id:
            prov=Provider.objects.get(pk=provider)

            header = PurchaseHeader(
                purchase_date=purchase_date,
                observation=observation,
                invoice_no=invoice_no,
                invoice_date=invoice_date,
                provider=prov,
                created_by = request.user 
            )
            if header:
                header.save()
                purchase_id=header.id
        else:
            header=PurchaseHeader.objects.filter(pk=purchase_id).first()
            if header:
                header.purchase_date=purchase_date
                header.observation=observation
                header.invoice_no=invoice_no
                header.invoice_date=invoice_date
                header.modified_by=request.user.id
                header.save()

        if not purchase_id:
            return redirect("purchase:purchase_list")
        
        product = request.POST.get("id_id_product")
        quantity = request.POST.get("id_quantity_detail")
        price = request.POST.get("id_price_detail")
        sub_total_detail = request.POST.get("id_sub_total_detail")
        discount_detail  = request.POST.get("id_discount_detail")
        total_detail  = request.POST.get("id_total_detail")

        prod = Product.objects.get(pk=product)

        detail = PurchaseDetail(
            purchase=header,
            product=prod,
            quantity=quantity,
            provider_price=price,
            discount=discount_detail,
            cost=0,
            created_by = request.user
        )

        if detail:
            detail.save()

            sub_total=PurchaseDetail.objects.filter(purchase=purchase_id).aggregate(Sum('sub_total'))
            discount=PurchaseDetail.objects.filter(purchase=purchase_id).aggregate(Sum('discount'))
            header.sub_total = sub_total["sub_total__sum"]
            header.discount=discount["discount__sum"]
            header.save()

        return redirect("purchase:edit_purchase",purchase_id=purchase_id)


    return render(request, template_name, context)
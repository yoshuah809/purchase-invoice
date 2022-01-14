from django import forms

from purchase.models import Provider, PurchaseHeader

class ProviderForm(forms.ModelForm):
    email=forms.EmailField(max_length=150)
    
    class Meta:
        model=Provider
        exclude = ['modified_by', 'date_modified', 'created_by', 'date_created']
        labels = {"is_active": "Active"}
        widget={'description': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update ({
                'class': 'form-control'
            })


class PurchaseHeaderForm(forms.ModelForm):
    purchase_date = forms.DateInput()
    invoice_date= forms.DateInput()
    
    class Meta:
        model=PurchaseHeader
        fields=['provider','purchase_date','observation',
            'invoice_no','invoice_date','sub_total',
            'discount','total']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['purchase_date'].widget.attrs['readonly'] = True
        self.fields['invoice_date'].widget.attrs['readonly'] = True
        self.fields['sub_total'].widget.attrs['readonly'] = True
        self.fields['discount'].widget.attrs['readonly'] = True
        self.fields['total'].widget.attrs['readonly'] = True
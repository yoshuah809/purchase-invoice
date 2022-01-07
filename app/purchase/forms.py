from django import forms

from purchase.models import Provider

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
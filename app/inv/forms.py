from django import forms

from .models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields = ['description', 'state']
        labels = {'description': "Category description", "state":"State"}
        widget={'description': forms.TextInput}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update ({
                    'class': 'form-control'
                })
from django import forms

from .models import Brand, Category, SubCategory


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields = ['description', 'is_active']
        labels = {'description': "Category description", "is_active":"Active"}
        widget={'description': forms.TextInput}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update ({
                    'class': 'form-control'
                })

class SubCategoryForm(forms.ModelForm):
    category= forms.ModelChoiceField(
        queryset=Category.objects.filter(is_active=True).order_by('description'), empty_label= 'Select Category'
    )
    class Meta:
        model=SubCategory
        fields = ['category','description', 'is_active']
        labels = {'description': "SubCategory ", "is_active":"Active"}
        widget={'description': forms.TextInput}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update ({
                    'class': 'form-control'
                })
            

class BrandForm(forms.ModelForm):
    class Meta:
        model=Brand
        fields = ['description', 'is_active']
        labels = {'description': "Brand description", "is_active":"Active"}
        widget={'description': forms.TextInput}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update ({
                    'class': 'form-control'
                })
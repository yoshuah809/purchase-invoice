from django import forms

from .models import Brand, Category, Product, SubCategory, Unit


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields = ['description', 'is_active']
        labels = {'description': "Category description", "is_active":"Active"}
        widget={'description': forms.TextInput()}

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
        widget={'description': forms.TextInput()}

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
        widget={'description': forms.TextInput()}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update ({
                    'class': 'form-control'
                })



class UnitForm(forms.ModelForm):
    class Meta:
        model=Unit
        fields = ['description', 'is_active']
        labels = {'description': "Unit description", "is_active":"Active"}
        widget={'description': forms.TextInput}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update ({
                    'class': 'form-control'
                })                

class ProductForm(forms.ModelForm):
    subcategory= forms.ModelChoiceField(
        queryset=Category.objects.filter(is_active=True).order_by('description'), empty_label= 'Select Category'
    )
    brand= forms.ModelChoiceField(queryset=Brand.objects.filter(is_active=True).order_by('description'),empty_label= 'Select Brand')
    class Meta:
        model=Product
        fields = ['code','bar_code', 'description', 'is_active', 'price', 'in_stock', 'last_purchased', 'brand', 'subcategory', 'unit']
        exclude = ['modified_by', 'date_modified', 'created_by', 'date_created']
        widget={'description': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update ({
                'class': 'form-control'
            })  
        self.fields['last_purchased'].widget.attrs['readonly'] = True     
        self.fields['in_stock'].widget.attrs['readonly'] = True                   
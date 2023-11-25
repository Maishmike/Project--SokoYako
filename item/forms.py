from django import forms
from .models import Item, Category


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image', 'is_featured')

        widgets = {
            'category': forms.Select(attrs={
                'class': 'border form-control rounded-3 mx-1',
                'placeholder': 'Select a category',
            }),
            'name': forms.TextInput(attrs={
                'class': 'border form-control rounded-3',
                'placeholder': 'Item Name',
            }),
            'description': forms.Textarea(attrs={
                'class': 'border form-control rounded-3',
                'placeholder': 'Item Description',
                'rows': '3'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'border form-control rounded-3',
                'placeholder': 'Item Price'
            }),
            'image': forms.FileInput(attrs={
                'class': 'border form-control rounded-3',
                'placeholder': 'Item Image'
            }),
            'is_featured': forms.CheckboxInput(attrs={
                'class': 'rounded-3',
                'id': 'is_featured',
                'name': 'is_featured'
            })

        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold', 'is_featured')

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'border form-control rounded-3',
                'placeholder': 'Item Name',
            }),
            'description': forms.Textarea(attrs={
                'class': 'border form-control rounded-3',
                'placeholder': 'Item Description'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'border form-control rounded-3',
                'placeholder': 'Item Price'
            }),
            'image': forms.FileInput(attrs={
                'class': 'border form-control rounded-3',
                'placeholder': 'Item Image'
            }),
            'is_featured': forms.CheckboxInput(attrs={
                'class': 'rounded-3',
                'id': 'is_featured',
                'name': 'is_featured'
            })

        }









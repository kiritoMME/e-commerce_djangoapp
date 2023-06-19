from django import forms
from .models import product

class product_form(forms.ModelForm):
    class Meta:
        model = product
        fields = ['name', 'description', 'sizes', 'price', 'featured_product', 'offer', 'image', 'gallery_1', 'gallery_2', 'gallery_3', 'gallery_4', 'offer_image']
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control', 'style':'width: 300px;height: 24px; margin: 10px 0;max-width: 100%'}) ,
            'description' : forms.Textarea(attrs={'class': 'form-control','style':'width: 100%'}) ,
            'sizes' : forms.TextInput(attrs={'class': 'form-control', 'style':'width: 300px;height: 24px; margin: 10px 0;max-width: 100%'}) ,
            # 'featured_product' : forms.bool(attrs={'class':'form-control'}) ,
            # 'offer' : forms.bool(attrs={'class':'form-control'}) ,
            'image' : forms.FileInput(attrs={'class':'form-control', 'style': 'margin: 10px 0'}) ,
            'gallery_1' : forms.FileInput(attrs={'class':'form-control', 'style': 'margin: 10px 0'}) ,
            'gallery_2' : forms.FileInput(attrs={'class':'form-control', 'style': 'margin: 10px 0'}) ,
            'gallery_3' : forms.FileInput(attrs={'class':'form-control', 'style': 'margin: 10px 0'}) ,
            'gallery_4' : forms.FileInput(attrs={'class':'form-control', 'style': 'margin: 10px 0'}) ,
            'offer_image' : forms.FileInput(attrs={'class':'form-control', 'style': 'margin: 10px 0'}) 
            
        }
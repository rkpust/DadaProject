# # from django import forms
# # from .models import CapOrder

# # class CapOrderForm(forms.ModelForm):
# #     class Meta:
# #         model = CapOrder
# #         fields = '__all__'  # You can specify specific fields if needed


from django import forms
from .models import CapOrder, CapOrderImage

class CapOrderForm(forms.ModelForm):
    # image = forms.ImageField(
    #     required=False,
    #     widget=forms.FileInput(attrs={'style': 'width: 200px;'}),
    #     help_text="Upload one or more images (optional)."
    # )
    class Meta:
        model = CapOrder
        fields = '__all__'
        widgets = {
            'ps_number': forms.TextInput(attrs={'style': 'width: 200px;'}),
            'ps_date': forms.DateInput(attrs={'type': 'date', 'style': 'width: 200px;'}),
            'sst10_date': forms.DateInput(attrs={'type': 'date', 'style': 'width: 200px;'}),
            'style': forms.TextInput(attrs={'style': 'width: 200px;'}),
            'byr_po': forms.TextInput(attrs={'style': 'width: 200px;'}),
            'quantity': forms.NumberInput(attrs={'min': 0, 'style': 'width: 200px;'}),
            'byr': forms.TextInput(attrs={'style': 'width: 200px;'}),
            'ship_date': forms.DateInput(attrs={'type': 'date', 'style': 'width: 200px;'}),
            'cap_item': forms.TextInput(attrs={'style': 'width: 200px;'}),
            'cap_type': forms.TextInput(attrs={'style': 'width: 200px;'}),
            'ship_via': forms.TextInput(attrs={'style': 'width: 200px;'}),
            'destination': forms.TextInput(attrs={'style': 'width: 200px;'}),
            'final_destination': forms.TextInput(attrs={'style': 'width: 200px;'}),
            'embroidery': forms.TextInput(attrs={'style': 'width: 200px;'}),
            'washing_method': forms.TextInput(attrs={'style': 'width: 200px;'}),
            'c_pattern': forms.TextInput(attrs={'style': 'width: 200px;'}),
            'v_pattern': forms.TextInput(attrs={'style': 'width: 200px;'}),
            'eyelet_number': forms.NumberInput(attrs={'style': 'width: 200px;'}),
            'eyelet_material': forms.TextInput(attrs={'style': 'width: 200px;'}),
            'c_cutter': forms.TextInput(attrs={'style': 'width: 200px;'}),
            'v_cutter': forms.TextInput(attrs={'style': 'width: 200px;'}),
            'color': forms.TextInput(attrs={'style': 'width: 200px;'}),
            'position': forms.TextInput(attrs={'style': 'width: 200px;'}),
            'f_mold': forms.TextInput(attrs={'style': 'width: 200px;'}),
            'b_mold': forms.TextInput(attrs={'style': 'width: 200px;'}),
            'visor_rows': forms.NumberInput(attrs={'style': 'width: 200px;'}),
            'extra_stitch_rows': forms.NumberInput(attrs={'style': 'width: 200px;'}),
            'first_row_from_brim': forms.NumberInput(attrs={'step': '0.01', 'style': 'width: 200px;'}),
            'distance_from_front_end': forms.NumberInput(attrs={'step': '0.01', 'style': 'width: 200px;'}),
            'packing': forms.TextInput(attrs={'style': 'width: 200px;'}),
        }
        labels = {
            'ps_number': 'PS Number',
            'ps_date': 'PS Date',
            'byr_po': 'Buyer PO',
            'quantity': 'Quantity',
            'ship_via': 'Shipping Method',
            'ship_date': 'S/D',
        }
        help_texts = {
            'quantity': 'Enter a positive integer for quantity.',
            'ps_date': 'Select the date of the PS.',
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity is not None and quantity < 0:
            raise forms.ValidationError("Quantity must be a non-negative integer.")
        return quantity


class CapOrderImageForm(forms.ModelForm):
    class Meta:
        model = CapOrderImage
        fields = ['image']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'multiple': 'multiple', 'style': 'width: 200px;'})

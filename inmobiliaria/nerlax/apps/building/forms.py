from django import forms
from .models import *


class buildingForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(buildingForm, self).__init__(*args, **kwargs)
        self.fields['supplier'].queryset = Supplier.objects.filter(state=True)
        self.fields['type_resource'].queryset = Classification.objects.filter(state=True)

    class Meta:
        model = Building
        fields = ['name', 'address', 'address2', 'city', 'postal_code', 'supplier',
                  'region', 'unit_qty', 'amenities', 'type_resource', 'description']
        labels = {
            'name': 'Name',
            'address': 'Address',
            'unit_qty': 'Quantity of flat',
            'amenities': 'It has amenities ?',
            'type_resource': 'Property type',
            'supplier': 'Supplier',
            'description': 'Description',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Building name ...',
                    'id': 'name',
                    'class': 'form-control',
                }),
            'address': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Street address'
                }),
            'address2': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Street addres line 2'
                }),
            'city': forms.TextInput(
                attrs={
                    'placeholder': 'City'
                }),
            'region': forms.TextInput(
                attrs={
                    'placeholder': 'Zone'
                }),
            'postal_code': forms.TextInput(
                attrs={
                    'placeholder': 'Postal / zip code',
                    'id': 'postal_code',
                    'class': 'form-control',
                }),
            'amenities': forms.CheckboxInput(
                attrs={
                    'id': 'aminities'
                }),
            'unit_qty': forms.NumberInput(
                attrs={
                    'id': 'unit_qty',
                    'class': 'form-control',
                }),
            'description': forms.Textarea(
                attrs={
                    'id': 'description',
                    'class': 'form-control',
                    'row': 6
                }),
            'supplier': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                })
        }


class unitForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(unitForm, self).__init__(*args, **kwargs)
        self.fields['renter'].queryset = UserModel.objects.filter(is_active=True)
        self.fields['building_id'].queryset = Building.objects.filter(state=True)
        self.fields['type_resource'].queryset = Classification.objects.filter(state=True)

    class Meta:
        model = Unit
        fields = ['number', 'meter_qty', 'flat', 'rent_price', 'renter',
                  'init_date', 'name', 'type_resource', 'building_id',
                  'renovation_date', 'expiration_date', 'description']
        labels = {
            'name': 'Name',
            'init_date': 'Contract start date',
            'number': 'Number of unit',
            'meter_qty': 'M2',
            'rent_price': 'Price of rent',
            'expiration_date': 'Contract expiration date',
            'renovation_date': 'Contract renovation date',
            'renter': 'Renter',
            'building_id': 'Building',
            'type_resource': 'Property type',
            'description': 'Description',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Unit name ...',
                    'id': 'name',
                    'class': 'form-control',
                }),
            'init_date': forms.DateInput(
                format=('%d-%m-%Y'),
                attrs={
                    'placeholder': 'dd/mm/aaaa',
                    'id': 'init_date',
                    'class': 'form-control',
                }),
            'number': forms.TextInput(
                attrs={
                    'placeholder': 'Unit ...',
                    'class': 'form-control',
                    'id': 'number'
                }),
            'flat': forms.TextInput(
                attrs={
                    'placeholder': 'Flat ...',
                    'class': 'form-control',
                    'id': 'flat'
                }),
            'meter_qty': forms.NumberInput(
                attrs={
                    'id': 'meter_qty',
                    'class': 'form-control',
                }),
            'rent_price': forms.NumberInput(
                attrs={
                    'id': 'rent_price',
                    'class': 'form-control',
                }),
            'expiration_date': forms.DateInput(
                format=('%d-%m-%Y'),
                attrs={
                    'placeholder': 'dd/mm/aaaa',
                    'id': 'expiration_date',
                    'class': 'form-control',
                }),
            'renovation_date': forms.DateInput(
                format=('%d-%m-%Y'),
                attrs={
                    'placeholder': 'dd/mm/aaaa',
                    'id': 'renovation_date',
                    'class': 'form-control',
                }),
            'description': forms.Textarea(
                attrs={
                    'id': 'description',
                    'class': 'form-control',
                }),

        }


class commonExpensesForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(commonExpensesForm, self).__init__(*args, **kwargs)
        self.fields['building'].queryset = Building.objects.filter(state=True)

    class Meta:
        model = CommonExpenses
        fields = ['building', 'payment_date', 'total_amount']
        labels = {
            'building': 'Building',
            'payment_date': 'Payment date',
            'total_amount': 'Amount',
        }
        widgets = {
            'payment_date': forms.DateInput(
                format=('%d-%m-%Y'),
                attrs={
                    'placeholder': 'dd/mm/aaaa',
                    'class': 'form-control',
                    'id': 'payment_date'
                }),
            'total_amount': forms.NumberInput(
                attrs={
                    'id': 'total_amount',
                    'class': 'form-control',
                }),
        }


class commonExpensesLinesForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(commonExpensesLinesForm, self).__init__(*args, **kwargs)
        self.fields['concept'].queryset = Services.objects.filter(state=True)

    class Meta:
        model = CommonExpensesLines
        fields = ['concept', 'amount', 'common_expenses']
        labels = {
            'concept': 'Concept',
            'common_expenses': 'Concept expenses',
            'amount': 'Amount',
        }
        widgets = {
            'amount': forms.NumberInput(
                attrs={
                    'id': 'amount',
                    'class': 'form-control',
                }),
        }

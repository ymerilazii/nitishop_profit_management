from django import forms
from datetime import date

today = date.today()

class InputValues(forms.Form):
    f_date = forms.DateField(label="Data",widget=forms.DateInput(format='%d/%m/%Y',attrs={'class':'form-control',}),input_formats=('%d/%m/%Y', ), initial=today,)
    f_cashbox = forms.DecimalField(label="Arka",max_digits=9, decimal_places=2,widget=forms.NumberInput(attrs={'class':'form-control'}))
    f_withdraw = forms.DecimalField(label="Terheqje",max_digits=9, decimal_places=2,widget=forms.NumberInput(attrs={'class':'form-control'}))
    f_remain = forms.DecimalField(label="Mbetje",max_digits=9, decimal_places=2,widget=forms.NumberInput(attrs={'class':'form-control'}))
    f_sale = forms.DecimalField(label="Shitje",max_digits=9, decimal_places=2,widget=forms.NumberInput(attrs={'class':'form-control'}))
    f_profit = forms.DecimalField(label="Profit",max_digits=9, decimal_places=2,widget=forms.NumberInput(attrs={'class':'form-control'}))
    f_neto = forms.DecimalField(label="Neto",max_digits=9, decimal_places=2,widget=forms.NumberInput(attrs={'class':'form-control'}))
    f_expense = forms.DecimalField(label="Shpenzimet",max_digits=9, decimal_places=2,widget=forms.NumberInput(attrs={'class':'form-control'}))

#### BASIC PAGE MAIN #####
class EndOfDay(forms.Form):
    f_date = forms.DateField(label="Data", widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control', }),input_formats=('%d/%m/%Y',), initial=today)
    f_cashbox = forms.DecimalField(label="Arka", max_digits=9, decimal_places=2,widget=forms.NumberInput(attrs={'class': 'form-control'}),required=False)
    f_withdraw = forms.DecimalField(label="Terheqje", max_digits=9, decimal_places=2,widget=forms.NumberInput(attrs={'class': 'form-control'}),required=False)

    def clean_f_cashbox(self):
        data = self.cleaned_data['f_cashbox']
        if not data:
            data = 0.00
        return data

    def clean_f_withdraw(self):
        data = self.cleaned_data['f_withdraw']
        if not data:
            data = 0.00
        return data

class ExpenseAdd(forms.Form):
    f_date = forms.DateField(label="Data", widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control', }),input_formats=('%d/%m/%Y',), initial=today)
    f_expense = forms.DecimalField(label="Shpenzimet", max_digits=9, decimal_places=2,widget=forms.NumberInput(attrs={'class': 'form-control'}),required=False)

    def clean_f_expense(self):
        data = self.cleaned_data['f_expense']
        if not data:
            data = 0.00
        return data

class DateChoose(forms.Form):
    month_choices = [
        (1,'Janar'),
        (2,'Shkurt'),
        (3, 'Mars'),
        (4, 'Prill'),
        (5, 'Maj'),
        (6, 'Qershor'),
        (7, 'Korrik'),
        (8, 'Gusht'),
        (9, 'Shtator'),
        (10,'Tetor'),
        (11, 'Nentor'),
        (12, 'Dhjetor'),
    ]
    this_month= forms.IntegerField(label='Muaji?',widget=forms.Select(choices=month_choices,attrs={'class': 'form-control'}))
    this_year= forms.IntegerField(label='Viti?',initial=2020,widget=forms.NumberInput(attrs={'class': 'form-control'}))
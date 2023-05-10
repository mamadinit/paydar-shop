from django import forms


class Add2CartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=9, widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                                            'placeholder': 'quantity'}))


class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':' کد تخفیف '}), label='')
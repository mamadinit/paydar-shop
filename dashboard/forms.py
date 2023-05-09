from django import forms
from account.models import User


class DashboardInfoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super(DashboardInfoForm, self).__init__(*args, **kwargs)
        if not user.is_superuser:
            self.fields['phone'].disabled = True

    class Meta():
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone', 'bank_card']        
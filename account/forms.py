
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import get_user_model
from .models import User, Address



UserModel = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    phone = forms.RegexField(regex = '^0\d{10}$', required=True,
                            error_messages = {
                                    'required': 'شماره موبایل اجباری است',
                                    'invalid' : 'شماره موبایل باید در فورمت 09000000000 با 11 رقم باشد .'
                                }
                            )                        
    class Meta:
        model = UserModel
        fields = ('phone','first_name', 'last_name', 'email','password1', 'password2')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = UserModel
        fields = ('phone',)

class CustomPasswordResetForm(PasswordResetForm):
    pass

class VerifyForm(forms.Form):
    otp_code = forms.CharField(label='Code', max_length=6, required=True,
                        error_messages = {
                            'required' : 'کد تایید اجباری است',
                            'max_length' : 'پیش از حد مجاز'
                        }
    
                    )
    

class AddressUpdateForm(forms.ModelForm):
    class Meta():
        model = Address
        fields = ['province', 'city', 'postal_code', 'address', 'transferee_name']     

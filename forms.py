from django.forms import ModelForm, inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from  django.contrib.auth.models import User
from django import forms

from .models import Customer, Address, SignUp


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        exclude = ()


class AddressForm(ModelForm):
    class Meta:
        model = Address
        exclude = ()


AddressFormSet = inlineformset_factory(Customer, Address,
                                            form=AddressForm, extra=1)


class SignUpForm(UserCreationForm):
       first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
       last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
       email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')


class Meta:
    model = SignUp
    fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
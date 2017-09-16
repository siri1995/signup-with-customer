from django.core.urlresolvers import reverse
from django.db import models
from .validators import *


class ContactInfo(models.Model):
    mobile_number = models.CharField(max_length=20, validators=[validate_mobile_number])
    phone_number = models.CharField(max_length=20, validators=[validate_phone_number])
    email_id = models.EmailField(max_length=50)

class Customer(ContactInfo):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, validators=[validate_first_name])
    last_name = models.CharField(max_length=20, validators=[validate_last_name])

def get_absolute_url(self):
        return reverse('customer-update', kwargs={'pk': self.pk})


class Address(models.Model):
        customer_id = models.ForeignKey(Customer)
        address_id = models.AutoField(primary_key=True)
        address1 = models.CharField(max_length=100, blank=True, null=True)
        address2 = models.CharField(max_length=100, blank=True, null=True)
        city = models.CharField(max_length=20, blank=True, null=True, validators=[validate_city])
        state = models.CharField(max_length=20, blank=True, null=True, validators=[validate_state])
        landmark = models.CharField(max_length=20, blank=True, null=True, validators=[validate_landmark])
        pincode = models.IntegerField(blank=True, null=True)


class SignUp(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)



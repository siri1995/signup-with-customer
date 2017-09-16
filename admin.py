from django.contrib import admin
from .models import Customer, Address,ContactInfo, SignUp

admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(ContactInfo)
admin.site.register(SignUp)



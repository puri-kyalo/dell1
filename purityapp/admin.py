from django.contrib import admin
from purityapp.models import Member, Products, Appointment, Ordered, ImageModel

# Register your models here.
admin.site.register(Member)
admin.site.register(Products)
admin.site.register(Appointment)
admin.site.register(Ordered)
admin.site.register(ImageModel)

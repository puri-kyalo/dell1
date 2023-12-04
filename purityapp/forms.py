from django import forms
from purityapp.models import Products, ImageModel
from purityapp.models import Appointment
from purityapp.models import Ordered
class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'price', 'description', 'origin', 'color']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'phone', 'date', 'department', 'doctor', 'message']

class OrderedForm(forms.ModelForm):
    class Meta:
        model = Ordered
        fields = ['name', 'phone', 'quantity', 'delivery_date']

class ImagesUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['image', 'title', 'price']




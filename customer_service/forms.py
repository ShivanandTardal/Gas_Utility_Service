from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'details', 'attachments']

class RequestUpdateForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['status']

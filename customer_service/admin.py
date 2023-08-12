from django.contrib import admin
from .models import ServiceRequest, Attachment

admin.site.register(ServiceRequest)
admin.site.register(Attachment)

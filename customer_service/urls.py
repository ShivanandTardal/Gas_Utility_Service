from django.urls import path
from . import views

urlpatterns = [
    path('', views.submit_request, name='submit_request'),
    path('view/<int:request_id>/', views.view_request, name='view_request'),
    path('request/<int:request_id>/', views.view_request, name='view_request'),
    path('request/<int:request_id>/update/', views.update_request, name='update_request'),
    path('request_submitted/', views.request_submitted, name='request_submitted'),
    path('request_updated/', views.request_updated, name='request_updated'),
]
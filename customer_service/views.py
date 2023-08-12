from django.shortcuts import render, redirect
from .forms import ServiceRequestForm, RequestUpdateForm
from .models import ServiceRequest

def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('request_submitted')
    else:
        form = ServiceRequestForm()
    return render(request, 'submit_request.html', {'form': form})

def view_request(request, request_id):
    service_request = ServiceRequest.objects.get(id=request_id)
    return render(request, 'view_request.html', {'service_request': service_request})

def update_request(request, request_id):
    service_request = ServiceRequest.objects.get(id=request_id)
    if request.method == 'POST':
        form = RequestUpdateForm(request.POST, instance=service_request)
        if form.is_valid():
            form.save()
            return redirect('request_updated')
    else:
        form = RequestUpdateForm(instance=service_request)
    return render(request, 'update_request.html', {'form': form, 'service_request': service_request})


def request_submitted(request):
    return render(request, 'request_submitted.html')

def request_updated(request):
    return render(request, 'request_updated.html')



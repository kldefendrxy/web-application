from django.shortcuts import render

# Create your views here.

from .models import Patient, Ward, Stay

def index(request):
    patients = Patient.objects.all()
    stays = Stay.objects.select_related('patient', 'ward').all()
    wards = Ward.objects.all()
    context = {
        'patients': patients,
        'stays': stays,
        'wards': wards
    }
    return render(request, 'btest/index.html', context)

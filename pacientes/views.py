from django.shortcuts import render, get_object_or_404
from .models import Paciente


def home(request):
    pacientes = Paciente.objects.all()
    return render(request, 'home.html', {'pacientes': pacientes})


def about(request):
    return render(request, 'about.html')


def patient_description(request, pk):
    pacientes = get_object_or_404(Paciente, pk=pk)
    return render(request, 'patient.html', {'pacientes': pacientes})

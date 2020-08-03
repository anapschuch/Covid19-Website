from django.shortcuts import render, get_object_or_404
from .models import Paciente


def home(request):
    pesquisar = request.GET.get('pesquisar')
    if pesquisar is not None:
        pacientes = Paciente.objects.filter(nome__startswith=pesquisar).order_by('nome')
        if len(pesquisar) == 0:
            pesquisar = "Nome"
    else:
        pacientes = Paciente.objects.all().order_by('nome')
        pesquisar = "Nome"
    return render(request, 'home.html', {'pacientes': pacientes, 'pesquisar': pesquisar})


def about(request):
    return render(request, 'about.html')


def home_logged(request):
    return render(request, 'home-logged-user.html')


def patient_description(request, pk):
    pacientes = get_object_or_404(Paciente, pk=pk)
    return render(request, 'patient.html', {'pacientes': pacientes})

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Paciente
from .forms import InsertPatient
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required
def patient_edit(request):
    """Returns the patient editor."""
    pesquisar = request.GET.get('pesquisar')

    if pesquisar is not None:
        if len(pesquisar) == 0:
            pesquisar = None

    if pesquisar is not None:
        pacientes = Paciente.objects.filter(nome__startswith=pesquisar).order_by('nome')
    else:
        pacientes = Paciente.objects.all().order_by('nome')
        pesquisar = "Nome"
        paginator = Paginator(pacientes, 15)
        page = request.GET.get('page', 1)

        try:
            pacientes = paginator.page(page)
        except PageNotAnInteger:
            pacientes = paginator.page(1)
        except EmptyPage:
            pacientes = paginator.page(paginator.num_pages)

    return render(request, 'patient_edit.html', {'pacientes': pacientes, 'pesquisar': pesquisar})


def about(request):
    return render(request, 'about.html')


@login_required
def home_logged(request):
    return render(request, 'home-logged-user.html')


@login_required
def patient_insertion(request):
    
    if request.method == 'POST':
        form = InsertPatient(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Paciente inserido com sucesso!')
            return redirect('patient_insertion')
    else:
        form = InsertPatient()
    return render(request, 'patient_new.html', {'form': form})


@login_required
def patient_description(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    remove = request.GET.get('delete')
    
    if remove is not None:
        paciente.delete()
        return redirect('patient_edit')
    
    if request.method == 'POST':
        patient_form = InsertPatient(request.POST, instance=paciente)
        if patient_form.is_valid():
            patient_form.save()
            messages.success(request, f'Paciente editado com sucesso!')
    else:
        patient_form = InsertPatient(instance=paciente)
    return render(request, 'patient.html', {'form': patient_form})

from django.shortcuts import render, get_object_or_404
from .models import Person


def home(request):
    patients = Person.objects.all()
    return render(request, 'home.html', {'patients': patients})


def about(request):
    return render(request, 'about.html')


def board_topics(request, pk):
    patients = get_object_or_404(Person, pk=pk)
    return render(request, 'patient.html', {'patients': patients})

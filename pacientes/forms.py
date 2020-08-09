from django import forms
from .models import Paciente

class PostForm(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = ['nome', 'idade', 'temperatura_maxima', 'data_inicio_sintomas']
from django.shortcuts import render
from pacientes.models import Paciente
import pandas as pd
import matplotlib.pyplot as plt

#Define constants:
LIMIT = 10000

# Create your views here.
def query_home (request):
    '''
    From url: r'^consultar-dados$'
    Description: View to query and visualize data.
    '''
    return render(request, 'query_home.html')

def return_results (request):
    ''' r'^consultar-dados$' '''
    param = request.GET['param']
    type   = request.GET['type']
    print(param)
    print(type)
    #Uses Paciente's manager (called objects) to retrieve all Paciente's instances:
    all_patients = Paciente.objects.all()[:LIMIT].values() #List of dictionaries.
    table        = pd.DataFrame(all_patients)
    table[param].hist()
    plt.savefig('static/plots/graph.png')
    return render(request, 'query_home.html')
    #return render(request, 'show_results.html', {'table':table})

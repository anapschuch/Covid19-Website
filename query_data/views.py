import io
from django.shortcuts import render
from django.http      import FileResponse
from pacientes.models import Paciente
import matplotlib.pyplot as plt, mpld3
import pandas            as pd
from reportlab.pdfgen        import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus      import SimpleDocTemplate, Table

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
    #Uses Paciente's manager (called objects) to retrieve all Paciente's instances:
    all_patients = Paciente.objects.all()[:LIMIT].values() #List of dictionaries.
    table        = pd.DataFrame(all_patients)
    table.drop("nome", axis=1, inplace=True) #Eliminates the column 'nome'.
    if type == 'hist':
        fig = plt.figure()
        table[param].hist()
        histogram = mpld3.fig_to_html(fig)
        context = {'histogram':histogram, 'type':type}
        return render(request, 'show_results.html', context)
    elif type == 'line_listing':
        #Transform table from DataFrame to a list of lists:
        data      = table.to_string(index=False).splitlines()
        data_copy = data.copy()
        data      = []
        #First line:
        first_line = []
        for word in data_copy[0].split():
            first_line.append(word.upper().replace('_', ' '))
        data.append(first_line)
        for n, line in enumerate(data_copy):
            if n > 0:
                data.append(line.split())
        buffer = io.BytesIO() # Create a file-like buffer to receive PDF data.
        pdf = SimpleDocTemplate(
        buffer,
        pagesize=letter
        )
        table_list = Table(data)
        pdf.build([table_list])
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=False, filename='line_list_COVID19.pdf')

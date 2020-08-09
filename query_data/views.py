import io
from django.shortcuts import render, redirect
from django.http      import FileResponse
from django.contrib   import messages
from pacientes.models import Paciente
import matplotlib.pyplot as plt, mpld3
import pandas            as pd
from reportlab.lib           import colors
from reportlab.pdfgen        import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus      import SimpleDocTemplate, Table, TableStyle

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
    if len(all_patients) == 0:#There are no patients
        messages.add_message(request, messages.ERROR, 'Não há pacientes cadastrados no banco de dados.')
        return redirect('no_results')
    table        = pd.DataFrame(all_patients)
    table.drop("nome", axis=1, inplace=True) #Eliminates the column 'nome'.
    if type == 'hist': #Returns the histogram.
        fig = plt.figure()
        label = param.upper().replace('_', ' ')
        if param == "temperatura_maxima":
            label = ''.join([label, "(°C)"])
        table[param].hist(bins=30)
        plt.xlabel(label)
        plt.ylabel('Frequência')
        plt.title('Histograma')
        histogram = mpld3.fig_to_html(fig)
        context = {'histogram':histogram, 'type':type}
        return render(request, 'show_results.html', context)
    elif type == 'line_listing': #Returns the line-list.
        #Transform table from DataFrame to a list of lists:
        data      = table.to_string(index=False).splitlines()
        data_copy = data.copy()
        data      = []
        #First line:
        first_line = []
        for word in data_copy[0].split():
            if word == "temperatura_maxima":
                word = ''.join([word, "(°C)"])
            first_line.append(word.upper().replace('_', ' '))
        data.append(first_line)
        for n, line in enumerate(data_copy):
            if n > 0:
                data.append(line.split())
        buffer = io.BytesIO() # Create a file-like buffer to receive PDF data.
        pdf = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        title="Line List COVID - 19",
        )
        table_list = Table(data, repeatRows=1)
        #Set style:
        style = TableStyle([
            ('FONTNAME', (0, 0), (-1, 0), 'Times-Bold'),   #Font name of the first line.
            ('FONTNAME', (0, 1), (-1, -1), 'Times-Roman'), #Font name of the remaining table.
            ('FONTSIZE', (0, 0), (-1, 0), 12),  #Font size of the first line.
            ('FONTSIZE', (0, 1), (-1, -1), 10),  #Font size of the remaining table.
            ('GRID', (0, 0), (-1, -1), 2, colors.black),
        ])
        table_list.setStyle(style)
        title = "Line Listing COVID - 19"
        pdf.build([table_list])
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=False, filename='line_list_COVID19.pdf')


def no_results (request):
    return render(request, 'query_home_no_results.html')

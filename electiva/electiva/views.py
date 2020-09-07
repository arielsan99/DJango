import matplotlib
matplotlib.use('Agg') #para evitar que se apague el servidor
from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
import pdfkit as pdf
from electiva.model.estadisticos import Estadisticos
def index(request):
    return render(request,'index.html')

def reporte(request):
        if request.method=='POST':
            nombre = request.POST['name_stadistic'] #obtenemos el valor del campo estadistico
            curso = request.POST['curso']
            periodo = request.POST['periodo']
            csv = request.FILES['csv']
            e = Estadisticos(csv)
            datos,i = e.begin()
            document = {"datos":datos,"nombre":nombre,"periodo":periodo,"curso":curso,"i":i}
            template = get_template('pdf.html')
            html = template.render(document)
            options = {
                'page-size': 'Letter',
                'encoding': "UTF-8",
                'quiet': '',
            }
            pdfile = pdf.from_string(html,False,options)
            response = HttpResponse(pdfile, content_type='application/pdf')
            response['Content-Disposition'] = ' filename="reporte.pdf"'
            return response

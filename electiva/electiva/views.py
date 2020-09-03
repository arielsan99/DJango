from django.shortcuts import render
import pandas as pd
def index(request):
    return render(request,'index.html')

def previo(request):
    if request.method=='POST':
        nombre = request.POST['name_stadistic'] #obtenemos el valor del campo estadistico
        curso = request.POST['curso']
        periodo = request.POST['periodo']
        csv = request.FILES['csv']
        lista = pd.read_csv(csv,sep=';')
        dFrame = pd.DataFrame(lista) #Leemos el csv y lo convertimos a DataFrame
        print(dFrame.describe())
        numFilas = dFrame.count(axis=0)[0] #obtenemos la cantidad de filas
        numColumns = dFrame.count(axis=1)[0]  #obtenemos la cantidad de columnas
        document = {"nombre":nombre,"numFilas":numFilas,"numColumns":numColumns,"nombre":nombre,"periodo":periodo,"dFrame":lista}
        return render(request,'previo.html',document)

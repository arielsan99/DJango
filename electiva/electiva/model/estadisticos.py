import pandas as pd
from electiva.model.Graficas import Graficas
class Estadisticos:
    def __init__(self,csv):
        self.dFrame = None
        self.csv = csv
        self.cabecera = []
        self.tamCabecera=0

        self.medias=[]
        self.varianzas=[]
        self.promedioCurso=0
        self.promedioEstudiantes=[]
        self.modaCurso=0
        self.modas=[]
        self.promMax=0
        self.promMin=0

    def begin(self):
        self.dFrame=pd.read_csv(self.csv,sep=';')
        self.cabecera=list(self.dFrame)
        self.tamCabecera = len(self.cabecera)
        for n in range(1,self.tamCabecera):
            notas = self.dFrame[self.cabecera[n]]
            media = float("{0:.2f}".format(self.media(notas)))
            self.medias.append(media)
            varianza = float("{0:.2f}".format(self.varianza(notas,media)))
            self.varianzas.append(varianza)
            self.modas.append(self.moda(notas)[0])
        self.modaCurso=self.moda(pd.DataFrame(self.modas))[0][0]
        self.cpromediosEstudiantes()
        self.promedioCurso = float("{0:.2f}".format(self.media(self.promedioEstudiantes)))
        g = Graficas()
        image = g.plot(self.medias,self.varianzas,self.cabecera[1::])
        return [self.promedioCurso,self.modaCurso,self.promMax,self.promMin],image

    def media(self,notas):
        sum=0
        for i in notas:
            sum+=i
        return sum/len(notas)

    def varianza(self,notas,mu):
        sum = 0
        for i in notas:
            sum+=(i-mu)**2
        return sum/len(notas)

    def moda(self,notas):
        return notas.mode()

    def cpromediosEstudiantes(self):
        prom = list(self.dFrame.median(axis=1))
        self.promMax=max(prom)
        self.promMin=min(prom)
        self.promedioEstudiantes=prom

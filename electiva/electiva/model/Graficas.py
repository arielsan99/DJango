import matplotlib.pyplot as plt
import base64
from io import BytesIO
import numpy as np
from scipy import stats
class Graficas:

    def plot(self,mu,var,materias):

        x = np.linspace(-20,90, 100)

        for i in range(len(mu)):
            normal = stats.norm(mu[i], var[i])
            fp = normal.pdf(x) # Función de Probabilidad
            plt.plot(x, fp)
        plt.legend(materias);
        plt.title('Distribución Normal')
        plt.ylabel('probabilidad')
        plt.xlabel('Notas')
        #plot sth

        tmpfile = BytesIO()
        plt.savefig(tmpfile, format='png')
        encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')
        html = '<img src=\'data:image/png;base64,{}\' style=\'width: 100%;\'>'.format(encoded)
        return html

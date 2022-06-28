from DataManager import *
from Ahumada import *
import csv

from Farmazon import Farma
from Remedios import medicamentos
from Simi import Simi
from UFprice import getUFprice
from Funciones import *

def main():

    remedios = read_txt("principios_activos.txt")

    Ahumada(remedios)
    #Simi(remedios)
    #Farma(remedios)
    getUFprice()

    with open('Medicamentos.csv', 'w') as Medicamentos_csv:
        writer = csv.writer(Medicamentos_csv)
        for x in medicamentos:
            writer.writerow([x.activo, x.farmacia, x.descripcion, x.precioClp, x.precioUf])
    Csv('Medicamentos.csv')
    for Principio_Activo in remedios:
        Promedio_Activo(Principio_Activo)
        Promedio_Activo_Farmacia(Principio_Activo, "Ahumada")
        #Promedio_Activo_Farmacia(Principio_Activo, "Simi")
        #Promedio_Activo_Farmacia(Principio_Activo, "Farma")
        Minimo_Farmacia(Principio_Activo, "Ahumada")
        #Minimo_Farmacia(Principio_Activo, "Simi")
        #Minimo_Farmacia(Principio_Activo, "Farma")
        Minimo_Activo(Principio_Activo)
        maxBulto(Principio_Activo,remedios)

if __name__ == "__main__":
    main()

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
        Minimo_Farmacia(Principio_Activo, "Ahumada")

if __name__ == "__main__":
    main()

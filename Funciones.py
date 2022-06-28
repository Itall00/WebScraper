import pandas as pd

from Remedios import medicamentos
from functools import reduce
import functools

def Csv(Nombre):
    df = pd.read_csv(Nombre, encoding = 'latin')
    df.columns=['Principio Activo', 'Farmacia', 'Descripción', 'Precio en Pesos Chilenos', 'Precio en UF']
    df= df[df['Precio en Pesos Chilenos'] != 0.0]
    df.to_csv('Medicamentos.csv', index=False)

def Promedio_Activo(Input_Activo):

    activos_filtrados=list(filter(lambda x: x.activo == Input_Activo, medicamentos))
    print(f"El precio en CLP del activo {Input_Activo} es: ")
    print(reduce(lambda suma, p: suma + p.precioClp, activos_filtrados,0)/len(activos_filtrados),"\n")
    print(f"El precio en UF del activo {Input_Activo} es: ")
    print(reduce(lambda suma, p: suma + p.precioUf, activos_filtrados,0)/len(activos_filtrados),"\n")

    

def Minimo_Farmacia(Input_Activo, Input_Farmacia):
    activos_filtrados = list(filter(lambda x: x.activo == Input_Activo and x.farmacia == Input_Farmacia, medicamentos))
    Minimo_Farmacia = min(activos_filtrados, key=lambda value: value.precioClp)
    print("\n", Minimo_Farmacia.activo, Minimo_Farmacia.farmacia, Minimo_Farmacia.descripcion, Minimo_Farmacia.precioClp, Minimo_Farmacia.precioUf)
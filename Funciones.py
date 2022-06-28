from Remedios import medicamentos
from functools import reduce
import functools
import pandas as pd

def Csv(Nombre):
    df = pd.read_csv(Nombre, encoding = 'latin')
    df.columns=['Principio Activo', 'Farmacia', 'Descripción', 'Precio en Pesos Chilenos', 'Precio en UF']
    df= df[df['Precio en Pesos Chilenos'] != 0.0]
    df.to_csv('Remedios.csv', index=False)

def Promedio_Activo(Input_Activo):

    activos_filtrados=list(filter(lambda x: x.activo == Input_Activo, medicamentos))
    print(f"El precio en CLP del activo {Input_Activo} es: ")
    print(reduce(lambda suma, p: suma + p.precioClp, activos_filtrados,0)/len(activos_filtrados),"\n")
    print(f"El precio en UF del activo {Input_Activo} es: ")
    print(reduce(lambda suma, p: suma + p.precioUf, activos_filtrados,0)/len(activos_filtrados),"\n")


def Maximo_Precio(Input_Activo):
    print (reduce(lambda a,b : a if a > b else b,medicamentos))


    

    
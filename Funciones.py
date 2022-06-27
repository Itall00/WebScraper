from Remedios import medicamentos
from functools import reduce


def Promedio_Activo(Input_Activo):

    activos_filtrados=list(filter(lambda x: x.activo == Input_Activo, medicamentos))
    print(f"El precio en CLP del activo {Input_Activo} es: ")
    print(reduce(lambda suma, p: suma + p.precioClp, activos_filtrados,0)/len(activos_filtrados),"\n")
    print(f"El precio en UF del activo {Input_Activo} es: ")
    print(reduce(lambda suma, p: suma + p.precioUf, activos_filtrados,0)/len(activos_filtrados),"\n")
from Remedios import medicamentos
from functools import reduce


def Promedio_Activo(Input_Activo):

    activos_filtrados=list(filter(lambda x: x.activo == Input_Activo, medicamentos))
    print(f"El precio promedio en CLP del activo {Input_Activo} es: ")
    print(reduce(lambda suma, p: suma + p.precioClp, activos_filtrados,0)/len(activos_filtrados),"\n")
    print(f"El precio promedio en UF del activo {Input_Activo} es: ")
    print(reduce(lambda suma, p: suma + p.precioUf, activos_filtrados,0)/len(activos_filtrados),"\n")

def Promedio_Activo_Farmacia(Input_Activo,Input_Farmacia):

    activos_filtrados = list(filter(lambda x: x.activo == Input_Activo and x.farmacia == Input_Farmacia, medicamentos))
    print(f"El precio promedio en CLP del activo {Input_Activo} y de la farmacia {Input_Farmacia} es: ")
    print(reduce(lambda suma, p: suma + p.precioClp, activos_filtrados,0)/len(activos_filtrados),"\n")
    print(f"El precio promedio en UF del activo {Input_Activo} y de la farmacia {Input_Farmacia} es: ")
    print(reduce(lambda suma, p: suma + p.precioUf, activos_filtrados,0)/len(activos_filtrados),"\n")


def Minimo_Farmacia(Input_Activo, Input_Farmacia):#precio minimo en la farmacia seleccionada
    activos_filtrados = list(filter(lambda x: x.activo == Input_Activo and x.farmacia == Input_Farmacia, medicamentos))
    Minimo_Farmacia = min(activos_filtrados, key=lambda value: value.precioClp)
    print("Principio Activo: ", Minimo_Farmacia.activo, "\nFarmacia: ", Minimo_Farmacia.farmacia, "\nDescripcion: ",Minimo_Farmacia.descripcion,"\nPrecio min CLP: " ,Minimo_Farmacia.precioClp, "\nPrecio min UF: " ,Minimo_Farmacia.precioUf)

def Maximo_Farmacia(Input_Activo, Input_Farmacia):#precio maximo en la farmacia seleccionada
    activos_filtrados = list(filter(lambda x: x.activo == Input_Activo and x.farmacia == Input_Farmacia, medicamentos))
    Maximo_Farmacia = max(activos_filtrados, key=lambda value: value.precioClp)
    print("Principio Activo: ", Maximo_Farmacia.activo, "\nFarmacia: ", Maximo_Farmacia.farmacia, "\nDescripcion: ",Maximo_Farmacia.descripcion,"\nPrecio min CLP: " ,Maximo_Farmacia.precioClp, "\nPrecio min UF: " ,Maximo_Farmacia.precioUf)

def Minimo_Activo(Input_Activo):#precio minimo entre todas las farmacias
    activos_filtrados = list(filter(lambda x: x.activo == Input_Activo, medicamentos))
    Minimo = min(activos_filtrados, key=lambda value: value.precioClp)
    print("\n", Minimo.activo, Minimo.farmacia, Minimo.descripcion, Minimo.precioClp, Minimo.precioUf)

def Maximo_Activo(Input_Activo):#precio maximo entre todas las farmacias
    activos_filtrados = list(filter(lambda x: x.activo == Input_Activo, medicamentos))
    Maximo = max(activos_filtrados, key=lambda value: value.precioClp)
    print("\n", Maximo.activo, Maximo.farmacia, Maximo.descripcion, Maximo.precioClp, Maximo.precioUf)

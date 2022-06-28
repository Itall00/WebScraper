def read_txt(archivo):

    with open(archivo, "r", encoding="utf8") as activos:
        lines = activos.read().split('\n')

    return lines
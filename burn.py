from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from base64 import urlsafe_b64encode, urlsafe_b64decode

clave = "SC2SC2SC2SC2SC2SC2SC2" 

def generate_key(clave):
    clave = hashes.Hash(hashes.SHA256(), backend=default_backend()).update(clave).finalize()
def encrypt(key,file):
    return False
def replace_file(file):
    return False

def main(file):
    key=generate_key(clave)
    encrypt(key,file)
    replace_file(file)
    return True

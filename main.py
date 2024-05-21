import os

import app.seal as seal
from app.burn import Encrypter
from app.discover import Discover

extensiones = ["pptx", "xlsx", "docx", "txt"]
extensiones_encriptados = ["sc2"]
origen = "./tests"
key_path = "./app/keys/"


def main():
    discover = Discover(origen)
    archivos = discover.find_files(extensiones)
    archivos_encriptados = discover.find_files(extensiones_encriptados)

    print(f"files found:\n {archivos}")

    ### path of keyfiles
    public = ""
    private = ""

    print("searching keys...")
    keyFiles = os.listdir(key_path)

    if len(keyFiles) > 1:
        print("key files founded!")

    else:
        print("no keys found... creating new ones...")
        public, private = seal.non_volatile_key()
        print("keys created!")

    print(public, private)

    respuesta = input("que quieres hacer?\n1) encriptar\n2)desencriptar\n").strip()
    print(respuesta)
    encripter = Encrypter(public, private)
    if respuesta == "0":
        encriptar(encripter, archivos)
    else:
        desencriptar(encripter, archivos_encriptados)


def desencriptar(encripter: Encrypter, archivos):
    for item in archivos:
        encripter.decrypt(item)


def encriptar(encripter, archivos):

    for item in archivos:
        encripter.encrypt(item)


if __name__ == "__main__":
    main()

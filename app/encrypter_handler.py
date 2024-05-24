import os

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa


def create_keys(key_path):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend(),
    )

    public_key = private_key.public_key()

    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )

    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )

    with open(os.path.join(key_path, "private_key.pem"), "wb") as private_key_file:
        private_key_file.write(private_key_pem)

    with open(os.path.join(key_path, "public_key.pem"), "wb") as public_key_file:
        public_key_file.write(public_key_pem)


class Encryption:
    def __init__(self, key_path) -> None:
        self.key_path = key_path
        keys = os.listdir(self.key_path)

        if len(keys) < 1:
            create_keys(self.key_path)
        else:
            print("encryption keys already exist, no need to create new ones")

        if "public" in keys[0]:
            self.public_key = f"{key_path}/{keys[0]}"
            self.private_key = f"{key_path}/{keys[1]}"
        else:
            self.public_key = f"{key_path}/{keys[1]}"
            self.private_key = f"{key_path}/{keys[0]}"

    def encrypt_file(self, file_path):
        with open(file_path, "rb") as file:
            data = file.read()

        with open(self.public_key, "rb") as key_file:
            public_key = serialization.load_pem_public_key(
                key_file.read(), backend=default_backend()
            )

        encrypted_data = public_key.encrypt(
            data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )

        return encrypted_data

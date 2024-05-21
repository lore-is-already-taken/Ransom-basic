from typing import Tuple

from Crypto.PublicKey import RSA

key_location = "./app/keys"


def non_volatile_key() -> Tuple[str, str]:
    """
    Generate a pair of keys wich are stored in textfiles
    """
    path_to_private_key = f"{key_location}/priv.pem"
    path_to_public_key = f"{key_location}/public.pem"

    key = RSA.generate(2048)

    private_key = key.export_key()
    public_key = key.publickey().export_key()

    with open(path_to_private_key, "wb") as f:
        f.write(private_key)

    with open(path_to_public_key, "wb") as f:
        f.write(public_key)

    return path_to_private_key, path_to_public_key


def volatile_key() -> tuple[bytes, bytes]:
    """
    Generate a pair of keys wich are only stored in memory.
    Returns a tuple of [priv_key,pub_key]
    """
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    return private_key, public_key

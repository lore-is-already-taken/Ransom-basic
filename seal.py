from Crypto.PublicKey import RSA

def non_volatile_key():
    """
    Generate a pair of keys wich are stored in textfiles
    """
    key = RSA.generate(2048)
    private_key = key.export_key()
    with open("priv.pem","wb") as f:
        f.write(private_key)
    
    public_key = key.publickey().export_key()
    with open("seal.pem","wb") as f:
        f.write(public_key)

def volatile_key()->tuple[bytes,bytes]:
    """
    Generate a pair of keys wich are only stored in memory.
    Returns a tuple of [priv_key,pub_key]
    """
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    return private_key,public_key

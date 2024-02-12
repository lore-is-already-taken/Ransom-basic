from Crypto.PublicKey import RSA

def main():
    key = RSA.generate(2048)
    private_key = key.export_key()
    with open("priv.pem","wb") as f:
        f.write(private_key)
    
    public_key = key.publickey().export_key()
    with open("seal.pem","wb") as f:
        f.write(public_key)

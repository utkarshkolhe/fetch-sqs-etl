from Crypto.PublicKey import RSA
from src.cryptography.masking import Masking


# Generate RSA keys
private_key = RSA.generate(1024)
public_key = private_key.publickey()
# Export public key
with open("public_key.pem", 'wb') as f:
    f.write(private_key.publickey().export_key(format="PEM"))

# Export private key
with open("private_key.pem", 'wb') as f:
    f.write(private_key.export_key(format="PEM"))


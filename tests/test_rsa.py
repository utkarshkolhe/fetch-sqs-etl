import pytest
from src.cryptography.masking import Masking 
import src.constants as constants
from Crypto.PublicKey import RSA
from unittest.mock import MagicMock, patch

def test_postgres_rsa():
    # Load public key from file
    with open(constants.RSA_PUBLIC_KEY_LOCATION, 'rb') as f:
        public_key = RSA.import_key(f.read())

    # Load private key from file
    with open(constants.RSA_PRIVATE_KEY_LOCATION, 'rb') as f:
        private_key = RSA.import_key(f.read())

    Masking.setMasker("RSA",public_key,private_key)
    records = []

    data = "1.1.1.1"
    # Encrypt the data
    encrypted_data = Masking.mask(data)

    # Decrypt the datapython 
    decrypted_data = Masking.demask(encrypted_data)

    assert data == decrypted_data
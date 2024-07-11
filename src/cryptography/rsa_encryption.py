from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64encode,b64decode

class RSAEncyption:
    def __init__(self,public_key,private_key=None) -> None:
        self.public_key = public_key
        self.private_key= private_key
		
    def mask(self,message: str) -> str:
        """
			Encrypts a string using RSA with public key.

			Parameters:
				message (str): The string to encrypt.

			Returns:
				str: The encrpted string.
		"""
        rsa_key = self.public_key
        cipher = PKCS1_OAEP.new(rsa_key)
        encrypted_data = cipher.encrypt(message.encode())
        return b64encode(encrypted_data).decode('utf-8')

    def demask(self,message: str) -> str:
        """
			Decrypts a string using RSA with private key.

			Parameters:
				message (str): The string to decrypt.

			Returns:
				str: The decrypted string. Returns empty string if private key is not set.
		"""
        try:
            rsa_key = self.private_key
            cipher = PKCS1_OAEP.new(rsa_key)
            encrypted_data = b64decode(message.encode('utf-8'))
            decrypted_data = cipher.decrypt(encrypted_data)
            return decrypted_data.decode('utf-8')
        except:

            return ""



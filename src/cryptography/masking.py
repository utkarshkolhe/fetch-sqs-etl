from .rsa_encryption import RSAEncyption
from .sha_hashing import SHAHashing
class Masking:
    masker = None
    masker_type=""
    @staticmethod
    def setMasker(masker_type,public_key=None,private_key=None):
        Masking.masker_type=masker_type
        if masker_type=="SHA":
            Masking.masker=SHAHashing()
        if masker_type=="RSA":
            Masking.masker=RSAEncyption(public_key,private_key)
    @staticmethod
    def mask(message):
        return Masking.masker.mask(message)
    @staticmethod
    def demask(message):
        if Masking.masker_type=="SHA":
            return ""
        return Masking.masker.demask(message)
    
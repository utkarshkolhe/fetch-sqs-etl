import hashlib
class SHAHashing:
	def mask(self,message: str) -> str:
			"""
			Hashes a string using SHA-256.

			Parameters:
				unmasked (str): The string to hash.

			Returns:
				str: The hashed string.
			"""
			return hashlib.sha256(message.encode("utf-8")).hexdigest()
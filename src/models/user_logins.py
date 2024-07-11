from cryptography.masking import Masking
from datetime import datetime
from typing import List, Dict, Any, Optional

class UserLogin:
    """
    A class for user login data, with ip and decive_id being masked
    """
    
    def __init__(self,user_id,device_type,ip,device_id,locale,app_version):
        """
        Initialization to hash sensitive fields.
        """
        self.user_id = user_id
        self.device_type=device_type
        self.locale=locale
        self.app_version=app_version

        self.create_date = datetime.now().isoformat()

        self.masked_ip =Masking.mask(ip) 
        self.masked_device_id=Masking.mask(device_id)



    def get_record(self) -> tuple:
        """
        Returns the record as a tuple.

        Returns:
            tuple: The record as a tuple.
        """
        return (
            self.user_id,
            self.device_type,
            self.masked_ip,
            self.masked_device_id,
            self.locale,
            self.app_version,
            self.create_date
        )
    @staticmethod
    def create_record(data: Dict[str, Any]) -> Optional[Any]:
        """
        Creates a UserLoginWrapper record from a dictionary of data.

        Parameters:
            data (Dict[str, Any]): The data to create a record from.

        Returns:
            Optional[UserLoginWrapper]: The created record or None if data is None.
        """
        if data is None:
            return None

        # If all the keys are not present then the data is considered incomplete and thus discarded.
        if not data.get("user_id") and not data.get("device_type") and not data.get("ip") and not data.get("device_id") \
                and not data.get("locale") and not data.get("app_version"):
            return None

        return UserLogin(
            user_id=data.get("user_id", ""),
            device_type=data.get("device_type", ""),
            ip=data.get("ip", ""),
            device_id=data.get("device_id", ""),
            locale=data.get("locale", ""),
            app_version=int(data.get("app_version", "0").replace(".", ""))
        )
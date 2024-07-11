from typing import Dict, Any, Optional, List
from models.user_logins import UserLogin
import psycopg2
from psycopg2.extras import execute_values
class PostgresConnector():
    """
    Handles database operations related to user logins.
    """

    def __init__(self,dbname,user,password,host,port):
        """
        Initializes the database connection parameters.
        """
        print("username,pass",user,password)
        self.connection = {
            "dbname": dbname,
            "user": user,
            "password": password,
            "host": host,
            "port": port,
        }

    def get_insert_query(self) -> str:
        """
        Constructs the SQL query for inserting records into the user_logins table.

        Returns:
            str: SQL query string for insertion.
        """
        return """
            INSERT INTO user_logins (
                user_id,
                device_type,
                masked_ip,
                masked_device_id,
                locale,
                app_version,
                create_date
            ) VALUES %s;
        """

    def insert(self, records: List[UserLogin]) -> None:
        """
        Inserts a list of records into the database.

        Parameters:
            records (List[UserLoginWrapper]): List of records to insert.
        """
        insert_query = self.get_insert_query()

        with psycopg2.connect(**self.connection) as conn:
            with conn.cursor() as cur:
                # Convert the UserLogin objects to tuples
                converted_records = self.get_records(records)

                # Log the records being inserted for debugging
                print(f"Inserting records: {converted_records}")

                # Execute the insert query
                execute_values(cur, insert_query, converted_records)

            # Commit the transaction to save changes
            conn.commit()
    def get_records(self, userlogins: List[UserLogin]) -> List[Any]:
        """
        Retrieves records from a list of wrapper objects.

        Parameters:
        	wrappers (List[UserLogin]): List of wrapper objects that contain records.

        Returns:
        	List[Any]: List of records retrieved from wrapper objects.
        """
        # Initialize an empty list to store records
        records = []

        # Loop through each wrapper object to get records
        for userlogin in userlogins:
            records.append(userlogin.get_record())
             
        return records

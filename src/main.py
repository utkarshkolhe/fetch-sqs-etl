import json
from typing import List, Dict, Any, Optional
from sqs.sqs_reader import SQSQueue
import time
from postgres.postgres_connector import PostgresConnector
import constants
from models.user_logins import UserLogin
from cryptography.masking import Masking
from Crypto.PublicKey import RSA




# Function to process messages read from the SQS queue and create UserLoginWrapper records
def process_messages(messages: List[Dict[str, Any]]) -> List[UserLogin]:
    """Processes a list of messages to create UserLoginWrapper objects.

    Args:
        messages (List[Dict[str, Any]]): List of messages read from SQS.

    Returns:
        List[UserLoginWrapper]: List of UserLoginWrapper objects created from the messages.
    """
    records = []  # Initialize an empty list to store UserLoginWrapper objects

    # Loop through each message to process it
    for message in messages:
        # Parse the JSON content of the message
        data = json.loads(message["Body"])
        print(f"Loaded message data: {data}")

        # Uncomment the next line if you want to mask any PII data
        # masked_data = mask_pii_data(data)

        # Create a UserLoginWrapper object from the parsed message data
        record = UserLogin.create_record(data)

        # Append the UserLoginWrapper object to the list if it's not None
        if record is not None:
            records.append(record)

    return records  # Return the list of UserLoginWrapper objects


# Main function to execute the ETL process
def main():
    """Main function to continuously read messages from SQS, process them,
    and insert the resulting UserLoginWrapper objects into a PostgreSQL database.
    """

    # Load public key from file
    with open(constants.RSA_PUBLIC_KEY_LOCATION, 'rb') as f:
        public_key = RSA.import_key(f.read())

    # Load private key from file
    with open(constants.RSA_PRIVATE_KEY_LOCATION, 'rb') as f:
        private_key = RSA.import_key(f.read())

    connector = PostgresConnector(constants.POSTGRES_DBNAME,constants.POSTGRES_USER,constants.POSTGRES_PASSWORD,constants.POSTGRES_HOST,constants.POSTGRES_PORT)
    if constants.MASK_CHOICE=="SHA":
        Masking.setMasker("SHA")    
    else:
        Masking.setMasker("RSA",public_key,private_key)
    
    while True:  # Infinite loop to keep the process running
        # Initialize SQS service and read messages from the queue
        sqs = SQSQueue(constants.SQS_QUEUE_URL,constants.SQS_ENDPOINT_URL,constants.SQS_REGION_NAME)
        messages = sqs.read_messages()
        print(f"Messages: {messages}")

        # Process the messages to create UserLoginWrapper objects
        records = process_messages(messages)
        print(f"Records: {records}")

        # Insert the UserLoginWrapper objects into the PostgreSQL database
        connector.insert(records)

        # Sleep for 5 seconds before the next iteration to avoid overwhelming the system
        time.sleep(5)


# Entry point of the script
if __name__ == "__main__":
    main()  # Run the main function
    


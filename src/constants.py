#Select Masking Technique RSA or SHA
MASK_CHOICE="RSA"

#RSA Constants
RSA_PUBLIC_KEY_LOCATION="src/cryptography/rsa_keys/public_key.pem"
RSA_PRIVATE_KEY_LOCATION="src/cryptography/rsa_keys/private_key.pem"

#SQS Constants
SQS_QUEUE_URL= "http://fetch-sqs-etl-localstack-1:4566/000000000000/login-queue"
SQS_ENDPOINT_URL = "http://fetch-sqs-etl-localstack-1:4566"
SQS_REGION_NAME="us-east-1"

#Postgres Constants
POSTGRES_DBNAME= "postgres"
POSTGRES_USER= "postgres"
POSTGRES_PASSWORD="postgres"
POSTGRES_HOST="fetch-sqs-etl-postgres-1"
POSTGRES_PORT=5432

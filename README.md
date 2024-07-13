# SQS ETL with Postgres

## Installation

### Prerequisites
- Clone of the repository
- Docker
- python (optional)

### Setting Up

1. Clone the repository.
2. (Optional) Generate new RSA keys by running `python key_generator.py`. you can save the private_key.pem for later decrypting if required.
3. (Optional) Chnage MASK_CHOICE in constants.py to "RSA" or "SHA". Based on what you want to use. Set to "RSA" by default. (Refer MAsking Section)
4. Run `docker-compose up -d`
5. Test your setup,
  - Retrieve a message from the queue: 
  `docker exec -it fetch-sqs-etl-awslocal-1 bash`
  `awslocal sqs receive-message --queue-url http://localhost:4566/000000000000/login-queue`
  - Connect to PostgreSQL to view your table: 
  `docker exec -it fetch-sqs-etl-postgres-1 bash`
  `psql -d postgres -U postgres -p 5432 -h localhost -W`
  Enter your password
  `SELECT * FROM user_logins;`

## Masking using SHA and RSA

There are two choices to mask Encryption and Hashing, you can choose between the two by editing MASK_CHOICE in constants.py
SHA is suggested in general case. RSA can be used if we need to retrive original data afterwards from the masked data.

RSA used is 1024 bit to match 256 char limit on masked columns which is not super secure. 2048 bits and higher RSA is suggested which would require the data table to have varcahr limit of 350+.


### File Structure
The file structure below only covers the main files in the project.
```
fetch-sqs-etl/
├─ src                              - Main source folder for the APP
|    ├─ cryptography                - Conatins data for masking mechanism
|      ├─ rsa_keys/                 - Folder to hold RSA public and private keys in the container
|      ├─ masking.py                - Class to handle RSA and SHA
|      ├─ rsa_encryption.py         - Class to Perform RSA Encryption
|      ├─ sha_hashing.py            - class to perform SHA
|    ├─ models                      - Conatains data model classes
|      ├─ user_logins.py            - Data Class for user login
|    ├─ postgres                    - Contains code for postgres connector
|      ├─ postgres_connector.py     - Class to interact with postgres
|    ├─ sqs                         - Contains code for SQS connector
|      ├─ sqs_reader.py             - Class to interact with SQS
├─ tests                            - Contains test cases
├─ docker-compose.yml               - Docker Compose file to build containers
├─ Dockerfile                       - Docker file to build main app
├─ key_generator.py                 - Code to generate new public and private keys for RSA
├─ private_key.pem                  - Private Key for RSA
├─ public_key.py                    - Public Key for RSA
├─ README.md                        - Readme file for git
├─ requirements.txt                 - List of dependecies for the application
```


## Future Development
- Enhance error handling and logging to manage exceptions and capture crucial debugging information.
- Implement monitoring and metrics (e.g., Prometheus + Grafana) for better visibility into application performance and resource utilization.
- Optimize performance by profiling and refining SQS message retrieval and database write operations.
- Ensure scalability by evaluating and implementing horizontal scaling strategies using container orchestration (e.g., Kubernetes).

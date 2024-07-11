from botocore.exceptions import ClientError
import boto3


class SQSQueue:
	"""
	A class to interact with an SQS (Simple Queue Service) queue.
	"""

	def __init__(self,sqs_url,endpoint_url,region_name):
		"""
		Initializes an boto3 SQS client and sets the sqs URL.
		"""
		# Save the URL of the SQS queue
		self.sqs_url = sqs_url

		# Initialize the boto3 SQS client
		self.sqs = boto3.client(
			"sqs",
			endpoint_url=endpoint_url,
			region_name=region_name
		)

	def read_messages(self, limit: int = 10) -> list:
		"""
		Reads and returns messages from the SQS queue with upper limit.

		Parameters:
			limit (int): Max number of messages to read from the queue.

		Returns:
			list: List of messages from the queue.
		"""
		# Initialize an empty list to store messages
		messages = []

		try:
			# Request messages from the SQS queue
			response = self.sqs.receive_message(
				QueueUrl=self.sqs_url,
				MaxNumberOfMessages=limit
			)

			# Check if the response contains any messages
			if "Messages" in response:
				messages = response["Messages"]

				# Delete each message from the queue after it's read
				for message in messages:
					self.delete_message(message["ReceiptHandle"])

		except ClientError as e:
			# Log any errors that occur while reading messages
			print(f"Error reading messages from SQS: {e}")

		return messages

	def delete_message(self, receipt_handle: str):
		"""
		Deletes a message from the SQS queue.

		Parameters:
			receipt_handle (str): The receipt handle of the message to be deleted.
		"""
		try:
			# Delete the message from the queue
			self.sqs.delete_message(
				QueueUrl=self.sqs_url,
				ReceiptHandle=receipt_handle
			)
		except ClientError as e:
			# Log any errors that occur while deleting the message
			print(f"Error deleting message from SQS: {e}")

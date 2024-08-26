import pika
import os
from dotenv import load_dotenv

# Configure credentials
config_path = os.path.join(os.path.dirname(__file__), 'config')
load_dotenv(os.path.join(config_path, '.env'))

USERNAME = os.getenv("RABBIT_USERNAME")
PASSWORD = os.getenv("RABBIT_PASSWORD")

credentials = pika.PlainCredentials( USERNAME, PASSWORD)

# Create a connection
connection = pika.BlockingConnection(
    pika.ConnectionParameters("localhost", credentials=credentials, heartbeat=0)
)

channel = connection.channel()

# Create a queue named "chitchat"
channel.queue_declare(queue="chitchat", durable=True)

while True:
    msg = input("Type a message: ")

    if msg == "exit":
        # Close connection
        connection.close()
        break

    # Send a message to queue
    channel.basic_publish(
        exchange="",
        routing_key="chitchat",
        body=msg,
    )
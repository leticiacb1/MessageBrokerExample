import pika
import os
import time
from dotenv import load_dotenv

# Configure credentials
config_path = os.path.join(os.path.dirname(__file__), 'config')
load_dotenv(os.path.join(config_path, '.env'))

USERNAME = os.getenv("RABBIT_USERNAME")
PASSWORD = os.getenv("RABBIT_PASSWORD")

# Define callback function (consumer function)
def callback(ch, method, properties, body):
    print(f"Received: {body}")
    time.sleep(10)
    print(f"Done: {body}")
    # Notify RabbitMQ that message was processed
    ch.basic_ack(method.delivery_tag)

# Configure credentials
credentials = pika.PlainCredentials(USERNAME, PASSWORD)

# Create a connection
connection = pika.BlockingConnection(
    pika.ConnectionParameters("localhost", credentials=credentials, heartbeat=0)
)

channel = connection.channel()

# Declare a queue named "chitchat"
channel.queue_declare(queue="chitchat", durable=True)

# Configures which function should process the messages
channel.basic_consume(
    queue="chitchat",
    auto_ack=False,
    on_message_callback=callback,
)

print("Waiting for messages. To exit press CTRL+C...")

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()

connection.close()
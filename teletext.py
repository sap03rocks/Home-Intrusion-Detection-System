import asyncio
import telegram

# Telegram Bot API Token
TOKEN = ''

# Initialize Telegram bot
bot = telegram.Bot(token=TOKEN)

# Function to send a paragraph of Lorem Ipsum text
async def send_details():
    mqtt_broker = 'broker.hivemq.com'  # Replace with the HiveMQ public broker's IP or hostname
    mqtt_port = 1883  # HiveMQ's default MQTT port is 1883
    mqtt_topic_ultrasonic = 'ultrasonic_data'
    mqtt_topic_commands = 'arduino_commands'  # Separate topic for transmitting commands to Arduino
    mqtt_broker_link=f"https://www.hivemq.com/demos/websocket-client/?host=broker.hivemq.com&port=1883",
    text = """The ultrasonic sensor detected a distance below 40cm.

MQTT Broker Link: "https://www.hivemq.com/demos/websocket-client/?host=broker.hivemq.com&port=1883"
Ultrasonic Sensor Topic: ultrasonic_data
Commands Topic: arduino_commands
"""

    await bot.send_message(chat_id='', text=text)

# Main function
def main():
    # Create an event loop
    loop = asyncio.get_event_loop()

    # Schedule the send_lorem_ipsum coroutine to run once
    loop.run_until_complete(send_details())

    # Close the event loop
    loop.close()

if __name__ == "__main__":
    main()

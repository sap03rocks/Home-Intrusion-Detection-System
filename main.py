import serial
import paho.mqtt.client as mqtt
import smtplib
import os
import cv2
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from subprocess import call

def telebotcall():
    # Make sure that teletext.py is in the same directory and is implemented correctly.
    call(["python", "teletext.py"])

def take_and_send_picture():
    # Make sure that piclele.py is in the same directory and is implemented correctly.
    call(["python", "piclele.py"])

def take_and_send_pics_to_telegram():
    call(["python", "picfortele.py"])

# Replace 'COMX' with the correct port for your Arduino (e.g., 'COM3' on Windows or '/dev/ttyUSB0' on Linux)
ser = serial.Serial('COM8', 9600)  # Change the baud rate (9600) if your Arduino uses a different rate

# MQTT Settings
mqtt_broker = 'broker.hivemq.com'  # Replace with the HiveMQ public broker's IP or hostname
mqtt_port = 1883  # HiveMQ's default MQTT port is 1883
mqtt_topic_ultrasonic = 'ultrasonic_data'
mqtt_topic_commands = 'arduino_commands'  # Separate topic for transmitting commands to Arduino

# Initialize MQTT client
mqtt_client = mqtt.Client()

# Email Settings
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'saptarshi03official@gmail.com'
receiver_email = 'ankita05saha03@gmail.com'
subject = 'Ultrasonic Sensor Alert'
body_template = """The ultrasonic sensor detected a distance below 40cm.

MQTT Broker Link: {mqtt_broker_link}
Ultrasonic Sensor Topic: {mqtt_topic_ultrasonic}
Commands Topic: {mqtt_topic_commands}
"""

# Initialize email notification flag
email_sent = False

def send_email_notification(gmail_username, gmail_password, sensor_data):
    global email_sent

    body = body_template.format(
        mqtt_broker_link=f"https://www.hivemq.com/demos/websocket-client/?host={mqtt_broker}&port={mqtt_port}",
        mqtt_topic_ultrasonic=mqtt_topic_ultrasonic,
        mqtt_topic_commands=mqtt_topic_commands
    )

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    text = MIMEText(body)
    msg.attach(text)

    # Attach the ultrasonic sensor data as a plain text to the email
    attachment = MIMEText(sensor_data)
    attachment.add_header('Content-Disposition', 'attachment', filename='sensor_data.txt')
    msg.attach(attachment)

    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(gmail_username, gmail_password)
            server.sendmail(sender_email, [receiver_email], msg.as_string())

        email_sent = True
        print("Email notification sent.")
        telebotcall()  # Call telebotcall function after sending the email
        take_and_send_picture()  # Call take_and_send_picture function after sending the email
    except Exception as e:
        print("Error sending email:", e)

def on_message(client, userdata, message):
    global email_sent

    command = message.payload.decode()
    print("Received command from MQTT:", command)

    if command == "pic" and not email_sent:
        # Use subprocess to run the capture_image.py script in a separate process
        # subprocess.run(['python', 'picturelele.py'])  # Commented out as it's not used anymore

        email_sent = True
    else:
        # Send the command to the Arduino through the serial connection
        ser.write(command.encode())

try:
    # Prompt the user to enter Gmail credentials
    gmail_username = 'saptarshi03official@gmail.com'
    gmail_password = 'alynutopfnozhbpo'

    # Connect to MQTT broker
    mqtt_client.connect(mqtt_broker, mqtt_port)
    mqtt_client.subscribe(mqtt_topic_commands)  # Subscribe to the commands topic
    mqtt_client.on_message = on_message  # Set the on_message callback function

    mqtt_client.loop_start()  # Start the MQTT loop in the background

    while True:
        try:
            line = ser.readline().decode('utf-8', errors='ignore').strip()  # Read a line of data from the Arduino and decode it
        except UnicodeDecodeError:
            continue

        data = line.split(',')
        if len(data) == 2:
            angle = int(data[0])
            distance = int(data[1])

            #print("Received from Arduino: Angle =", angle, ", Distance =", distance, "cm")

            # Send the data to the MQTT server
            mqtt_client.publish(mqtt_topic_ultrasonic, line)
            print("Data sent to MQTT server")

            # Check if the ultrasonic sensor reading is less than 40 for email notification
            if distance < 40 and not email_sent:
                # Send email notification with the sensor data
                send_email_notification(gmail_username, gmail_password, line)

except KeyboardInterrupt:
    print("Exiting...")

# Close the MQTT client and serial connection when done
mqtt_client.loop_stop()
mqtt_client.disconnect()
ser.close()

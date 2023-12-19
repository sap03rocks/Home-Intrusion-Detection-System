import cv2
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

def capture_picture():
    # Take a picture using the laptop webcam
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    camera.release()

    return frame

def send_picture_email(sender_email, sender_password, receiver_email, subject, body, image):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    # Attach the image as an attachment
    img_data = cv2.imencode('.jpg', image)[1].tobytes()
    image_attachment = MIMEImage(img_data, name='captured_image.jpg')
    msg.attach(image_attachment)

    try:
        # Connect to the SMTP server and send the email with the picture attachment
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, [receiver_email], msg.as_string())

        print("Picture sent via email.")
    except Exception as e:
        print("Error sending email:", e)

def main():
    # Enter your email credentials and recipient email address here
    sender_email = ''
    sender_password = ''
    receiver_email = ''

    subject = 'Picture from Webcam'
    body = 'Hi, I am sending you a picture from my webcam.'

    # Capture a picture from the webcam
    image = capture_picture()

    # Send the picture as an attachment in the email
    send_picture_email(sender_email, sender_password, receiver_email, subject, body, image)

if __name__ == "__main__":
    main()

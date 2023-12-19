import requests
import telegram

# Telegram Bot API Token
TOKEN = ''

# Path to the sample picture
PHOTO_PATH = 'img-min.png'

# Initialize Telegram bot
bot = telegram.Bot(token=TOKEN)

# Function to send a sample picture
def send_sample_picture(chat_id):
    photo = open(PHOTO_PATH, 'rb')
    response = requests.post(
        f'https://api.telegram.org/bot{TOKEN}/sendPhoto',
        data={'chat_id': chat_id},
        files={'photo': photo},
        timeout=60
    )
    photo.close()

    if response.status_code == 200:
        print('Photo sent successfully')
    else:
        print('Failed to send photo')

# Main function
def main():
    # Replace 'YOUR_CHAT_ID' with the actual chat ID where you want to send the picture
    chat_id = '1978499299'

    # Send the sample picture
    send_sample_picture(chat_id)

if __name__ == '__main__':
    main()

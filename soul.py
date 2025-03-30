import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from PIL import Image
import requests
from io import BytesIO

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Define a command handler function
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome to the Ghibli Style Photo Generator! Send me an image.')

def generate_ghibli_style_image(image_path):
    # Placeholder for the image generation logic
    # This should call your image generation API or model
    # Here, we just return the input image for the sake of example.
    
    return Image.open(image_path)  # This is a placeholder. Implement your style transfer logic here.

def photo_handler(update: Update, context: CallbackContext) -> None:
    # Get the photo sent by the user
    photo = update.message.photo[-1]  # Get the highest quality photo
    file = photo.get_file()
    photo_path = 'user_photo.jpg'
    file.download(photo_path)

    # Generate Ghibli style image
    styled_image = generate_ghibli_style_image(photo_path)
    
    # Save the generated image
    styled_image_path = 'styled_image.jpg'
    styled_image.save(styled_image_path)

    # Send the styled image back
    with open(styled_image_path, 'rb') as img_file:
        update.message.reply_photo(photo=img_file)

def main() -> None:
    # Insert your bot token here
    TOKEN = '7446815655:AAEopVY4VbqjCM5mcJsoxWclmXH2O-p1n3o'

    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.photo, photo_handler))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()


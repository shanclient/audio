import subprocess
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Send me a video to extract audio.')

def process_video(update: Update, context: CallbackContext) -> None:
    video_file = update.message.video.get_file()
    video_path = video_file.download()

    audio_file = "extracted_audio.mp3"
    subprocess.run(["ffmpeg", "-i", video_path, "-vn", audio_file])

    with open(audio_file, "rb") as audio:
        update.message.reply_audio(audio)

def main():
    updater = Updater("6411556913:AAEg3rtoZegdx1mGyCJo8GVhwnQZ5XgIEKA")
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.video, process_video))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

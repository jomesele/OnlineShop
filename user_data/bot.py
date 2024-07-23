import os
import django
from OnlineShop.settings import DATABASES
from user_data.models import UserData
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    user_data, created = UserData.objects.get_or_create(user_id=user_id)
    if created:
        user_data.save()
    update.message.reply_text('Welcome to the Online Shop bot!')

def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater('7213905139:AAFQVM0u8BTjCZNe_qqsIOebUHV7La2VLYM')
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
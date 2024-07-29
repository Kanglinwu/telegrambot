import logging, json
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

def configHandler():
    with open('config.json', 'r', encoding='utf-8') as file:
        config = json.load(file)
    return config['bot']['token']


async def command_1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        f'hello, {update.message.from_user.first_name}, process command_1'
    )
        
async def command_2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        f'hello, {update.message.from_user.first_name}, process command_2'
    )


def main() -> None:
    """Start the bot."""
    # Replace 'YOUR_TOKEN' with your actual bot token
    fixTokenString = configHandler()
    application = ApplicationBuilder().token(fixTokenString).build()

    # Command handler for when user execute command_1
    application.add_handler(CommandHandler("command_1", command_1))
    
    # Command handler for when user execute command_2
    application.add_handler(CommandHandler("command_2", command_2))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
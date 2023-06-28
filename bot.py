from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '5933245891:AAE568EvBW1fBVGhx-rb6kjVVTxDxKza_VE'
BOT_USERNAME: Final = '@AITbooks_bot'

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Welcome to AITbook Bot.')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('You can search material by-> \nM1\nM2\nPHYSICS\nCHEMISTRY\nBXE\nBEE\nEM\nSME\nPAPS')
                                   
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('this is a custom command')

# Responses

def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hey there!\nHow can I help you?'
   
    if 'm1' in processed:
        return 'https://drive.google.com/drive/u/0/folders/1PlgMVv2vp2AKUhU_WpV6Xv7ARUxuaJ_G'
    
    if 'm2' in processed:
        return 'https://drive.google.com/drive/u/0/folders/1tXGqaYYN8_qBFyvpzdLKm6xsBbhf6jp6'
    
    if 'chemistry' in processed:
        return 'https://drive.google.com/drive/u/0/folders/13fMvfuIN8WtlIxkRbGBu0d_le-EWZSSA'
    
    if 'physics' in processed:
        return 'https://drive.google.com/drive/u/0/folders/1inLxemE3yDvNXAtrnmjDlvhT60J91cOV'
    
    if 'bee' in processed:
        return 'https://drive.google.com/drive/u/0/folders/1WINLvLu7MUm4fDiCvMpcfA3icmQlW26-'
    
    if 'bxe' in processed:
        return 'https://drive.google.com/drive/u/0/folders/1WrAgNJLtRiaJtCf0ZUAIFeoZadhlgO2P'
    
    if 'sme' in processed:
        return 'https://drive.google.com/drive/u/0/folders/13P8JqtsL_e0xxSCyNrBZRDLGB8FzM8WD'
    
    if 'paps' in processed:
        return 'https://drive.google.com/drive/u/0/folders/1vOXQpuUSKZyAtwKc4NXLIWfqQY5iA_Vr'
    
    if 'em' in processed:
        return 'https://drive.google.com/drive/u/0/folders/1Bq9PVaNkzOpOvEpoBg356vg3IkxavtoN'
    
    return "Sorry, I don't understand! Please search for /help "

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "text"')

    # if message_type == 'group':
    #     if BOT_USERNAME in text:
    #         new_text: str = text.replace(BOT_USERNAME, '').strip()
    #         response: str = handle_response(new_text)
    #     else:
    #         return

    # else:
    response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print('Starting bot....')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))


    # Message

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)


    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=2)

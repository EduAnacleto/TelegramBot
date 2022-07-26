import telegram
import telegram.ext
from credentials import get_credentials



def start(update, context):
    update.message.reply_text("Hello!")


def help(update, context):
    update.message.reply_text("""
    The following commands are available:

    /start -> Welcome Message
    /help -> This Message
    /content -> Information about OlhoFinanceiro
    /contact -> Information about contact
    """)

def content(update, context):
    update.message.reply_text("We have ...")

def contact(update, context):
    print('info', context.bot)
    print('info', context.user_data)
    print('info', context.chat_data)
    print('info', context.bot_data)
    print('info', update)

    update.message.reply_text("Contact Edu")


def handle_message(update, context):
    update.message.reply_text(f"You said {update.message.text}")



if __name__ == '__main__':
   
    token = get_credentials('../Credentials', 'OlhoFinanceiroBot')
    updater = telegram.ext.Updater(token, use_context=True)

    disp = updater.dispatcher

    disp.add_handler(telegram.ext.CommandHandler("start", start))
    disp.add_handler(telegram.ext.CommandHandler("help", help))
    disp.add_handler(telegram.ext.CommandHandler("content", content))
    disp.add_handler(telegram.ext.CommandHandler("contact", contact))
    disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

    updater.start_polling()
    updater.idle()




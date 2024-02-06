from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import Update

updater = Updater("6712587553:AAFyNeLR1R0a5cFlBshe8_Ts8zIYQC2slvI", use_context=True)

valid_commands = ['/start', '/service', '/help', '/feedback', '/site', '/customercare']

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hello, welcome to the Saleswave Bot. Please write "
        "/help to see the available services."
    )

def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Services:
    /service - To get service
    /feedback - To feedback products
    /customercare - To get customer care information
    /site - Visit our site""")

def site(update: Update, context: CallbackContext):
    update.message.reply_text("Visit our site => https://www.youtube.com/")

def service(update: Update, context: CallbackContext):
    update.message.reply_text("Service => https://www.youtube.com/")

def feedback(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Feedback => https://www.linkedin.com/in/dwaipayan-bandyopadhyay-007a/"
    )

def customercare(update: Update, context: CallbackContext):
    update.message.reply_text("Customer Care => Call 8080-XXXX-XXXX")

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry, '%s' is not a valid command" % update.message.text)

def handle_messages(update: Update, context: CallbackContext):
    # Check if the message starts with '/'
    if update.message.text.startswith('/'):
        command = update.message.text.split()[0]  # Extract the command from the message
        if command not in valid_commands:
            update.message.reply_text("Invalid service. Please use one of the valid command.\n"
                                      "/help to see the available services.")
        else:
            context.dispatcher.process_update(update)
    else:
        update.message.reply_text(
            "Hello, welcome to the Saleswave Bot. Please write "
            "/help to see the available services."
        )

# Add a MessageHandler for handling messages
updater.dispatcher.add_handler(MessageHandler(Filters.text, callback=handle_messages))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('service', service))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('feedback', feedback))
updater.dispatcher.add_handler(CommandHandler('site', site))
updater.dispatcher.add_handler(CommandHandler('customercare', customercare))

updater.start_polling()
updater.idle()

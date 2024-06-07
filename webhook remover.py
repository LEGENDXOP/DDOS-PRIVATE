import telebot

TOKEN = '6116358973:AAHmZclg7OVPvpaBZCcHllkpD9ImGMqRV4M'
bot = telebot.TeleBot(TOKEN)

# Remove any existing webhooks
bot.remove_webhook()

# Define your message handlers and other bot logic here
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

# Start polling
bot.polling()
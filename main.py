import telebot
from telebot.apihelper import ApiTelegramException

bot = telebot.TeleBot("6262080069:AAF1Fs94pvefypcLcdgyueZx4qUNy8mvDtw")

CHAT_ID = 'pristbank' #replace your channel id

def is_subscribed(chat_id, user_id):
    try:
        response = bot.get_chat_member(chat_id, user_id)
        if response.status == 'left':
            return False
        else:
            return True

    except ApiTelegramException as e:
        if e.result_json['description'] == 'Bad Request: chat not found':
            return False



@bot.message_handler(commands=['start'])
def send_welcome(message):

    if not is_subscribed(CHAT_ID,message.chat.id):
        # user is not subscribed. send message to the user
        bot.send_message(message.chat.id, 'Please subscribe to the channel')
    else:
        bot.send_message(message.chat.id, 'You are subscribed')
        bot.send_message(message.chat.id, 'start msg', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def send_welcome(message):

    if not is_subscribed(CHAT_ID,message.chat.id):
        # user is not subscribed. send message to the user
        bot.send_message(message.chat.id, 'Please subscribe to the channel')
    else:
        bot.send_message(message.chat.id, 'help msg')

bot.polling()

from telebot import*
from telebot.types import*
from telebot.apihelper import ApiTelegramException


bot = telebot.TeleBot("6262080069:AAF1Fs94pvefypcLcdgyueZx4qUNy8mvDtw")

CHAT_ID = '@pristbank' #replace your channel id
startmsg = 'start msg'
not_sub_msg = """Please subscribe to our main channel to use this BOT."""
sub_msg = 'You are subscribed'
helpmsg = 'help msg'
adminmsg='CONTACT ADMIN HERE'

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

#BUTTONS
def sub():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("JOIN CHANNEL", url="https://t.me/pristbank"))
    return markup

def start_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("FREE TIPS", callback_data="free"),
               InlineKeyboardButton("VIP MATCHES", callback_data="vip-menu"))
    return markup

def help_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("MAIN MENU", callback_data="menu"),
               InlineKeyboardButton("CONTINUE", callback_data="vip-menu"))
    return markup

def admin_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("ADMIN", url="@pristlegacy"),
               InlineKeyboardButton("BACK", callback_data="menu"))
    return markup

def help_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("MAIN MENU", callback_data="menu"),
               InlineKeyboardButton("CONTINUE", callback_data="vip-menu"))
    return markup

def help_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("MAIN MENU", callback_data="menu"),
               InlineKeyboardButton("CONTINUE", callback_data="vip-menu"))
    return markup

def vipmenu():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("MAIN MENU", callback_data="menu"))
    return markup

#CALLBACK
@bot.callback_query_handler(func=lambda call: True)
def callback_data(call):
    if call.message:
        if call.data == "free":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text="FREE MATCHES MENU")
        elif call.data == "vip-menu":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text="VIP MATCHES MENU", reply_markup=vipmenu())
        elif call.data == "menu":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=startmsg, reply_markup=start_btn())
        elif call.data == "admin":

            bot.edit_message_text(chat_id=call.message.chat.id,

                                  message_id=call.message.message_id,

                                  text=adminmsg, reply_markup=admin_btn())
            

#COMMANDS
@bot.message_handler(commands=['start'])
def send_welcome(message):
    
    if not is_subscribed(CHAT_ID,message.chat.id):
        # user is not subscribed. send message to the user
        bot.send_message(message.chat.id, text=not_sub_msg
                         , reply_markup=sub())
    else:
        bot.send_message(message.chat.id, text=sub_msg)
        bot.send_message(message.chat.id, text=startmsg, reply_markup=start_btn())

@bot.message_handler(commands=['help'])
def send_welcome(message):
    not_sub_msg = """Please subscribe to our main channel to use this BOT."""
    sub_msg = 'You are subscribed'

    if not is_subscribed(CHAT_ID,message.chat.id):
        # user is not subscribed. send message to the user
        bot.send_message(message.chat.id, text=not_sub_msg
                         , reply_markup=sub())
    else:
        bot.send_message(message.chat.id, text=sub_msg)
        bot.send_message(message.chat.id, text=helpmsg, reply_markup=help_btn())

@bot.message_handler(commands=['admin'])
def send_welcome(message):
    
    if not is_subscribed(CHAT_ID,message.chat.id):
        # user is not subscribed. send message to the user
        bot.send_message(message.chat.id, text=not_sub_msg
                         , reply_markup=sub())
        else:



        bot.send_message(message.chat.id, text=adminmsg, reply_markup=admin_btn())
        
        
print('BOT IS STARTED SUCCESSFULLY')




bot.polling()

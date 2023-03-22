from telebot import*
from telebot.types import*
from telebot.apihelper import ApiTelegramException
from helpers import*


bot = telebot.TeleBot("5906860486:AAF9_DU9F_6Xk9tQq7rvls26HgJMzHyJJpY")

CHAT_ID = '@pristbank' #replace your channel id
admin = 'https://t.mepristlegacy'
startmsg = """
Hey {}
Thanks for using {}
I can help you in many things regarding to fixed games. Am smart but you can still contact the **UFM administration** for farther help.
**So now can I know your need ?**
Use below buttons for simplicity!
    """
not_sub_msg = """Please subscribe to our main channel to use this BOT."""
sub_msg = 'You are subscribed'
helpmsg = 'help msg'
freetips_msg = "free tips msg"
freetips = "TODAY'S FREE TIPS"
vip_msg = "VIP MSG"
vipmenu_msg = "VIP MATCHES MENU"
cs_msg = "CORRECT SCORE MSG"
country_msg = "SUBSCRIBE MSG"
admin_msg = "ADMIN MSG"
commands_msg = "ALL COMMANDS"
vipdes_msg = "VIP DESCRIPTION"
how_msg = "HOW MSG HERE"

ug_msg = "PRICE {ug} ugx"
ke_msg = "PRICE {ke} kes"
gh_msg = "PRICE {gh} cedi"
rw_msg = "PRICE {rw} rwf"
tz_msg = "PRICE {tz} tzs"
usa_msg = "PRICE {usa} $"
ng_msg = "PRICE {ng} ngn"


ug = 47000
ke = 1535
gh = 99.3
rw = 13370
tz = 30492
usa = 17.473
ng = 6500




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

def commands_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("MAIN MENU", callback_data="menu"))
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

def free_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("BACK", callback_data="menu"),
               InlineKeyboardButton("TODAYS TIPS", callback_data="today's_tips"))
    return markup

def today_tips_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("MAIN MENU", callback_data="menu"),)
    #put reply keyboard (generate booking kode)
    return markup

def freetips_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("RELOAD TIP", callback_data="reload"),
               InlineKeyboardButton("100% SURE ODDS", callback_data="vip-menu"))
    return markup
def reload_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("BACK", callback_data="menu"),
               InlineKeyboardButton("100% SURE ODDS", callback_data="vip-menu"))
    return markup
#VIP-SECTION
def vipmenu_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("TODAY'S GAMES", callback_data="vip"),
               InlineKeyboardButton("HOW IT WORKS", callback_data="how"))
    return markup

def how_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("JOIN VIP NOW", callback_data="vip-menu"),
               InlineKeyboardButton("ASK MORE", callback_data="admin"))
    return markup
#reply keyboard for admin
def admin_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("ADMIN", url='https://t.me/pristlegacy'))
    markup.add(InlineKeyboardButton("MAIN MENU", callback_data="menu"))
    return markup

def vip_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("CORRECT SCORE", callback_data="cs"),
               InlineKeyboardButton("HT/FT", callback_data="ht/ft_menu"))
    return markup

def htft_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("BACK", callback_data="vip"))
    return markup

def cs_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("BACK", callback_data="vip"),
               InlineKeyboardButton("MAIN MENU", callback_data="menu"))
    markup.add(InlineKeyboardButton("BUY MATCHES NOW", callback_data="subscribe"))
    return markup

#REPLY KEYBOARD FOR COUNTRIES
def country_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("UGANDA", callback_data="ug"),
               InlineKeyboardButton("KENYA", callback_data="ke"),
               InlineKeyboardButton("GHANA", callback_data="gh"),
               InlineKeyboardButton("RWANDA", callback_data="rw"),
               InlineKeyboardButton("TANZANIA", callback_data="tz"),
               InlineKeyboardButton("USA", callback_data="usa"),
               InlineKeyboardButton("NIGERIA", callback_data="ni"))
    markup.add(InlineKeyboardButton("BACK", callback_data="cs"), 
               InlineKeyboardButton("OTHERS", callback_data="others"))
    return markup


def ug_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("JOIN VIP", callback_data="join_vip"),
               InlineKeyboardButton("JOIN VVIP", callback_data="join_vvip"))
    markup.add(InlineKeyboardButton("NOT SURE ??", callback_data="vip_des"))
    return markup
def ke_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("JOIN VIP", callback_data="join_vip"),
               InlineKeyboardButton("JOIN VVIP", callback_data="join_vvip"))
    markup.add(InlineKeyboardButton("NOT SURE ??", callback_data="vip_des"))
    return markup
def gh_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("JOIN VIP", callback_data="join_vip"),
               InlineKeyboardButton("JOIN VVIP", callback_data="join_vvip"))
    markup.add(InlineKeyboardButton("NOT SURE ??", callback_data="vip_des"))
    return markup
def rw_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("JOIN VIP", callback_data="join_vip"),
               InlineKeyboardButton("JOIN VVIP", callback_data="join_vvip"))
    markup.add(InlineKeyboardButton("NOT SURE ??", callback_data="vip_des"))
    return markup
def tz_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("JOIN VIP", callback_data="join_vip"),
               InlineKeyboardButton("JOIN VVIP", callback_data="join_vvip"))
    markup.add(InlineKeyboardButton("NOT SURE ??", callback_data="vip_des"))
    return markup
def usa_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("JOIN VIP", callback_data="join_vip"),
               InlineKeyboardButton("JOIN VVIP", callback_data="join_vvip"))
    markup.add(InlineKeyboardButton("NOT SURE ??", callback_data="vip_des"))
    return markup
def ng_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("JOIN VIP", callback_data="join_vip"),
               InlineKeyboardButton("JOIN VVIP", callback_data="join_vvip"))
    markup.add(InlineKeyboardButton("NOT SURE ??", callback_data="vip_des"))
    return markup
def others_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("BACK", callback_data="country"),
               InlineKeyboardButton("TALK TO ADMIN", callback_data="admin"))
    markup.add(InlineKeyboardButton("NOT SURE ??", callback_data="vip_des"))
    return markup


def vipdes_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("BACK", callback_data="price"))
    return markup

#MODE OF PAYMENTS


#CALLBACK
@bot.callback_query_handler(func=lambda call: True)
def callback_data(call):
    if call.message:
        #FREE TIPS
        if call.data == "free":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text="FREE MATCHES MENU", reply_markup=free_btn())
        elif call.data == "today's_tips":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=freetips_msg, reply_markup=freetips_btn())
        elif call.data == "reload":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text= "Updated" + freetips_msg, reply_markup=reload_btn())
       #MAIN MENU     
        elif call.data == "menu":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=startmsg, reply_markup=start_btn(), 
                                   disable_web_page_preview=True)
        #VIP SECTION
        elif call.data == "vip-menu":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=vipmenu_msg, reply_markup=vipmenu_btn())
        elif call.data == "vip":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=vip_msg, reply_markup=vip_btn())
        elif call.data == "how":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=how_msg, reply_markup=how_btn())
        
        elif call.data == "cs":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=cs_msg, reply_markup=cs_btn())
        elif call.data == "subscribe":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=country_msg, reply_markup=country_btn())
        elif call.data == "country":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=country_msg, reply_markup=country_btn())
        #COUNTRY SECTION    
        elif call.data == "ug":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=ug_msg, reply_markup=ug_btn())
        elif call.data == "ke":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=ke_msg, reply_markup=ke_btn())
        elif call.data == "gh":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=gh_msg, reply_markup=gh_btn())
        elif call.data == "rw":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=rw_msg, reply_markup=rw_btn())
        elif call.data == "tz":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=tz_msg, reply_markup=tz_btn())
        elif call.data == "usa":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=usa_msg, reply_markup=usa_btn())
        elif call.data == "ng":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=ng_msg, reply_markup=ng_btn())
            
        elif call.data == "vip_des":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=vipdes_msg, reply_markup=vipdes_btn())
            

#COMMANDS
@bot.message_handler(commands=['start'])
def send_welcome(message):
    
    if not is_subscribed(CHAT_ID,message.chat.id):
        # user is not subscribed. send message to the user
        bot.send_message(message.chat.id, text=not_sub_msg
                         , reply_markup=sub())
    else:
        bot.send_message(message.chat.id, text=startmsg, reply_markup=start_btn(),
                         disable_web_page_preview=True)

@bot.message_handler(commands=['help'])
def send_welcome(message):
    if not is_subscribed(CHAT_ID,message.chat.id):
        # user is not subscribed. send message to the user
        bot.send_message(message.chat.id, text=not_sub_msg
                         , reply_markup=sub())
    else:
        bot.send_message(message.chat.id, text=helpmsg, reply_markup=help_btn())
        
@bot.message_handler(commands=['free'])
def send_welcome(message):
    if not is_subscribed(CHAT_ID,message.chat.id):
        # user is not subscribed. send message to the user
        bot.send_message(message.chat.id, text=not_sub_msg
                         , reply_markup=sub())
    else:
        bot.send_message(message.chat.id, text=freetips_msg, reply_markup=freetips_btn())
        
@bot.message_handler(commands=['contact'])
def send_welcome(message):
    if not is_subscribed(CHAT_ID,message.chat.id):
        # user is not subscribed. send message to the user
        bot.send_message(message.chat.id, text=not_sub_msg
                         , reply_markup=sub())
    else:
        bot.send_message(message.chat.id, text=admin_msg, reply_markup=admin_btn())
        

        
@bot.message_handler(commands=['commands'])
def send_welcome(message):
    if not is_subscribed(CHAT_ID,message.chat.id):
        # user is not subscribed. send message to the user
        bot.send_message(message.chat.id, text=not_sub_msg
                         , reply_markup=sub())
    else:
        bot.send_message(message.chat.id, text=commands_msg, reply_markup=commands_btn())
        
        
        

print('BOT IS STARTED SUCCESSFULLY')




bot.polling()

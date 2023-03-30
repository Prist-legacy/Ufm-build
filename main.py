from telebot import*
from telebot.types import*
from telebot.apihelper import ApiTelegramException


bot = telebot.TeleBot("5906860486:AAF9_DU9F_6Xk9tQq7rvls26HgJMzHyJJpY")

CHAT_ID = '@pristbank' #replace your channel id
admin = 'https://t.mepristlegacy'
startmsg = """
I can help you in many things regarding to fixed games. Am smart but you can still contact the **UFM administration** for farther help.
**So now can I know your need ?**
Use below buttons for simplicity!
    """
not_sub_msg = """Please subscribe to our main channel 📢 to use this BOT.
After use /reload to proceed"""

helpmsg = 'THIS A HELP MESSAGE DESCRIBING ALL WAYS AND HOW TO GET ONE RICH IN BETTING. ALL COMMANDS AND SHORT CODES ARE FOUND HERE'
commands = {  # command description used in the "help" command
    'start'       : 'Start the bot again',
    'help'        : 'Gives you information about the available services and how to use the bot',
    'free': 'To quickly access FREE TIPS.',
    'getImage'    : 'A test using multi-stage messages, custom keyboard, and media sending',
    'commands'    : 'All commands available with the bot',
    'admin'    : 'Get admin link. You can also type admin for quick access.'
}

free_msg = """‼️Caution:\n
Here at our platform, we know things are hard so we came up with the FREE TIPS department where the administrator provides you with free predictions. \nWhat does this mean, matches provided here are not 100% sure. They most times win but stake them on your own risk, losses are not on us.
\nFor 100% sure matches, join our VIP GAMES or else you may proceed to see today's free matches”9Ð5"""

freetips = """TODAY'S FREE TIPS\n

{tip}
\n

Stake accordingly 🥤"""
vip_msg = "VIP MSG"
vipmenu_msg = """VIP MATCHES ARE 100% SURE GAMES.
WINNING IS GUARANTEED. IN SHORT, THEY ARE RISK FREE MATCHES.
STAKE HIGH ON THEM."""
cs_msg = """YOU ARE ABOUT TO BUY
Match Type: Correct Score
Count: 2
ODDS: 200+

Confirm And Proceed To Booking"""
country_msg = "SPECIFY YOUR COUNTY"
admin_msg = """
🧑‍💻ADMIN CONTACT\n

You be redirected to the admin's box.\n Please try to be brief and precise\n

IE: Be on point because there are many people in that box.
"""

vipdes_msg = "VIP DESCRIPTION"
how_msg = "THIS DESCRIBES HOW TO BOOK MATCHES BOTH VIP AND VVIP"










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
    markup.add(InlineKeyboardButton("JOIN CHANNEL 📢", url="https://t.me/pristbank"))
    return markup

def commands_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("MAIN MENU 🔰", callback_data="menu"))
    return markup

def start_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("▫️FREE TIPS", callback_data="free"),
               InlineKeyboardButton("🔹VIP MATCHES ðŸ’¯", callback_data="vip-menu"))
    return markup

def help_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("MAIN MENU 🔰", callback_data="menu"),
               InlineKeyboardButton("CONTINUE ➡️", callback_data="vip-menu"))
    return markup

def free_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("BACK 🔙", callback_data="menu"),
               InlineKeyboardButton("TODAYS TIPS 🥤", callback_data="today's_tips"))
    return markup

def today_tips_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("MAIN MENU 🔰", callback_data="menu"),)
    #put reply keyboard (generate booking kode)
    return markup

def freetips_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("RELOAD TIP 🔃", callback_data="reload"),
               InlineKeyboardButton("✅ SURE ODDS", callback_data="vip-menu"))
    return markup
def reload_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("BACK 🔙", callback_data="menu"),
               InlineKeyboardButton("✅ SURE ODDS", callback_data="vip-menu"))
    return markup
#VIP-SECTION
def vipmenu_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("TODAY'S GAMES 🥤", callback_data="vip"),
               InlineKeyboardButton("HOW IT WORKS ⁉️", callback_data="how"))
    return markup

def how_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("JOIN VIP NOW 💰", callback_data="vip-menu"),
               InlineKeyboardButton("ASK MORE ⁉️", callback_data="admin"))
    return markup
#reply keyboard for admin
def admin_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("ADMIN 🧑‍💻", url='https://t.me/pristlegacy'))
    markup.add(InlineKeyboardButton("MAIN MENU 🔰", callback_data="menu"))
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
    markup.add(InlineKeyboardButton("BACK 🔙", callback_data="vip"))
    return markup

def cs_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("BUY MATCHES NOW 💰", callback_data="subscribe"))
    markup.add(InlineKeyboardButton("BACK 🔙", callback_data="vip"),
               InlineKeyboardButton("MAIN MENU 🔰", callback_data="menu"))
    
    return markup

#REPLY KEYBOARD FOR COUNTRIES
def country_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("UGANDA 🇺🇬", callback_data="ug"),
               InlineKeyboardButton("KENYA 🇰🇪", callback_data="ke"),
               InlineKeyboardButton("GHANA 🇬🇭", callback_data="gh"),
               InlineKeyboardButton("RWANDA 🇷🇼", callback_data="rw"),
               InlineKeyboardButton("TANZANIA 🇹🇿", callback_data="tz"),
               InlineKeyboardButton("USA 🇺🇲", callback_data="usa"),
               InlineKeyboardButton("NIGERIA 🇳🇬", callback_data="ng"))
    markup.add(InlineKeyboardButton("🔙", callback_data="cs"), 
               InlineKeyboardButton("OTHERS 🌐", callback_data="others"))
    return markup


def ug_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("JOIN VIP", callback_data="join_vip"),
               InlineKeyboardButton("JOIN VVIP", callback_data="join_vvip"))
    markup.add(InlineKeyboardButton("NOT SURE ⁉️", callback_data="vip_des"))
    return markup
def ke_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("JOIN VIP", callback_data="join_vip"),
               InlineKeyboardButton("JOIN VVIP", callback_data="join_vvip"))
    markup.add(InlineKeyboardButton("NOT SURE ⁉️", callback_data="vip_des"))
    return markup
def gh_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("JOIN VIP", callback_data="join_vip"),
               InlineKeyboardButton("JOIN VVIP", callback_data="join_vvip"))
    markup.add(InlineKeyboardButton("NOT SURE ⁉️", callback_data="vip_des"))
    return markup
def rw_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("JOIN VIP", callback_data="join_vip"),
               InlineKeyboardButton("JOIN VVIP", callback_data="join_vvip"))
    markup.add(InlineKeyboardButton("NOT SURE â‰ï¸", callback_data="vip_des"))
    return markup
def tz_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("JOIN VIP", callback_data="join_vip"),
               InlineKeyboardButton("JOIN VVIP", callback_data="join_vvip"))
    markup.add(InlineKeyboardButton("NOT SURE ⁉️", callback_data="vip_des"))
    return markup
def usa_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("JOIN VIP", callback_data="join_vip"),
               InlineKeyboardButton("JOIN VVIP", callback_data="join_vvip"))
    markup.add(InlineKeyboardButton("NOT SURE ⁉️", callback_data="vip_des"))
    return markup
def ng_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("JOIN VIP", callback_data="join_vip"),
               InlineKeyboardButton("JOIN VVIP", callback_data="join_vvip"))
    markup.add(InlineKeyboardButton("NOT SURE ⁉️", callback_data="vip_des"))
    return markup
def others_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("BACK ðŸ”™", callback_data="country"),
               InlineKeyboardButton("TALK TO ADMIN", callback_data="admin"))
    markup.add(InlineKeyboardButton("NOT SURE ⁉️", callback_data="vip_des"))
    return markup


def vipdes_btn():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("BACK 🔙", callback_data="country"))
    return markup

#MODE OF PAYMENTS



#CALLBACK
@bot.callback_query_handler(func=lambda call: True)
def callback_data(call):
    if call.message:
        price_tag = "PRICE IS"
        #FREE TIPS
        if call.data == "free":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=free_msg, reply_markup=free_btn())
        elif call.data == "today's_tips":
            tip = """

            TODAY'S TIP HERE

            """
            freetips = """TODAY'S FREE TIPS\n

            {tip}

            \n

            Stake accordingly 🥤"""
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=freetips, reply_markup=freetips_btn())
        elif call.data == "reload":
            freetips = """TODAY'S FREE TIPS\n

            {tip}

            \n

            Stake accordingly 🥤"""
            tip = """
            TODAY'S TIP HERE
            """
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text= "Updated \n" + freetips, reply_markup=reload_btn())
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
            ug = 47000
            ug_msg = f"VIP PRICE; {ug}ugx \n VVIP PRICE; {ug}ugx"
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=ug_msg, reply_markup=ug_btn())
        elif call.data == "ke":
            ke = 1535
            ke_msg = f"VIP PRICE; {ke}kes \n VVIP PRICE; {ke}kes"
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=ke_msg, reply_markup=ke_btn())
        elif call.data == "gh":
            gh = 99.3
            gh_msg = f"VIP PRICE; {gh}cedi \n VVIP PRICE; {gh}cedi"
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=gh_msg, reply_markup=gh_btn())
        elif call.data == "rw":
            rw = 13370
            rw_msg = f"VIP PRICE; {rw}rwf \n VVIP PRICE; {rw}rwf"
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=rw_msg, reply_markup=rw_btn())
        elif call.data == "tz":
            tz = 30492
            tz_msg = f"VIP PRICE; {tz}tzs \n VVIP PRICE; {tz}tzs"
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=tz_msg, reply_markup=tz_btn())
        elif call.data == "usa":
            usa = 17.473
            usa_msg = f"VIP PRICE; {usa}$ \n VVIP PRICE; {usa}$"
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=usa_msg, reply_markup=usa_btn())
        elif call.data == "ng":
            ng = 6500
            ng_msg = f"VIP PRICE; {ng}ngn \n VVIP PRICE; {ng}ngn"
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
        user_id = message.from_user.id
        user_name = message.from_user.first_name
   
        mention = "["+user_name+"](tg://user?id="+str(user_id)+")" 
        #mention = f"{user_name + user_name2}"
        bot.send_message(message.chat.id, text=f"**HEY {mention}**" + startmsg, reply_markup=start_btn(), parse_mode = "Markdown")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    if not is_subscribed(CHAT_ID,message.chat.id):
        # user is not subscribed. send message to the user
        bot.send_message(message.chat.id, text=not_sub_msg
                         , reply_markup=sub())
    else:
        bot.send_message(message.chat.id, text=helpmsg, reply_markup=help_btn())
        
@bot.message_handler(commands=['commands'])
def send_welcome(message):
    if not is_subscribed(CHAT_ID,message.chat.id):
        # user is not subscribed. send message to the user
        bot.send_message(message.chat.id, text=not_sub_msg
                         , reply_markup=sub())
    else:
        cmdmsg = "The following commands are available: \n"
        for key in commands:  # generate help text out of the commands dictionary defined at the top
            cmdmsg += "/" + key + ": "
            cmdmsg += commands[key] + "\n"
        bot.send_message(message.chat.id, text=cmdmsg, reply_markup=commands_btn())
        
@bot.message_handler(commands=['free'])
def send_welcome(message):
    if not is_subscribed(CHAT_ID,message.chat.id):
        # user is not subscribed. send message to the user
        bot.send_message(message.chat.id, text=not_sub_msg
                         , reply_markup=sub())
    else:
        bot.send_message(message.chat.id, text=freetips_msg, reply_markup=freetips_btn())
        
@bot.message_handler(commands=['admin'])
def send_welcome(message):
    if not is_subscribed(CHAT_ID,message.chat.id):
        # user is not subscribed. send message to the user
        bot.send_message(message.chat.id, text=not_sub_msg
                         , reply_markup=sub())
    else:
        #USAGES    
        user_id = message.from_user.id    
        user_name = message.from_user.first_name
        
        mention = "["+user_name+"](tg://user?id="+str(user_id)+")" 
            #END USAGES    
        bot.send_message(message.chat.id, text=f"USER = {mention}\n" + f"ID = {user_id}\n" + admin_msg, 
                             reply_markup=admin_btn(), 
                             parse_mode = "Markdown", 
                             disable_web_page_preview=True)
        
@bot.message_handler(func=lambda message:True)
def send_admin(message):
    if not is_subscribed(CHAT_ID,message.chat.id):
        
        
        # user is not subscribed. send message to the user
        bot.send_message(message.chat.id, text=not_sub_msg
                         , reply_markup=sub())
    else:
        if message.text.lower() == "admin":
            #USAGES
            user_id = message.from_user.id
            user_name = message.from_user.first_name
            user_name2 = message.from_user.last_name
            mention = "["+user_name + user_name2+"](tg://user?id="+str(user_id)+")" 
            #END USAGES
            bot.send_chat_action(message.chat.id, 'typing')  # show the bot "typing" (max. 5 secs)
            time.sleep(3)
            bot.send_message(message.chat.id, text=f"USER = {mention}\n" + f"ID = {user_id}\n" + admin_msg, 
                             reply_markup=admin_btn(), 
                             parse_mode = "Markdown", 
                             disable_web_page_preview=True)
    
@bot.message_handler(commands=['reload'])
def send_welcome(message):
    if not is_subscribed(CHAT_ID,message.chat.id):
        # user is not subscribed. send message to the user
        bot.send_message(message.chat.id, text=not_sub_msg
                         , reply_markup=sub())
    else:
        bot.send_message(message.chat.id, text="Bot Reloaded")
        bot.send_message(message.chat.id, text=startmsg, reply_markup=start_btn())
        
        
        

print('BOT IS STARTED SUCCESSFULLY')




bot.infinity_polling()

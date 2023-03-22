from telebot import*
from telebot.types import*
from FSUB import*

admin = ''
startmsg = 'start msg'
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




def herrr_btn():
    markup = ReplyKeyboardMarkup()
    markup.row_width = 2
    markup.add(ReplyKeyboardMarkup("UGANDA", callback_data="ug"),
               ReplyKeyboardMarkup("KENYA", callback_data="ke"),
               ReplyKeyboardMarkup("GHANA", callback_data="gh"),
               ReplyKeyboardMarkup("RWANDA", callback_data="rw"),
               ReplyKeyboardMarkup("TANZANIA", callback_data="ta"),
               ReplyKeyboardMarkup("USA", callback_data="usa"),
               ReplyKeyboardMarkup("NIGERIA", callback_data="ni"),
               ReplyKeyboardMarkup("OTHERS", callback_data="others"))
    return markup



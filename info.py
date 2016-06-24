#info bot created by negative
#info bot created by negative
#info bot created by negative
#info bot created by negative
import telebot
from telebot import types
import sys
import json
reload(sys)
sys.setdefaultencoding("utf-8")

bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=['start', 'help'])
def welcome(m):
    bot.reply_to(m, "Hello.just send me any thing and see what will you see ...")

@bot.message_handler(commands=['wtf', 'wtf'])
def welcome(m):
    bot.reply_to(m, "be to che ?")
    
@bot.message_handler(commands=['id', 'ids', 'info', 'me'])
def id(m):      # info menu
    cid = m.chat.id
    title = m.chat.title
    usr = m.chat.username
    f = m.chat.first_name
    l = m.chat.last_name
    t = m.chat.type
    d = m.date
    text = m.text
    p = m.pinned_message
    fromm = m.forward_from
#info text
    bot.send_chat_action(cid, "typing")
    bot.reply_to(m, "*ID from* : ```{}``` \n\n *Chat name* : ```{}``` \n\n\n *Your Username* : ```{}``` \n\n *Your First Name* : ```{}```\n\n *Your Last Name* : ```{}```\n\n *Type From* : ```{}``` \n\n *Msg data* : ```{}```\n\n *Your Msg* : ```{}```\n\n* pind msg * : ```{}```\n\n *from* : ```{}```".format(cid,title,usr,f,l,t,d,text,p,fromm), parse_mode="Markdown")

@bot.message_handler(commands=['contact'])
def c(m):
    uid = m.chat.id
    bot.send_chat_action(uid, 'typing')
    bot.send_contact(uid, phone_number="+989398391927", first_name="parsa")


@bot.message_handler(commands=['about']) # copy right Taylor Team
def p(m):
    uid = m.chat.id
    bot.send_chat_action(uid, 'typing')
    bot.send_message(uid, "base by amir negative(taylor team)", parse_mode="Markdown")
    bot.send_photo(uid, open('taylor.jpg'), caption="@Taylor_Team")

@bot.message_handler(func=lambda m: m.chat.type == 'private', commands=['idme'])
def test_handler(m):
    cid = m.chat.id
    fl = m.chat.first_name
    bot.send_message(cid, "*{}*  Your ID = ```{}```".format(fl,cid), parse_mode="Markdown")
    

@bot.message_handler(func=lambda message: True)  # on pv all pm / group /id /me pm created by negative
def id(m):      # info menu
    cid = m.chat.id #id from
    title = m.chat.title #group title
    usr = m.chat.username #username
    f = m.chat.first_name #First name
    l = m.chat.last_name #last name
    t = m.chat.type #type
    d = m.date #data
    text = m.text #msg text
    p = m.pinned_message #msg pined
    fromm = m.forward_from #from 
#info text  by negative , taylor team copy right
    bot.send_chat_action(cid, "typing")
    bot.reply_to(m, "*ID from* : ```{}``` \n\n *Chat name* : ```{}``` \n\n\n *Your Username* : ```{}``` \n\n *Your First Name* : ```{}```\n\n *Your Last Name* : ```{}```\n\n *Type From* : ```{}``` \n\n *Msg data* : ```{}```\n\n *Your Msg* : ```{}```\n\n* pind msg * : ```{}```\n\n *from* : ```{}```".format(cid,title,usr,f,l,t,d,text,p,fromm), parse_mode="Markdown")
    


bot.polling()
#end

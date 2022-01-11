from pyrogram import *
from typing import Text
from pyrogram import *
from deep_translator import MyMemoryTranslator
from pyrogram.filters import Filter, chat
from pyrogram.methods.messages import send_message
from pyrogram.types import ChatPermissions
from time import time
import requests
from pyrogram.types.messages_and_media import message

app = Client("translate",
    api_id=5527711,
    api_hash='bfe9610f27c9298bbae60d066d11c5e7',
    bot_token='1670124420:AAF9g-ka_nDqbFFXNPkMNUW-sx8-KiQrjLA',
    )

# start
@app.on_message(filters.command(['start'|'start@two1two_bot']))
async def start(clinet,message):
    await message.reply("""
    سلام برای اطلاع از دستورات از 
    /helps
    استفاده کنید
    """)
# help
@app.on_message(filters.command('helps'|'helps@two1two_bot'))
async def helps(client,message):
    await message.reply("""
    /start
    /helps
    /tr [text]   => en to fa
    /trf [text]  => fa to en
    /day
    (admin)
    /kick
    /bon
    /unbon
    /pin
    /unpin
    """)
# download profile instagram
@app.on_message(filters.command('day'|'day@two1two_bot'))
async def day(client,message):
    response = requests.get("https://api.shelper.ir/monasebat.php")
    gets = response.json()[0]['occasion']
    await message.reply(gets)

# kick
@app.on_message(filters.command('kick'|'kick@two1two_bot')|filters.user('742297528'))
async def kick(client,message):
    chat_id = message.chat.id
    user_id = message.reply_to_message.from_user.id
    await client.kick_chat_member(chat_id,user_id)
    await message.reply('ریمو شد')
#pin
@app.on_message(filters.command('pin'|'pin@two1two_bot'))
async def pins(client,message):
    chat_id = message.chat.id
    message_id = message.reply_to_message.message_id
    await client.pin_chat_message(chat_id, message_id)
    await message.reply('پین شد')
#pin
@app.on_message(filters.command('bon'|'bon@two1two_bot')|filters.user('742297528'))
async def bon(client,message):
    chat_id = message.chat.id
    user_id = message.reply_to_message.from_user.id
    await client.restrict_chat_member(chat_id, user_id, ChatPermissions(), int(time() + 60))
    await message.reply('بن شد')
#unbon
@app.on_message(filters.command('unbon'|'unbon@two1two_bot')|filters.user('742297528'))
async def bon(client,message):
    chat_id = message.chat.id
    user_id = message.reply_to_message.from_user.id
    await client.unban_chat_member(chat_id, user_id)
    await message.reply('از بن خارج شد')
# unpin
@app.on_message(filters.command('unpin'|'unpin@two1two_bot')|filters.user('742297528'))
async def unpins(client,message):
    chat_id = message.chat.id
    await client.unpin_all_chat_messages(chat_id)


# welcome
@app.on_message(filters.new_chat_members)
async def new_chat(client, message):
    chatt = ''
    for i in message.new_chat_members:
        chatt += f"{i.first_name}"
    await message.reply(f'سلام {chatt} خوش آمدی به گروه ما')

# left
@app.on_message(filters.left_chat_member)
async def left_chat(client, message):
    await message.reply(f'به کیرم {message.left_chat_member.first_name}')

# tran to en to fa 
@app.on_message(filters.text, group = 2)
async def tr(client, message):
    text = message.text
    if text.startswith('/tr '):
        text = text.replace('/tr ', '')
        tr = MyMemoryTranslator(source= 'en', target= 'fa')
        tr = tr.translate(text)
        await message.reply(tr)

@app.on_message(filters.text, group=1)
async def trf(client, message):
    text = message.text
    if text.startswith('/trf '):
        text = text.replace('/trf ', '')
        trf = MyMemoryTranslator(source= 'fa', target= 'en')
        trf = trf.translate(text)
        await message.reply(trf)

@app.on_message(filters.text, group=8)
async def trr(client, message):
    
    text = (message.text).lower()
    
    if (text.startswith('trr') or text.startswith('trf') or text.startswith('tr') or text.startswith('/trr') or text.startswith('/trf') or text.startswith('/tr') or text.startswith('/tr@samyarborderbot') or text.startswith("'/trr@samyarborderbot'") or text.startswith("'/trf@samyarborderbot'") ) and message.reply_to_message:
       trf = MyMemoryTranslator(source= 'en', target= 'fa')
       trf = trf.translate(message.reply_to_message.text)
       await message.reply(trf) 
       tr= MyMemoryTranslator(source= 'fa', target= 'en')
       tr = tr.translate(message.reply_to_message.text)
       await message.reply(tr)

app.run()
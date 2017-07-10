#!/usr/bin/env python3

import logging
import re
from urllib.parse import urlparse
from urllib.request import urlopen
from datetime import datetime

from telegram import ParseMode, Message, Chat, MessageEntity
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram.ext.dispatcher import run_async

from start_bot import start_bot
from utils import send_async, error, TIMEOUT
from extract import extract_info
from shared_vars import updater, dispatcher

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)

def link_handler_routine(bot, update):
	"""Handler for links"""
	chat_id = update.message.chat_id
	print("Incoming: " + update.message.text)
	# Start by looking for netease sharing addr
	NMsong = re.findall(r'(http://music.163.com/song/\d+)', update.message.text)[0]
	print("Parsed: " + NMsong)
	bot.send_chat_action(chat_id=chat_id, action=u"解析中")
	try:
		response = urlopen(NMsong);
	except urllib.error.URLError as e:
		error(e.reason)
	NMhtml = bytes(response.read()).decode("utf-8")
	# Downloaded from server, start extracting
	NMtitle = extract_info(NMhtml, "title")
	NMsubtitle = extract_info(NMhtml, "subtitle")
	NMalbum = extract_info(NMhtml, "album")
	NMartist = extract_info(NMhtml, "artist")
	query=NMtitle + "\n" + NMsubtitle + "\n" + NMalbum + "\n" + NMartist
	send_async(bot, chat_id, text = query)
	
dispatcher.add_handler(MessageHandler((Filters.text & Filters.entity(MessageEntity.URL)), link_handler_routine))

start_bot(updater)
updater.idle()

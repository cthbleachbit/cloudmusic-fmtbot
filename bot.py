#!/usr/bin/env python3

import logging
import re
from urllib.parse import urlparse
from datetime import datetime

from telegram import ParseMode, Message, Chat, MessageEntity
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram.ext.dispatcher import run_async

from NetEaseMusicApi import api as NMapi

from start_bot import start_bot
from utils import send_async, error, TIMEOUT
from shared_vars import updater, dispatcher

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)

def link_handler_routine(bot, update):
	"""Handler for links"""
	chat_id = update.message.chat_id
	print("Incoming: " + update.message.text)
	# Start prasing.
	NMurl = re.findall(r'(http://music.163.com\S+)', update.message.text)[0]
	print("Parsed: " + NMurl)
	send_async(bot, chat_id, text = NMurl)
	
dispatcher.add_handler(MessageHandler((Filters.text & Filters.entity(MessageEntity.URL)), link_handler_routine))

start_bot(updater)
updater.idle()

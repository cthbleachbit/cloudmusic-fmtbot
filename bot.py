#!/usr/bin/env python3

import logging
from datetime import datetime

from telegram import ParseMode, Message, Chat, MessageEntity
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram.ext.dispatcher import run_async

from start_bot import start_bot
from utils import send_async, error, TIMEOUT
from shared_vars import updater, dispatcher

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)

def link_handler_routine(bot, update):
	"""Handler for links"""
	logger.info("Incoming: " + update.message.text)
	
dispatcher.add_handler(MessageHandler((Filters.text & Filters.entity(MessageEntity.URL)), link_handler_routine))

start_bot(updater)
updater.idle()

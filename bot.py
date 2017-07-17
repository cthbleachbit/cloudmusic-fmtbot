#!/usr/bin/env python3

import logging
import re
from urllib.parse import urlparse
from urllib.request import urlopen
from datetime import datetime
from io import BytesIO

from telegram import ParseMode, Message, Chat, ChatAction, MessageEntity
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram.ext.dispatcher import run_async

from start_bot import start_bot
from utils import send_async, send_photo_async, error, TIMEOUT
from extract import *
from shared_vars import *
import info_commands

logging.basicConfig(
		format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
		level=logging.INFO)
logger = logging.getLogger(__name__)

def link_handler_routine(bot, update):
	"""Handler for links"""
	chat_id = update.message.chat_id
	logger.debug("Incoming: " + update.message.text)
	
	# Start by looking for netease sharing sond id
	try:
		NMsong = extract_songid(update.message.text)
	except Exception as e:
		if chat_id > 0:
			send_async(bot, chat_id, text = u"这啥？")
		elif chat_id == special_group:
			send_async(bot, chat_id, text = easter_egg_msg)
		logger.info("Possibly not an valid link:")
		logger.info(update.message.text)
		return
	logger.info("Parsed: " + NMsong)
	
	# Start parsing
	bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
	try:
		response = urlopen("http://music.163.com/song/" + NMsong);
		NMhtml = bytes(response.read()).decode("utf-8")
	except Exception as e:
		send_async(bot, chat_id, text = u"无法连接到网易云")
		error(bot, update, "Connection failed")
		return
	
	# Downloaded from server, start extracting....
	# Text info
	try:
		NMtitle = extract_info(NMhtml, "title")
		NMsubtitle = extract_info(NMhtml, "subtitle")
		NMalbum = extract_info(NMhtml, "album")
		NMartist = extract_info(NMhtml, "artist")
		NMdetails = NMtitle + "\n" + NMsubtitle + "\n" + NMalbum + "\n" + NMartist + "\n\nhttp://music.163.com/song/" + NMsong
		logger.info("Done: " + NMsong)
	except Exception as e:
		error(bot, update, "Extraction failure?")
		send_async(bot, chat_id, u"抓取失败")
		return
	
	# To locate the url for album art
	try:
		NMalbumarturl = extract_albumarturl(NMhtml)
	except Exception as e:
		# If somehow there's no cover art, send a pure text message instead.
		error(bot, update, "Cannot download cover art")
		send_async(bot, chat_id, text = NMdetails)
		return
	logger.info("Downloading album art : " + NMalbumarturl)
	# Actually download the album art
	try:
		response = urlopen(NMalbumarturl)
		imgbuffer = BytesIO(response.read())
	except Exception as e:
		send_async(bot, chat_id, text = u"无法连接到网易云")
		error(bot, update, "Connection failed")
		return
	imgbuffer.name = "cover.png"
	imgbuffer.seek(0)
	send_photo_async(bot, chat_id, photo = imgbuffer, caption = NMdetails)
	logger.info("Sent full details with image: " + NMsong)

dispatcher.add_handler(MessageHandler((Filters.text & Filters.entity(MessageEntity.URL)), link_handler_routine))
info_commands.register()

start_bot(updater)
logger.info("Bot started.")
updater.idle()

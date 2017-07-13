# Thanks https://github.com/jh0ker from unobot for this file and great ideas!
# I changed indentation from 4 spaces to one tab and reformatted some comments:)

#!/usr/bin/env python3

import logging

from telegram import Emoji
from telegram.ext.dispatcher import run_async

logger = logging.getLogger(__name__)

# Considering krap network in China....
TIMEOUT = 5

# Get the current players name including their username, if possible 
def display_name(user):
	user_name = user.first_name
	if user.username:
		user_name += ' (@' + user.username + ')'
	return user_name

# Simple error handler
def error(bot, update, error):
	logger.exception(error)

# Send text message asynchronously
# Params:
# text = str
@run_async
def send_async(bot, *args, **kwargs):
	if 'timeout' not in kwargs:
		kwargs['timeout'] = TIMEOUT

	try:
		bot.sendMessage(*args, **kwargs)
	except Exception as e:
		error(None, None, e)

# Send photo message asynchronously
# Params:
# photo = photo blob or object
# caption = text caption for this photo
@run_async
def send_photo_async(bot, *args, **kwargs):
	if 'timeout' not in kwargs:
		kwargs['timeout'] = TIMEOUT

	try:
		bot.sendPhoto(*args, **kwargs)
	except Exception as e:
		error(None, None, e)

# Somehow unnecessary here since sharing from app cannot be processed as an
# inline query without user intervention.
# Reply to an inline query asynchronously
@run_async
def answer_async(bot, *args, **kwargs):
	if 'timeout' not in kwargs:
		kwargs['timeout'] = TIMEOUT

	try:
		bot.answerInlineQuery(*args, **kwargs)
	except Exception as e:
		error(None, None, e)

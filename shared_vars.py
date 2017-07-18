#!/usr/bin/env python3

from telegram.ext import Updater
from telegram.contrib.botan import Botan
from auth import TOKEN

updater = Updater(token=TOKEN, workers=16)
dispatcher = updater.dispatcher

# When a invalid link appears in the special group, the bot will reply with the
# easter egg message.
#
# When a valid link from the special group has been parsed and prepared, the bot
# sends the share to the special channel in addition to a regular reply to the
# link.
#
# the special group chat id and channel chat id
# set to 0 to disable these extra functions
special_group = 0
special_channel = 0
easter_egg_msg = u""

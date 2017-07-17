#!/usr/bin/env python3

from telegram.ext import Updater
from telegram.contrib.botan import Botan
from auth import TOKEN

updater = Updater(token=TOKEN, workers=16)
dispatcher = updater.dispatcher
# the special group chat id and channel chat id
# set to 0 to disable
# the bot will activate special functions for this group:
#	activates easter egg
#	repost share from the group to the channel automatically
special_group = 0
special_channel = 0
easter_egg_msg = u""

#!/usr/bin/env python3

from telegram.ext import Updater
from telegram.contrib.botan import Botan
from auth import TOKEN

updater = Updater(token=TOKEN, workers=16)
dispatcher = updater.dispatcher

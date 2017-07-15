from telegram import ParseMode
from telegram.ext import CommandHandler

from utils import send_async
from shared_vars import dispatcher

help_text = ("按照以下步骤\n\n"
		"1. 从网易云音乐客户端分享或者复制浏览器的网页地址\n"
		"2. 发送给这个 bot\n"
		"3. 得到有专辑封面的分享消息")

# Handling /help and /start
def help(bot, update):
	send_async(bot, update.message.chat_id, text=help_text,
			parse_mode=ParseMode.HTML, disable_web_page_preview=True)

# Returns chat id
def getcid(bot, update):
	send_async(bot, update.message.chat_id, text=update.message.chat_id,
			parse_mode=ParseMode.HTML, disable_web_page_preview=True)

def register():
	dispatcher.add_handler(CommandHandler('help', help))
	dispatcher.add_handler(CommandHandler('start', help))

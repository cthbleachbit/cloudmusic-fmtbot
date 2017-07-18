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
			disable_web_page_preview=True)

# Returns chat id
def getcid(bot, update):
	send_async(bot, update.message.chat_id, text=update.message.chat_id,
			disable_web_page_preview=True)

# Returns user id
def getuid(bot, update):
	send_async(bot, update.message.chat_id, text=update.message.from_user.id,
			disable_web_page_preview=True)

def version(bot, update):
	p = subprocess.Popen("""bash -c 'printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"' """, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	lines = ""
	for line in p.stdout.readlines():
		lines = lines + line.decode('utf-8')
	retval = p.wait()
	send_async(bot, update.message.chat_id, text=lines,
			disable_web_page_preview=True)

def register():
	dispatcher.add_handler(CommandHandler('help', help))
	dispatcher.add_handler(CommandHandler('start', help))
	dispatcher.add_handler(CommandHandler('getcid', getcid))
	dispatcher.add_handler(CommandHandler('getuid', getuid))
	dispatcher.add_handler(CommandHandler('version', version))

# cloudmusic-fmtbot
Netease Cloudmusic Telegram sharing formatting bot

# What is it?
Netease Cloudmusic sharing generates __extra amount__ of junk text when sharing songs. This bot generates a photo message with album art and song info. It is also capable of sharing songs from a group to a channel, see `shared_vars.py` for details.

Thanks [jh0ker](https://github.com/jh0ker) 's unobot implementation for a nice structural design!

# To run
Store your Bot API token in `auth.py`, install the whole bunch of dependencies for python 3 and run `bot.py`

# Commands available

* `help`, `start` triggers a help message
* `version` sends current git revision
* `getuid`, `getcid` retrives numerical user id and chat id

# Deps
* python-telegram-bot
* urllib

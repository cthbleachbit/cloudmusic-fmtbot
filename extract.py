#!/usr/bin/env python3

import logging
import re

def extract_songid(url):
	NMsongid = re.findall(r'https?://music.163.com/song/(\d+)', url) + re.findall(r'https?://music.163.com/#/song\?id=(\d+)', url)
	return NMsongid[0]

def extract_albumid(url):
	NMalbumid = re.findall(r'https?://music.163.com/album/(\d+)', url) + re.findall(r'https?://music.163.com/#/album\?id=(\d+)', url)
	return NMalbumid[0]

def extract_info(html, infotype):
	if infotype == "title":
		return re.findall(r'<em class="f-ff2">(.+)</em>', html)[0]
	if infotype == "subtitle":
		result=re.findall(r'<div class="subtit f-fs1 f-ff2">(.+)</div>', html);
		if len(result) == 0:
			return u"--"
		else:
			return result[0]
	elif infotype == "album":
		return re.findall(u'<p class="des s-fc4">所属专辑：<a href="/album\?id=\d+" class="s-fc7">(.+)</a>.*</p>', html)[0]
	elif infotype == "artist":
		return re.findall(u'<p class="des s-fc4">歌手：<span title="(.+)"><a class="s-fc7" href="/artist\?id=\d+">.+</a></span></p>', html)[0]

def extract_albumarturl(html):
	return re.findall(r'<img src=".+" class="j-img" data-src="(\S+)">', html)[0]

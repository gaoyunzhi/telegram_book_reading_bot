#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from telegram.ext import Updater
import yaml
import glob
import time
import random

with open('CREDENTIALS') as f:
	CREDENTIALS = yaml.load(f, Loader=yaml.FullLoader)
tele = Updater(CREDENTIALS['bot_token'], use_context=True)
chat_id = -1001435357912
channel = tele.bot.get_chat(chat_id)

books = []
for filename in glob.glob("books/*.txt"):
	with open(filename) as f:
		books.append((filename, f.read()))

def retry(f):
	try:
		f()
	except Exception as e:
		print(e)
		time.sleep(random.random() * 100)
		retry(f)

def getBookName(filename):
	return filename[6:-4]

def getNewInfo(filename, message_id):
	book_name = getBookName(filename)
	link = 't.me/%s/%d' % (channel.username, message_id)
	return '[%s](%s)' % (book_name, link)

def getInfo(desc):
	r = []
	for k, v in desc.items():
		r.append(getNewInfo(k, v))
	r.sort()
	return '\n'.join(r)

def sending():
	desc = {}
	for filename, book in books:
		message_id = channel.send_message(filename).message_id
		desc[filename] = message_id
		for sentence in book.split('\n')[:10]:
			if not sentence:
				continue
			time.sleep(random.random() * 6)
			retry(lambda: channel.send_message(sentence))
		pin_id = channel.send_message(
			'电梯:\n' + getInfo(desc), parse_mode='Markdown', disable_web_page_preview=True).message_id
		tele.bot.pin_chat_message(chat_id, pin_id)

sending()
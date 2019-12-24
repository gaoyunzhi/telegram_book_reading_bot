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
channel = tele.bot.get_chat(-1001435357912)

books = []
for filename in glob.glob("books/*.txt"):
	with open(filename) as f:
		books.append((filename, f.read()))

for filename, book in books:
	channel.send_message(filename)
	for sentence in book.split('\n\n'):
		channel.send_message(sentence)
		time.sleep(random.random() / 10)
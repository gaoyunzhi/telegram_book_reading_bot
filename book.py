#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from telegram.ext import Updater
import yaml

with open('CREDENTIALS') as f:
	CREDENTIALS = yaml.load(f, Loader=yaml.FullLoader)
tele = Updater(CREDENTIALS['bot_token'], use_context=True)
channel = tele.bot.get_chat(-1001435357912)


from chatterbot import ChatBot 
from chatterbot.trainers import ListTrainer
import os, sys
bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)

for files in os.listdir('/mnt/e/Programming/chatterbot-corpus-master/chatterbot_corpus/data/english/'):
	data = open('/mnt/e/Programming/chatterbot-corpus-master/chatterbot_corpus/data/english/' + files, 'r').readlines()
	bot.train(data)

while True:
	message = input('You: ')
	if message.strip() == 'Bye':
		print('ChatBot: Bye')
		break
	else:
		reply = bot.get_response(message)
		print('ChatBot: ', reply)
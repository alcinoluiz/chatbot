#!/usr/bin/python
import time
import os
from random import randint
from gtts import gTTS

class ChatBot(object):
	def talk(self, txt):
		tts = gTTS(text=txt, lang=self.lang)
		tts.save("txt.mp3")
		os.system('mpg123 txt.mp3 &> /dev/null')

	def macthKeys(self, user_input):
		self.kb_keys = []
		for key in self.kb.keys():
			self.kb_keys.append([key,0])
		bigger = []
		for key in self.kb_keys:
			s1 = user_input.split(" ")
			s2 = key[0].split(" ")
			final_index = len(s1) if len(s1) < len(s2) else len(s2)
			for i in range(final_index):
				if s1[i] == s2[i]:
					key[1] += 1
			if len(bigger) < 1 and key[1] > 0:
				bigger = key
			if len(bigger) > 0:
				if bigger[1] < key[1]:
					bigger = key		
		if len(bigger) > 0:
			return self.createResponse(bigger[0], user_input)
		else:
			return self.getKey('*')

	def createResponse(self,key, user_input):
		
		response = self.getKey(key)
		
		if("*" in key):
			key = key.replace('*', '')
			
			for txt in key.split(' '):
				user_input = user_input.replace(txt, '')
			star = user_input.strip()
			
			response = response.replace('*', star)
			return response
		return response

	def readKb(self):
		fo = open("kb.txt", "a+")
		lineList = []
		for line in fo:
			lineList.append(line)
		return lineList

	def writeKb(self):
		keysList = list(self.kb.keys())
		for key in keysList:
			print key + "-" + str(self.kb[key])
	
	def getKey(self, key):
		rn = randint(0,len(self.kb[key])-1)
		return self.kb[key][rn]
	
	def learnMode(self):
		question = raw_input("pergunta: ")
		answer = raw_input("resposta: ")
		if question in self.kb.keys():
			l = list(self.kb[question])
			l.append(answer)
			self.kb[question] = tuple(l)
		else:
			l = list()
			l.append(answer)
			self.kb[question] = tuple(l)

	def chat(self):
		user_input = ""
		run =  True
		if self.lang == 'en':
			hi = "Hi, I'm " + self.name
			self.talk(hi)
			print hi
		elif self.lang == 'pt-br':
			oi = "Ola, eu sou "+ self.name
			self.talk(oi)
			print oi
		while run:
			user_input = raw_input("> ")
			if user_input == "tchau" or user_input == "sair":
				run = False
				print "Ate a proxima"
			elif user_input == "/learn":
				self.writeKb()
				# learnMode()
			else:
				resp = self.macthKeys(user_input)
				self.talk(resp)
				print resp
			
	def startKb(self,chatList):
		for chat in chatList:
			chat = chat.replace("\n", "")
			values = chat.split("|")
			if "=" in values[1]:
				values[1] = values[1].replace("=","")
				self.kb[values[0]] = self.kb[values[1]]
			else:
				self.kb[values[0]] = tuple(values[1:])
	
	def __init__(self, name, lang='en', kbFile='kb.txt'):
		self.name = name
		self.kb = {}
		self.kb_keys = []
		self.lang = lang
		self.kbFile = kbFile
		lines = self.readKb()
		self.startKb(lines)

samantha = ChatBot("Samantha",'en')
samantha.chat()
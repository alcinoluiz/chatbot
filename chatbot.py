#!/usr/bin/python
import time
from random import randint

class ChatBot(object):
	def macthKeys(self, user_input):
		self.kb_keys = []
		for key in self.kb.keys():
			self.kb_keys.append([key,0])
		bigger = []
		for key in self.kb_keys:
			if len(user_input.split(" ")) > 1:
				input_split = user_input.split(" ")
				for string in input_split:
					if string in key[0]:
						key[1] += 1
			else:
				if user_input in key[0]:
					key[1] += 1
			if len(bigger) < 1 and key[1] > 0:
				bigger = key
			if len(bigger) > 0:
				if bigger[1] < key[1]:
					bigger = key		
		if len(bigger) > 0:
			return self.createResponse(bigger[0], user_input)
		else:
			return self.getKey("*")

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
		fo = open("kb.txt", "r")
		lineList = []
		for line in fo:
			lineList.append(line)
		return lineList
		fo.close()

	def writeKb(self):
		keysList = list(self.kb.keys())
		lines = []
		fo = open('kb.txt', 'w')
		for key in keysList:
			line = key
			for value in self.kb[key]:
				line += "|" + value
			fo.write(line+"\n")
			lines.append(line)
		# print lines
		fo.close()
		
	
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
		print "Ola, eu sou ", self.name
		while run:
			user_input = raw_input("> ")
			if user_input == "tchau" or user_input == "sair":
				run = False
				self.writeKb()
				print "Ate a proxima"
			elif user_input == "/learn":
				self.learnMode()				
			else:
				resp = self.macthKeys(user_input)
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
	
	def __init__(self, name):
		self.name = name
		self.kb = {}
		self.kb_keys = []
		lines = self.readKb()
		self.startKb(lines)

peter = ChatBot("Peter")
peter.chat()
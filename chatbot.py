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
			s1 = user_input.split(" ")
			s2 = key[0].split(" ")
			# if len(s1) == len(s2):
			# print "same len"
			final_index = len(s1) if len(s1) < len(s2) else len(s2)
			for i in range(final_index):
				if s1[i] == s2[i]:
					key[1] += 1
			if len(bigger) < 1 and key[1] > 0:
				bigger = key
			if len(bigger) > 0:
				if bigger[1] < key[1]:
					bigger = key
		# print self.kb_keys
		if len(bigger) > 0:
			return self.createResponse(bigger[0])
		else:
			return "Nao ha resposta para isso."

	def createResponse(self,key):
		response = self.getKey(key)

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
		print self.kb[key][rn]
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
				print "Ate a proxima"
			elif user_input == "/learn":
				self.writeKb()
				# learnMode()
			elif user_input == "aaaa":
				print "aaa"
			else:
				# self.match(user_input)
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
		# print lines
		self.startKb(lines)

peter = ChatBot("Peter")
peter.chat()
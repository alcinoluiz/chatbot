# chatbot

Simple python chatbot example.

# How to use
Create a 'kb.txt' file to creae a knowledge base.<br>
The knowledge base line is like that:<br>
	hi|hello|hi|i'm here<br>
The first term is the key and the another ones is the answer (that will be choosen randomly).<br><br>

#Use the same answer
To use the same answer for different key just put <new key>|=<reference key><br>
	hi|hello|hi|i'm here<br>
	hello|=hi<br>
Now, 'hi' and 'hello' has te same answer.<br><br>

#Star Match
Star match is bascically<br>
	you of *?|What is the connection between me and *?|What else does * remind you of?<br>

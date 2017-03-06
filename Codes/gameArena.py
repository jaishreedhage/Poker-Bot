from HandEvaluator import *
from pokerUI import *
import variables
import random
import sys
import time



#global variables

deck = cards
game = 0

#shuffle cards
def shuffle () :
	random.shuffle(deck)


print variables.STOP,"***"

while (variables.STOP is 0) :

	shuffle()
	popped_cards = []
	print "In while loop :) ", game , variables.STOP
	
	ui.GameNumber(app,str(game))

	pop = deck.pop()
	popped_cards.append(pop)
	ui.p1c1(app,image_dir+pop+png)

	pop = deck.pop()
	popped_cards.append(pop)
	ui.p1c2(app,image_dir+pop+png)

	pop = deck.pop()
	popped_cards.append(pop)
	ui.p2c1(app,image_dir+pop+png)

	pop = deck.pop()
	popped_cards.append(pop)
	ui.p2c2(app,image_dir+pop+png)

	pop = deck.pop()
	popped_cards.append(pop)
	ui.bc1(app,image_dir+pop+png)

	pop = deck.pop()
	popped_cards.append(pop)
	ui.bc2(app,image_dir+pop+png)

	pop = deck.pop()
	popped_cards.append(pop)
	ui.cc1(app,image_dir+pop+png)

	pop = deck.pop()
	popped_cards.append(pop)
	ui.cc2(app,image_dir+pop+png)

	pop = deck.pop()
	popped_cards.append(pop)
	ui.cc3(app,image_dir+pop+png)

	pop = deck.pop()
	popped_cards.append(pop)
	ui.cc4(app,image_dir+pop+png)

	pop = deck.pop()
	popped_cards.append(pop)
	ui.cc5(app,image_dir+pop+png)

	app.processEvents()

	time.sleep(2)
	# print "Hello", STOP
	# app.processEvents()

if variables.STOP is 1 :
	sys.exit(app.exec_())



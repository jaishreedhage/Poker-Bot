from HandEvaluator import *
from pokerUI import *

import random
import sys
import time



#global variables

deck = cards
game = 0

#shuffle cards
def shuffle () :
	random.shuffle(deck)


print STOP,"***"

while (STOP is 0) :

	shuffle()
	popped_cards = []
	print "In while loop :) ", game
	
	ui.GameNumber(app,str(game))
	app.processEvents()
	pop = deck.pop()
	popped_cards.append(pop)
	game = game+1
	# ui.p1c1(MainWindow,image_dir+pop+png)
	# pop = deck.pop()
	# popped_cards.append(pop)
	# ui.p1c2(MainWindow,image_dir+pop+png)
	# pop = deck.pop()
	# popped_cards.append(pop)
	# ui.p2c1(MainWindow,image_dir+pop+png)
	# pop = deck.pop()
	# popped_cards.append(pop)
	# ui.p2c2(MainWindow,image_dir+pop+png)
	# pop = deck.pop()
	# popped_cards.append(pop)
	# ui.bc1(MainWindow,image_dir+pop+png)
	# pop = deck.pop()
	# popped_cards.append(pop)
	# ui.bc2(MainWindow,image_dir+pop+png)

	time.sleep(2)
	# print "Hello", STOP
	# app.processEvents()


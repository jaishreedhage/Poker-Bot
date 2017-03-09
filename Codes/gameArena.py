from handEvaluator import *
from pokerUI import *
import variables
import random
import sys
import time

#global variables

image_dir = "Images/"
png = ".png"
pot = 0
game = 0
round = ["Preflop","Flop","Turn","River"]
buy_in = 50
blind = 5

#variables to handle FOLD case
PLAYER1 = 0
PLAYER2 = 0
BOT = 0

p1_money = p2_money = bot_money = buy_in

deck = cards

#setup UI
app = QtGui.QApplication(sys.argv)
# MainWindow = QtGui.QMainWindow()
ui = Ui_MainWindow(app)
ui.setupUi(app)
ui.show()

#shuffle cards
def shuffle () :
	random.shuffle(deck)


#player1 decisions
def player1(round,PLAYER1) :
	value = 0
	print "PLAYER1 is playing" , round
	if round is "Preflop" :
		value = blind
		global p1_money
		p1_money = p1_money - blind
		print p1_money
	elif round is not "Preflop" and PLAYER1 is 2 :
		pass
	elif round is not "Preflop" and PLAYER1 is not 2 :
		#stuff need to be done here
		time.sleep(1)
		app.processEvents()
		while(variables.P1CALLCHECK is 0 and variables.P1BETRAISE is 0 and variables.P1FOLD is 0) :
			print "P1 WAITING"
			time.sleep(0.5)
			app.processEvents()
		if(variables.P1FOLD is 1) :
			PLAYER1 = 2
			variables.P1FOLD = 0
		elif(variables.P1BETRAISE is 1) :
			value = int(ui.player1bet.text())
			print value
			p1_money = p1_money - value
			print p1_money
			variables.P1BETRAISE = 0
		else :
			#take into account the different rounds
			if round is "Flop" :
				value = max(flop) - flop[0]
			elif round is "Turn" :
				value = max(turn) - turn[0]
			else :
				value = max(river) - river[0]
			print value
			p1_money = p1_money - value
			print p1_money
			variables.P1CALLCHECK = 0

	return value,PLAYER1

#player1 decisions
def player2(round,PLAYER2) :
	print "PLAYER2 is playing"
	value = 0
	if PLAYER2 is 2 :
		pass
	else :
		# app.processEvents()';'
		time.sleep(1)
		app.processEvents()
		while(variables.P2CALLCHECK is 0 and variables.P2BETRAISE is 0 and variables.P2FOLD is 0) :
			print "WAITING"
			time.sleep(0.5)
			app.processEvents()
		if(variables.P2FOLD is 1) :
			PLAYER2 = 2
			variables.P2FOLD = 0
		elif(variables.P2BETRAISE is 1) :
			value = int(ui.player2bet.text())
			print value
			global p2_money
			p2_money = p2_money - value
			print p2_money
			variables.P2BETRAISE = 0
		else :
			#take into account the different rounds
			if round is "Preflop" :
				value = max(preflop) - preflop[1]
			elif round is "Flop" :
				value = max(flop) - flop[1]
			elif round is "Turn" :
				value = max(turn) - turn[1]
			else :
				value = max(river) - river[1]
			print value
			p2_money = p2_money - value
			print p2_money
			variables.P2CALLCHECK = 0

	return value,PLAYER2



print "GAME IS GONNA START NOW"

while (variables.STOP is 0) :

	#set initial UI and variables at the start of each game
	round_name = 0        # to update the game round

	PLAYER1 = 0
	PLAYER2 = 0
	BOT = 0

	ui.cc1(app,image_dir+"facedown"+png)
	ui.cc2(app,image_dir+"facedown"+png)
	ui.cc3(app,image_dir+"facedown"+png)
	ui.cc4(app,image_dir+"facedown"+png)
	ui.cc5(app,image_dir+"facedown"+png)
	ui.p1c1(app,image_dir+"facedown"+png)
	ui.p1c2(app,image_dir+"facedown"+png)
	ui.p2c1(app,image_dir+"facedown"+png)
	ui.p2c2(app,image_dir+"facedown"+png)
	ui.bc1(app,image_dir+"facedown"+png)
	ui.bc2(app,image_dir+"facedown"+png)

	ui.p1OptionsHideShow(app,True);
	ui.p2OptionsHideShow(app,False);

	ui.p1Money(app,str(buy_in))
	ui.p2Money(app,str(buy_in))
	ui.BotMoney(app,str(buy_in))

	ui.PotMoney(app,str(pot))

	shuffle()
	popped_cards = []

	ui.GameNumber(app,str(game))
	ui.NameOfRound(app,round[round_name])

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

	app.processEvents()

	preflop = [blind,0,0]

	#variables to handle some cases -> one bot folds other bot should know, handling call/check and bet/raise
	flag = 0
	callCheck = -1     #to handle bigger case of call/check and bet/raise...presently it isnt taken into account

	while(True) :

		if(flag == 0) :
			ui.setP1Opt(app,0)

		else :
			ui.setP1Opt(app,1)

		ui.p1OptionsHideShow(app,True);
		ui.p2OptionsHideShow(app,False);

		val,PLAYER1 = player1(round[round_name],PLAYER1)

		ui.p1Money(app,str(p1_money))

		pot += val
		ui.PotMoney(app,str(pot))

		app.processEvents()

		ui.p1OptionsHideShow(app,False);
		ui.p2OptionsHideShow(app,True);

		if(flag==0) :
			flag = 1
			callCheck = 0

		ui.setP2Opt(app,callCheck)

		app.processEvents()

		val,PLAYER2 = player2(round[round_name],PLAYER2)

		preflop[1] = val

		pot += val
		ui.PotMoney(app,str(pot))

		ui.p2Money(app,str(p2_money))
		print preflop

		ui.p1OptionsHideShow(app,False);
		ui.p2OptionsHideShow(app,False);

		ui.BotPlays(app,"Bot is thinking..")

		app.processEvents()

		time.sleep(3)

		break

		# bot()


	round_name = round_name + 1
	ui.NameOfRound(app,round[round_name])

	pop = deck.pop()
	popped_cards.append(pop)
	ui.cc1(app,image_dir+pop+png)

	pop = deck.pop()
	popped_cards.append(pop)
	ui.cc2(app,image_dir+pop+png)

	pop = deck.pop()
	popped_cards.append(pop)
	ui.cc3(app,image_dir+pop+png)

	app.processEvents()

	print PLAYER1 , PLAYER2


	flop = [0]*3

	while(True) :


		ui.setP1Opt(app,1)

		ui.p1OptionsHideShow(app,True);
		ui.p2OptionsHideShow(app,False);

		val,PLAYER1 = player1(round[round_name],PLAYER1)

		pot += val
		ui.PotMoney(app,str(pot))

		flop[0] = val

		ui.p1Money(app,str(p1_money))

		app.processEvents()

		ui.p1OptionsHideShow(app,False);
		ui.p2OptionsHideShow(app,True);

		ui.setP2Opt(app,1)

		app.processEvents()

		val,PLAYER2 = player2(round[round_name],PLAYER2)

		pot += val
		ui.PotMoney(app,str(pot))

		flop[1] = val

		ui.p2Money(app,str(p2_money))
		print flop

		ui.p1OptionsHideShow(app,False);
		ui.p2OptionsHideShow(app,False);

		ui.BotPlays(app,"Bot is thinking..")

		app.processEvents()

		time.sleep(3)

		break

		# bot()
	#
	#
	round_name = round_name + 1
	ui.NameOfRound(app,round[round_name])

	pop = deck.pop()
	popped_cards.append(pop)
	ui.cc4(app,image_dir+pop+png)

	app.processEvents()

	print PLAYER1 , PLAYER2

	turn = [0]*3
	#
	while(True) :
		ui.setP1Opt(app,1)

		ui.p1OptionsHideShow(app,True);
		ui.p2OptionsHideShow(app,False);

		val,PLAYER1 = player1(round[round_name],PLAYER1)

		pot += val
		ui.PotMoney(app,str(pot))

		turn[0] = val

		ui.p1Money(app,str(p1_money))

		app.processEvents()

		ui.p1OptionsHideShow(app,False);
		ui.p2OptionsHideShow(app,True);

		ui.setP2Opt(app,1)

		app.processEvents()

		val,PLAYER2 = player2(round[round_name],PLAYER2)

		pot += val
		ui.PotMoney(app,str(pot))

		turn[1] = val

		ui.p2Money(app,str(p2_money))
		print turn

		ui.p1OptionsHideShow(app,False);
		ui.p2OptionsHideShow(app,False);

		ui.BotPlays(app,"Bot is thinking..")

		app.processEvents()

		time.sleep(3)

		break

		# bot()()

	print PLAYER1 , PLAYER2
#
	#
	round_name = round_name + 1
	ui.NameOfRound(app,round[round_name])

	pop = deck.pop()
	popped_cards.append(pop)
	ui.cc5(app,image_dir+pop+png)

	app.processEvents()
	#
	river = [0] * 3
	#
	while(True) :
		ui.setP1Opt(app,1)

		ui.p1OptionsHideShow(app,True);
		ui.p2OptionsHideShow(app,False);

		val,PLAYER1 = player1(round[round_name],PLAYER1)

		pot += val
		ui.PotMoney(app,str(pot))

		river[0] = val

		ui.p1Money(app,str(p1_money))

		app.processEvents()

		ui.p1OptionsHideShow(app,False);
		ui.p2OptionsHideShow(app,True);

		ui.setP2Opt(app,1)

		app.processEvents()

		val,PLAYER2 = player2(round[round_name],PLAYER2)

		pot += val
		ui.PotMoney(app,str(pot))

		river[1] = val

		ui.p2Money(app,str(p2_money))
		print river

		ui.p1OptionsHideShow(app,False);
		ui.p2OptionsHideShow(app,False);

		ui.BotPlays(app,"Bot is thinking..")

		app.processEvents()

		time.sleep(3)

		break

		# bot()
	#
	# winner()

	app.processEvents()


	time.sleep(2)

	print "GAME ", game, "IS OVER"
	deck = deck + popped_cards
	print len(deck)
	game = game + 1

if variables.STOP is 1 :
	sys.exit(app.exec_())

from handEvaluator import *
from pokerUI import *
from handStrength import *
from knowledgeBase import *
import variables
import random
import sys
import time

#global variables

csv_flop = "flop_base"
csv_turn = 'turn_base'
csv_river = 'river_base'

BOT_WON = 0

headers = ['Fold','Check','Call','Bet-1','Bet-2','Bet-5','Bet-7']

image_dir = "Images/"
png = ".png"
pot = 0
game = 1
round = ["Preflop","Flop","Turn","River"]
buy_in = 80
blind = 3

#skip_game variable
skip_game = 0

#variables to handle FOLD case
PLAYER1 = 0
PLAYER2 = 0
BOT = 0

p1_money = p2_money = bot_money = buy_in

deck = cards
popped_cards = []

#setup UI
app = QtGui.QApplication(sys.argv)
# MainWindow = QtGui.QMainWindow()
ui = Ui_MainWindow(app)
ui.setupUi(app)
ui.show()

#shuffle cards
def shuffle () :
	random.shuffle(deck)

#bot on basis of action is updating few values
def bot_action(action,game_round,BOT) :

	global bot_money

	value = 0

	if action == "Fold" :
		print "HELLO"
		BOT = 2
	elif action == "Call" or action == "Check":
		value = max(game_round) - game_round[2]
	elif action == "Bet-1" :
		value = max(game_round) + 1
	elif action == "Bet-2" :
		value = max(game_round) + 2
	elif action == "Bet-5" :
		value = max(game_round) + 5
	elif action == "Bet-7" :
		value = max(game_round) + 7

	bot_money -= value
	print bot_money,value,game_round

	return value,BOT

#skip game as two players have folded
def skipGame () :

	global skip_game
	global pot
	global game
	global deck
	global popped_cards

	if([PLAYER1,PLAYER2,BOT].count(2) is 2) :
		if(PLAYER1 is not 2) :
			global p1_money
			p1_money += pot
			pot = 0
		elif(PLAYER2 is not 2) :
			global p2_money
			p2_money += pot
			pot = 0
		else :
			global bot_money
			bot_money += pot
			pot = 0

		ui.p1Money(app,str(p1_money))
		ui.p2Money(app,str(p2_money))
		ui.BotMoney(app,str(bot_money))

		ui.PotMoney(app,str(pot))

		app.processEvents()

		time.sleep(2)

		print "GAME ", game, "IS OVER"
		deck = deck + popped_cards
		game = game + 1
		skip_game = 1

	return skip_game

#card checker for different players
def card_checker(player_cards,community_cards) :

	high_card = highCard(player_cards)

	if royalFlush(player_cards+community_cards) is "yes" :
		return 1,royalFlush(player_cards+community_cards), high_card
	elif len(straightFlush(player_cards+community_cards)) is not 0 :
		return 2,straightFlush(player_cards+community_cards), high_card
	elif len(fourOfAKind(player_cards+community_cards)) is not 0 :
		return 3,fourOfAKind(player_cards+community_cards), high_card
	elif len(fullHouse(player_cards+community_cards)) is not 0:
		return 4,fullHouse(player_cards+community_cards), high_card
	elif len(flush(player_cards+community_cards)) is not 0 :
		return 5,flush(player_cards+community_cards), high_card
	elif len(straight(player_cards+community_cards)) is not 0 :
		return 6,straight(player_cards+community_cards), high_card
	elif len(threeOfAKind(player_cards+community_cards)) is not 0 :
		return 7,threeOfAKind(player_cards+community_cards), high_card
	elif len(twoPair(player_cards+community_cards)) is not 0 :
		return 8,twoPair(player_cards+community_cards), high_card
	elif len(onePair(player_cards+community_cards)) is not 0 :
		return 9,onePair(player_cards+community_cards), high_card
	else :
		return 10,[],high_card


#decide between two players
def win_between_two_players(player1,player2,community_cards,P1,P2) :

	if(P1 is 2 and P2 is 2) :
		return [],0
	elif(P1 is 2) :
		return player2,2
	elif(P2 is 2) :
		return player1,1
	else :
		#player1
		best_hand_1 = card_checker(player1,community_cards)[0]
		best_card_1 = card_checker(player1,community_cards)[1]
		high_card_1 = card_checker(player1,community_cards)[2]

		#player2
		best_hand_2 = card_checker(player2,community_cards)[0]
		best_card_2 = card_checker(player2,community_cards)[1]
		high_card_2 = card_checker(player2,community_cards)[2]

		print best_hand_1,best_hand_2

		if(best_hand_1 > best_hand_2) :
			return player2,2
		elif(best_hand_1 < best_hand_2) :
			return player1,1
		else :
			#TODO:for now not considering the fact that two three of a kind exist, and the one with greater three of a kind would be given preference
			if(card_rank[high_card_1[1:]] > card_rank[high_card_2[1:]] ) :
				return player1,1
			else :
				return player2,2
			#not considering case when high cards are equal, have to see the next highest high card


#GAME deciding who won
def winner(player1_cards,player2_cards,bot_cards,community_cards) :
	print "CHECKING WHO WON THE GAME ",game

	global PLAYER1
	global PLAYER2
	global BOT
	global bot_money
	global p1_money
	global p2_money

	print player1_cards,player2_cards,bot_cards,community_cards

	PLAYERS = [PLAYER1,PLAYER2,BOT]

	print PLAYER1, PLAYER2, BOT

	player,person = win_between_two_players(player1_cards,player2_cards,community_cards,PLAYER1,PLAYER2)
	if player is [] :
		bot_money += pot
		BOT_WON = 1
		ui.BotMoney(app,str(bot_money))
	else :
		person_temp = person
		player,person = win_between_two_players(player,bot_cards,community_cards,PLAYERS[person-1],BOT)
		print player
		if(person is 2):
			print "PLAYER %d won" %(person+1)
			bot_money += pot
			BOT_WON = 1
			ui.BotMoney(app,str(bot_money))
		else :
			print "PLAYER %d won" %person_temp
			if(person_temp is 1):
				p1_money += pot
				ui.p1Money(app,str(p1_money))
			else :
				p2_money += pot
				ui.p2Money(app,str(p2_money))

	app.processEvents()




#checking what card bot has
def bot(bot_cards,community_cards) :
	print "CHECKING IF BOT HAS SOMETHING"

	best_hand = card_checker(bot_cards,community_cards)[0]
	best_card = card_checker(bot_cards,community_cards)[1]
	high_card = card_checker(bot_cards,community_cards)[2]

	print best_hand, best_card , high_card


def bot_preflop(bot_cards) :

	global bot_money

	bet = 2
	value = 0

	if(check_best_hand(bot_cards) == 8):
		value = max(preflop) + bet
		bot_money -= value

	print value, bot_money
	return value


#player1 decisions
def player1(round,PLAYER1) :
	value = 0
	print "PLAYER1 is playing" , round
	if round is "Preflop" :
		# value = blind
		# global p1_money
		# p1_money = p1_money - blind
		if preflop[0] is 0 :
			value = blind
			global p1_money
			p1_money = p1_money - value
		elif PLAYER1 is 2:
			pass
		else :
			time.sleep(0.1)
			app.processEvents()
			while(variables.P1CALLCHECK is 0 and variables.P1BETRAISE is 0 and variables.P1FOLD is 0 and variables.STOP is 0) :
				time.sleep(0.1)
				app.processEvents()
			if(variables.STOP is 1) :
				return value,PLAYER1
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
				value = max(preflop) - preflop[0]
				p1_money = p1_money - value
				print p1_money
				variables.P1CALLCHECK = 0

		# print p1_money
	elif round is not "Preflop" and PLAYER1 is 2 :
		pass
	elif round is not "Preflop" and PLAYER1 is not 2 :
		#stuff need to be done here
		time.sleep(0.1)
		app.processEvents()
		while(variables.P1CALLCHECK is 0 and variables.P1BETRAISE is 0 and variables.P1FOLD is 0 and variables.STOP is 0) :
			time.sleep(0.1)
			app.processEvents()

		if(variables.STOP is 1) :
			return value,PLAYER1
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
		time.sleep(0.1)
		app.processEvents()
		while(variables.P2CALLCHECK is 0 and variables.P2BETRAISE is 0 and variables.P2FOLD is 0 and variables.STOP is 0) :
			time.sleep(0.1)
			app.processEvents()
		if(variables.STOP is 1) :
			return value,PLAYER2
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

	skip_game = 0

	PLAYER1 = 0
	PLAYER2 = 0
	BOT = 0

	pot = 0

	bot_cards = []
	player1_cards = []
	player2_cards = []
	community_cards = []

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

	ui.p1Money(app,str(p1_money))
	ui.p2Money(app,str(p2_money))
	ui.BotMoney(app,str(bot_money))

	ui.PotMoney(app,str(pot))

	shuffle()
	popped_cards = []

	ui.GameNumber(app,str(game))
	ui.NameOfRound(app,round[round_name])

	pop = deck.pop()
	popped_cards.append(pop)
	player1_cards.append(pop)
	ui.p1c1(app,image_dir+pop+png)

	pop = deck.pop()
	popped_cards.append(pop)
	player1_cards.append(pop)
	ui.p1c2(app,image_dir+pop+png)

	pop = deck.pop()
	popped_cards.append(pop)
	player2_cards.append(pop)
	ui.p2c1(app,image_dir+pop+png)

	pop = deck.pop()
	popped_cards.append(pop)
	player2_cards.append(pop)
	ui.p2c2(app,image_dir+pop+png)

	pop = deck.pop()
	popped_cards.append(pop)
	bot_cards.append(pop)
	ui.bc1(app,image_dir+pop+png)

	pop = deck.pop()
	popped_cards.append(pop)
	bot_cards.append(pop)
	ui.bc2(app,image_dir+pop+png)

	app.processEvents()

	preflop = [0]*3

	#variables to handle some cases -> one bot folds other bot should know, handling call/check and bet/raise
	flag = 0
	callCheck = -1     #to handle bigger case of call/check and bet/raise...presently it isnt taken into account

	while(True) :

		if(flag == 0) :
			ui.setP1Opt(app,0)

		else :
			ui.setP1Opt(app,1)

		ui.p1OptionsHideShow(app,True)
		ui.p2OptionsHideShow(app,False)

		if(skipGame() is 1) :
			break

		val,PLAYER1 = player1(round[round_name],PLAYER1)

		if(variables.STOP is 1) :
			break

		preflop[0] += val

		ui.p1Money(app,str(p1_money))
		ui.player1bet.setText("")

		pot += val
		ui.PotMoney(app,str(pot))

		app.processEvents()

		ui.p1OptionsHideShow(app,False)
		ui.p2OptionsHideShow(app,True)

		if(flag==0) :
			flag = 1
			callCheck = 0

		ui.setP2Opt(app,callCheck)

		app.processEvents()

		if(skipGame() is 1) :
			break

		val,PLAYER2 = player2(round[round_name],PLAYER2)

		if(variables.STOP is 1) :
			break

		preflop[1] += val

		pot += val
		ui.PotMoney(app,str(pot))

		ui.p2Money(app,str(p2_money))
		ui.player2bet.setText("")
		print preflop

		ui.p1OptionsHideShow(app,False)
		ui.p2OptionsHideShow(app,False)

		if(skipGame() is 1) :
			break

		print "Bot is thinking...."
		ui.BotPlays(app,"Bot is thinking..")

		app.processEvents()

		time.sleep(3)

		BOTCHECK = 0
		val = bot_preflop(bot_cards)
		print val
		if val is 0	:
			val = max(preflop) - preflop[2]
			BOTCHECK = 1
			bot_money -= val

		preflop[2] += val

		pot += val
		ui.PotMoney(app,str(pot))
		ui.BotMoney(app,str(bot_money))

		if BOTCHECK is 1 :
			ui.BotPlays(app,"Bot decides to check")

		else :
			ui.BotPlays(app,"Bot decides to raise "+ val)

		app.processEvents()

		time.sleep(2)

		ui.BotPlays(app,"")

		PLAYERS = [PLAYER1,PLAYER2,BOT]
		eq = -1
		stopPreflop = 1
		for i in range(0,3) :
			if PLAYERS[i]!=2 and eq is -1:
				eq = preflop[i]
			if PLAYERS[i]!=2 and eq is not -1 and preflop[i]!=eq:
				stopPreflop = 0
				break

		if stopPreflop is 1 :
			print "THEY ARE ALL EQUAL"
			break

		else :
			print "NO THEY ARENT EQUAL"


	if(variables.STOP is 1) :
		break

	if(skip_game is 1) :
		continue


	round_name = round_name + 1
	ui.NameOfRound(app,round[round_name])

	pop = deck.pop()
	popped_cards.append(pop)
	community_cards.append(pop)
	ui.cc1(app,image_dir+pop+png)

	pop = deck.pop()
	popped_cards.append(pop)
	community_cards.append(pop)
	ui.cc2(app,image_dir+pop+png)

	pop = deck.pop()
	popped_cards.append(pop)
	community_cards.append(pop)
	ui.cc3(app,image_dir+pop+png)

	app.processEvents()

	print PLAYER1 , PLAYER2


	flop = [0]*3

	while(True) :


		ui.setP1Opt(app,1)

		ui.p1OptionsHideShow(app,True)
		ui.p2OptionsHideShow(app,False)

		if(skipGame() is 1) :
			break

		val,PLAYER1 = player1(round[round_name],PLAYER1)

		if(variables.STOP is 1) :
			break

		pot += val
		ui.PotMoney(app,str(pot))

		flop[0] += val

		ui.p1Money(app,str(p1_money))
		ui.player1bet.setText("")

		app.processEvents()

		ui.p1OptionsHideShow(app,False);
		ui.p2OptionsHideShow(app,True);

		ui.setP2Opt(app,1)

		app.processEvents()

		if(skipGame() is 1) :
			break

		val,PLAYER2 = player2(round[round_name],PLAYER2)

		if(variables.STOP is 1) :
			break

		pot += val
		ui.PotMoney(app,str(pot))

		flop[1] += val

		ui.p2Money(app,str(p2_money))
		ui.player2bet.setText("")
		print flop

		ui.p1OptionsHideShow(app,False)
		ui.p2OptionsHideShow(app,False)

		if(skipGame() is 1) :
			break

		if BOT is not 2:

			ui.BotPlays(app,"Bot is thinking..")

			app.processEvents()

			time.sleep(3)

			hand_strength = handStrength(bot_cards + community_cards)

			max_choice,max_choice_idx,idx = read_file(csv_flop,hand_strength)

			print hand_strength,max_choice,max_choice_idx,idx

			if max_choice == 0 :
				max_choice_idx = random.randint(0,6)
				print "max_choice = ",max_choice_idx

			print "Random Chosen Action Flop = ", headers[max_choice_idx]

			val,BOT = bot_action(headers[max_choice_idx],flop,BOT)
			knowledge_update['flop_base'][0] = max_choice_idx
			knowledge_update['flop_base'][1] = idx

			print val,BOT

			pot += val
			ui.PotMoney(app,str(pot))

			flop[2] += val

			ui.BotMoney(app,str(bot_money))

			ui.BotPlays(app,"Bot has decided to "+headers[max_choice_idx])

			time.sleep(2)

			ui.BotPlays(app,"")

		PLAYERS = [PLAYER1,PLAYER2,BOT]
		eq = -1
		stopFlop = 1
		for i in range(0,3) :
			if PLAYERS[i]!=2 and eq is -1:
				eq = flop[i]
			if PLAYERS[i]!=2 and eq is not -1 and flop[i]!=eq:
				stopFlop = 0
				break

		if stopFlop is 1 :
			print "THEY ARE ALL EQUAL"
			break

		else :
			print "NO THEY ARENT EQUAL"



	if(variables.STOP is 1) :
		break

	if(skip_game is 1) :
		continue

	#
	#
	round_name = round_name + 1
	ui.NameOfRound(app,round[round_name])

	pop = deck.pop()
	popped_cards.append(pop)
	community_cards.append(pop)
	ui.cc4(app,image_dir+pop+png)

	app.processEvents()

	print PLAYER1 , PLAYER2

	turn = [0]*3
	#
	while(True) :
		ui.setP1Opt(app,1)

		ui.p1OptionsHideShow(app,True)
		ui.p2OptionsHideShow(app,False)

		if(skipGame() is 1) :
			break

		val,PLAYER1 = player1(round[round_name],PLAYER1)

		if(variables.STOP is 1) :
			break

		pot += val
		ui.PotMoney(app,str(pot))

		turn[0] += val

		ui.p1Money(app,str(p1_money))
		ui.player1bet.setText("")

		app.processEvents()

		ui.p1OptionsHideShow(app,False)
		ui.p2OptionsHideShow(app,True)

		ui.setP2Opt(app,1)

		app.processEvents()

		if(skipGame() is 1) :
			break

		val,PLAYER2 = player2(round[round_name],PLAYER2)

		if(variables.STOP is 1) :
			break

		pot += val
		ui.PotMoney(app,str(pot))

		turn[1] += val

		ui.p2Money(app,str(p2_money))
		ui.player2bet.setText("")
		print turn

		ui.p1OptionsHideShow(app,False)
		ui.p2OptionsHideShow(app,False)

		if(skipGame() is 1) :
			break

		if BOT is not 2 :

			ui.BotPlays(app,"Bot is thinking..")

			app.processEvents()

			time.sleep(3)

			hand_strength = handStrength(bot_cards + community_cards)

			max_choice,max_choice_idx,idx = read_file(csv_turn,hand_strength)

			print hand_strength,max_choice,max_choice_idx,idx

			if max_choice == 0 :
				max_choice_idx = random.randint(0,6)
				print "max_choice = ",max_choice_idx


			print "Random Chosen Action Turn = ", headers[max_choice_idx]

			val,BOT = bot_action(headers[max_choice_idx],turn,BOT)

			knowledge_update['turn_base'][0] = max_choice_idx
			knowledge_update['turn_base'][1] = idx


			print val,BOT

			pot += val
			ui.PotMoney(app,str(pot))

			turn[2] += val

			ui.BotMoney(app,str(bot_money))

			ui.BotPlays(app,"Bot has decided to "+headers[max_choice_idx])

			time.sleep(2)

			ui.BotPlays(app,"")

		#
		PLAYERS = [PLAYER1,PLAYER2,BOT]
		eq = -1
		stopTurn = 1
		for i in range(0,3) :
			if PLAYERS[i]!=2 and eq is -1:
				eq = turn[i]
			if PLAYERS[i]!=2 and eq is not -1 and turn[i]!=eq:
				stopTurn = 0
				break

		if stopTurn is 1 :
			print "THEY ARE ALL EQUAL"
			break

		else :
			print "NO THEY ARENT EQUAL"





	if(variables.STOP is 1) :
		break

	if(skip_game is 1) :
		continue



	print PLAYER1 , PLAYER2
#
	#
	round_name = round_name + 1
	ui.NameOfRound(app,round[round_name])

	pop = deck.pop()
	popped_cards.append(pop)
	community_cards.append(pop)
	ui.cc5(app,image_dir+pop+png)

	app.processEvents()
	#
	river = [0] * 3
	#
	while(True) :
		ui.setP1Opt(app,1)

		ui.p1OptionsHideShow(app,True)
		ui.p2OptionsHideShow(app,False)

		if(skipGame() is 1) :
			break

		val,PLAYER1 = player1(round[round_name],PLAYER1)

		if(variables.STOP is 1) :
			break

		pot += val
		ui.PotMoney(app,str(pot))

		river[0] += val

		ui.p1Money(app,str(p1_money))
		ui.player1bet.setText("")

		app.processEvents()

		ui.p1OptionsHideShow(app,False)
		ui.p2OptionsHideShow(app,True)

		ui.setP2Opt(app,1)

		app.processEvents()

		if(skipGame() is 1) :
			break

		val,PLAYER2 = player2(round[round_name],PLAYER2)

		if(variables.STOP is 1) :
			break

		pot += val
		ui.PotMoney(app,str(pot))

		river[1] += val

		ui.p2Money(app,str(p2_money))
		ui.player2bet.setText("")
		print river

		ui.p1OptionsHideShow(app,False)
		ui.p2OptionsHideShow(app,False)

		if(skipGame() is 1) :
			break


		if BOT is not 2 :

			ui.BotPlays(app,"Bot is thinking..")

			app.processEvents()

			time.sleep(3)

			hand_strength = handStrength(bot_cards + community_cards)

			max_choice,max_choice_idx,idx = read_file(csv_river,hand_strength)

			print hand_strength,max_choice,max_choice_idx,idx

			if max_choice == 0 :
				max_choice_idx = random.randint(0,6)
				print "max_choice = ",max_choice_idx


			print "Random Chosen Action River = ", headers[max_choice_idx]

			val,BOT = bot_action(headers[max_choice_idx],river,BOT)
			knowledge_update['river_base'][0] = max_choice_idx
			knowledge_update['river_base'][1] = idx

			print val,BOT

			pot += val
			ui.PotMoney(app,str(pot))


			river[2] += val

			ui.BotMoney(app,str(bot_money))

			ui.BotPlays(app,"Bot has decided to "+headers[max_choice_idx])

			time.sleep(2)

			ui.BotPlays(app,"")



		PLAYERS = [PLAYER1,PLAYER2,BOT]
		eq = -1
		stopRiver = 1
		for i in range(0,3) :
			if PLAYERS[i]!=2 and eq is -1:
				eq = river[i]
			if PLAYERS[i]!=2 and eq is not -1 and river[i]!=eq:
				stopRiver = 0
				break

		if stopRiver is 1 :
			print "THEY ARE ALL EQUAL"
			break

		else :
			print "NO THEY ARENT EQUAL"




	if(variables.STOP is 1) :
		break

	if(skip_game is 1) :
		continue

	person = winner(player1_cards,player2_cards,bot_cards,community_cards)

	if(BOT_WON == 1):
		print "Bot won so updating knowledge base"
		reward = pot - (preflop[2] + flop[2] + turn[2] + river[2])
		for csv_file in knowledge_update.keys():
			write_file(csv_file,reward)

	else :
		print "bot lost so updating knowledge base"
		reward = -(preflop[2] + flop[2] + turn[2] + river[2])
		for csv_file in knowledge_update.keys():
			write_file(csv_file,reward)

	app.processEvents()


	time.sleep(2)

	print "GAME ", game, "IS OVER"
	deck = deck + popped_cards
	game = game + 1

print "GAME ENDED BY USER"

if variables.STOP is 1 :
	sys.exit(app.exec_())

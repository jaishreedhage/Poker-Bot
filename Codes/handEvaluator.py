#pack of 52 cards - Diamond,Clubs,Spades,Heart
cards = ['DA','D2','D3','D4','D5','D6','D7','D8','D9','D10','DJ','DQ','DK',
		 'CA','C2','C3','C4','C5','C6','C7','C8','C9','C10','CJ','CQ','CK',
		 'SA','S2','S3','S4','S5','S6','S7','S8','S9','S10','SJ','SQ','SK',
		 'HA','H2','H3','H4','H5','H6','H7','H8','H9','H10','HJ','HQ','HK' ]

#rank of each card
cardRank = { '2' : 1,
			 '3' : 2,
			 '4' : 3,
			 '5' : 4,
			 '6' : 5,
			 '7' : 6,
			 '8' : 7,
			 '9' : 8,
			 '10' : 9,
			 'J' : 10,
			 'Q' : 11,
			 'K' : 12,
			 'A' : 13 }

cardValue = { 'A' : 1,
			  '2' : 2,
			  '3' : 3,
			  '4' : 4,
			  '5' : 5,
			  '6' : 6,
			  '7' : 7,
			  '8' : 8,
			  '9' : 9,
			  '10': 10,
			  'J' : 11,
			  'Q' : 12,
			  'K' : 13 }			  
#card suit
suit = ['D','H','C','S']

#highest card in the hand(and amongst the 7 cards)
def highCard (hand) :
	noOfCards = len(hand)
	cardValue = hand[0]
	highest = hand[0][1:]
	for i in range (1,noOfCards) :
		if (cardRank[hand[i][1:]] > cardRank[highest]) :
			highest = hand[i][1:]
			cardValue = hand[i]

	return cardValue

#checking for 3 of a kind in the hand(and amongst the 7 cards)
def threeOfAKind (hand) :
	noOfCards = len(hand)
	cardPair = []
	cardValue = 'null'
	for i in range (0,noOfCards) :
		count = 1
		flag=0
		for j in range (0,noOfCards) :
			if (i!=j and hand[i][1:] == hand[j][1:]) :
				count = count+1
				
		if (count == 3) :
			cardValue = hand[i][1:]
			if (cardValue not in cardPair) :
				cardPair.append(cardValue)

	return cardPair

#checking for 4 of a kind in the hand(and amongst the 7 cards)
def fourOfAKind (hand) :
	noOfCards = len(hand)
	cardValue = 'null'
	for i in range (0,noOfCards) :
		count = 1
		flag=0
		for j in range (0,noOfCards) :
			if (i!=j and hand[i][1:] == hand[j][1:]) :
				count = count+1
				if (count==4) :
					cardValue = hand[i][1:]
					flag = 1;
					break
		if (flag==1) :
			break

	return cardValue

#checking for one pair in hand(and amongst the 7 cards)
def onePair (hand) :
	noOfCards = len(hand)
	cardPair = []
	cardValue = 'null'
	pairs = 0
	for i in range (0,noOfCards) :
		count = 1
		flag=0
		for j in range (0,noOfCards) :
			if (i!=j and hand[i][1:] == hand[j][1:]) :
				count = count+1
				
		if (count==2) :
			cardValue = hand[i][1:]
			if (not cardValue in cardPair) :
				cardPair.append(cardValue)
				pairs = pairs + 1

	if (pairs!=1) :
		cardPair = []

	return cardPair

#checking for twp pair in hand(and amongst the 7 cards)
def twoPair (hand) :
	noOfCards = len(hand)
	cardPair = []
	cardValue = 'null'
	pairs = 0
	for i in range (0,noOfCards) :
		count = 1
		for j in range (0,noOfCards) :
			if (i!=j and hand[i][1:] == hand[j][1:]) :
				count = count+1
				
		if (count==2 and pairs < 2) :
			cardValue = hand[i][1:]
			if (not cardValue in cardPair) :
				cardPair.append(cardValue)
			pairs = pairs + 1

		elif (count==2 and pairs >= 2) :
			cardValue = hand[i][1:]
			if (not cardValue in cardPair) :
				minCard = 0
				for k in range (0,len(cardPair)) :
					if (cardRank[hand[i][1:]] < cardRank[cardPair[minCard]] ) :
						minCard = k
				cardPair[k] = hand[i][1:]

	return cardPair

#searching for a flush in hand(and amnogst the 7 cards)
def flush (hand) :
	noOfCards = len(hand)
	flushSuit = 'null'
	for i in range (0,len(suit)) :
		count = 0 
		for j in range (0,noOfCards) :
			if (suit[i] == hand[j][0]) :
				count = count + 1
		if (count >= 5) :
			flushSuit = suit[i]
			break

	return flushSuit

#check for a royal flush
def royalFlush (hand) :
	royal_flush = 'null'
	flushSuit = flush(hand)
	if (flushSuit == 'null') :
		return royal_flush
	else :
		noOfCards = len(hand)
		count = 0
		for i in range (0,noOfCards) :
			if (hand[i][0] == flushSuit and ( hand[i][1:] == '10' or hand[i][1:] == 'J' or hand[i][1:] == 'Q' or hand[i][1:] == 'K' or hand[i][1:] == 'A')) :
				count = count + 1

		if (count is 5) :
			royal_flush = 'yes'

	return royal_flush


#check for a straight given a set of 5 or more cards
#returning the sequence of consecutive cards if community cards are < 3 in order to inform the bot about the possibility of a straight formation
#returns the highest straight possible if count of community cards >= 3
#returns False if no straight is possible
#handling seperately the case for the straight between [10 J Q K A] seperately

# TODO := Here if i get a [10,A] as my inital cards and i have [Q,K,{Card Set} - {10,J,K,Q,A}] so i want to return the possible straights too

def straight (hand):
	spl_hand = hand
	spl_hand = sorted(hand,key = lambda x : cardRank[''.join((list(x))[1:])],reverse = True) #list declared in order to seperately handle [10 J Q K A]
	hand = sorted(hand,key = lambda x : cardValue[''.join((list(x))[1:])])

	handValue = []
	handRank = []		#list taken in order to make comparison easier
	for card in hand:
		handValue.append(cardValue[''.join((list(card))[1:])])

	for card in spl_hand:
		handRank.append(cardRank[''.join((list(card))[1:])])

	def evaluateStraight(checkList):
		count = 0
		for i in range(0,len(checkList)-1) :
			if (checkList[i+1] - checkList[i] == 1) :
				count = count + 1
			else :
				break
		if (count == len(checkList)-1) :
			return True
		else :
			return False

	# Straight of Highest order handled here
	if(handRank[0:5] == [13, 12, 11, 10, 9]):
		spl_straight = (spl_hand[0:5])
		spl_straight.reverse()
		return spl_straight

	else :
		straightList = []
		index = 0
		straight_flag = 0
		for i in range(0,(len(hand))%5 + 1):
			checkList = handValue[i : 5 + i]
			if (evaluateStraight(checkList) and (checkList > straightList)) :
				straightList = checkList
				index = i
				straight_flag = 1

		if (straight_flag) :
			return hand[index : 5 + index]
		else :
			return False

#check for straight flush in a hand of 5 or more cards
#returns False if not a straight flush else returns the hand sequence
#handled the case where i have 2 cards with same number say [CA,HA] on which makes a straight flush and other just a straight. Function returns the hand with straight flush
#Test case => ['CA', 'HA', 'CK', 'CQ', 'CJ', 'C10', 'H2']
def straightFlush(hand):
	temp = []
	if (straight(hand) == False):
		flush_suit = flush(hand)
		for card in hand :
			if (list(card)[0] == flush_suit) :
				temp.append(card)
		return straight(temp)
	else :
		hand = straight(hand)
		if (flush(hand)):
			return hand
		else :
			return False



def fullHouse(hand):
	temp = hand
	three_card_val = threeOfAKind(temp)

	def cardScrapper(card_list,value):
		temp_list = []
		for i in range(0,len(card_list)) :
			if ((card_list[i][1:]) == (value[0])) :
				temp_list.append(card_list[i])
		return temp_list

	three_cards = cardScrapper(hand,three_card_val)

	for card in three_cards :
		temp.remove(card)

	one_pair_val = onePair(temp)
	one_pair_list = cardScrapper(temp,one_pair_val)

	final_list = three_cards + one_pair_list
	return final_list


#hand = ['D4','SA','DA','H4','C4','DA']
#hand = ['D1','H2','S5','C4','H3','S6','D7']
#hand = ['DJ','SA','H10','H7','CK','D4','SQ']
#hand = ['D10','SA','H5','H7','C6','DJ']
hand = ['D10','HQ','H10','S10','CQ','HJ','C9']

#print threeOfAKind(hand)
print fullHouse(hand)
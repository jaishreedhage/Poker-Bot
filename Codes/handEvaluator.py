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

	return cardValue

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

#check for full house
def fullHouse (hand) :
	noOfCards = len(hand)
	cardPair = []
	three_of_a_kind = threeOfAKind(hand)
	two_pair = twoPair(hand)
	if (len(three_of_a_kind) == 0) :
		pass
	elif (len(three_of_a_kind) == 1) :
		if (len(two_pair) == 0) :
			pass
		elif (len(two_pair) == 1) :
			cardPair.append(three_of_a_kind)
			cardPair.append(two_pair)
		elif (len(two_pair) > 1) :
			# cardPair.   yet to write..........
			pass

	return cardPair


hand = ['C9','HJ','CQ','S10','H10','HQ','D10']
print threeOfAKind(hand)
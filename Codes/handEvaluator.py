#pack of 52 cards - Diamond,Clubs,Spades,Heart
cards = ['DA','D2','D3','D4','D5','D6','D7','D8','D9','D10','DJ','DQ','DK',
		 'CA','C2','C3','C4','C5','C6','C7','C8','C9','C10','CJ','CQ','CK',
		 'SA','S2','S3','S4','S5','S6','S7','S8','S9','S10','SJ','SQ','SK',
		 'HA','H2','H3','H4','H5','H6','H7','H8','H9','H10','HJ','HQ','HK' ]

#rank of each card
card_rank = { '2' : 1,
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

card_rank2 = { 'A' : 1,
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

#function returning the card list from a list of card values
def valuetoCard(card_value_list,hand):
	hand = sorted(hand,key = lambda x : card_rank2[''.join((list(x))[1:])])
	final_hand = []
	value = lambda x : card_rank2[''.join((list(x))[1:])]
	for card_value in card_value_list:
		count = 1
		for card in hand:
			if value(card) == card_value and (count == 1):
				final_hand.append(card)
				count += 1
				continue

	return final_hand

#function scrapping off a set of cards with same numeric rank or value
def cardScrapper(card_list,value):
	scrap_list = []
	for i in range(0,len(card_list)) :
		if ((card_list[i][1:]) == (value[0])) :
			scrap_list.append(card_list[i])
	return scrap_list


#highest card in the hand(and amongst the 7 cards) returns the card with the highest value
def highCard (hand) :
	no_of_cards = len(hand)
	high_card = hand[0]
	highest = hand[0][1:]
	for i in range (1,no_of_cards) :
		if (card_rank[hand[i][1:]] > card_rank[highest]) :
			highest = hand[i][1:]
			high_card = hand[i]

	return high_card

#checking for 3 of a kind in the hand(and amongst the 7 cards)
def threeOfAKind (hand) :
	no_of_cards = len(hand)
	three_of_kind = []
	for i in range (0,no_of_cards) :
		count = 1
		flag=0
		for j in range (0,no_of_cards) :
			if (i!=j and hand[i][1:] == hand[j][1:]) :
				count = count+1

		if (count == 3) :
			card_value = hand[i][1:]
			if (card_value not in three_of_kind) :
				three_of_kind.append(card_value)

	return three_of_kind

#checking for 4 of a kind in the hand(and amongst the 7 cards)
def fourOfAKind (hand) :
	no_of_cards = len(hand)
	four_of_kind = []

	for i in range (0,no_of_cards) :
		count = 1
		flag=0
		for j in range (0,no_of_cards) :
			if (i!=j and hand[i][1:] == hand[j][1:]) :
				count = count+1
				if (count==4) :
					four_of_kind.append(hand[i][1:])
					flag = 1;
					break
				if (flag==1) :
					break

	return four_of_kind

#checking for one pair in hand(and amongst the 7 cards)
def onePair (hand) :
	no_of_cards = len(hand)
	card_pair = []
	card_value = 'null'
	count_pair = 0
	for i in range (0,no_of_cards) :
		count = 1
		flag=0
		for j in range (0,no_of_cards) :
			if (i!=j and hand[i][1:] == hand[j][1:]) :
				count = count+1

		if (count==2) :
			card_value = hand[i][1:]
			if (not card_value in card_pair) :
				card_pair.append(card_value)
				count_pair = count_pair + 1

	if (count_pair!=1) :
		card_pair = []

	return card_pair

#checking for twp pair in hand(and amongst the 7 cards)
#NOTE :- check the old twoPair for the test case hand = ['CA', 'HA', 'CK', 'C10', 'SK', 'CJ', 'H10'] that its wrong
def twoPair (hand) :
	no_of_cards = len(hand)
	card_pair = []
	card_value = 'null'
	count_pair = 0
	for i in range (0,no_of_cards) :
		count = 1
		for j in range (i+1,no_of_cards) :     			# CHANGED := loop index range changed from 0 -> no_of_cards to i+1 -> no_of_cards in order to remove repetitve cases
			if (i!=j and hand[i][1:] == hand[j][1:]) :
				count = count+1

		if (count==2 and count_pair < 2) :
			card_value = hand[i][1:]
			if (not card_value in card_pair) :
				card_pair.append(card_value)
			count_pair = count_pair + 1


		elif (count==2 and count_pair >= 2) :
			card_value = hand[i][1:]
		 	card_pair.append(card_value)				# CHANGED := made the two pair code more efficient as it wasnt working for a test case hand = ['CA', 'HA', 'CK', 'C10', 'SK', 'CJ', 'H10']
			min_card_value = 14
			for value in card_pair:
				if card_rank[value] < min_card_value:
					min_card_value = value
			card_pair.remove(min_card_value)

	if (len(card_pair) < 2) :
		card_pair = []

	return card_pair

#searching for a flush in hand(and amnogst the 7 cards)
def flush (hand) :
	no_of_cards = len(hand)
	flush_suit = []

	for i in range (0,len(suit)) :
		count = 0
		for j in range (0,no_of_cards) :
			if (suit[i] == hand[j][0]) :
				count = count + 1
		if (count >= 5) :
			flush_suit.append(suit[i])
			break

	return flush_suit

#check for a royal flush
def royalFlush (hand) :
	royal_flush = 'null'
	flush_suit = flush(hand)
	if (flush_suit == []) :
		return royal_flush
	else :
		no_of_cards = len(hand)
		count = 0
		for i in range (0,no_of_cards) :
			if (hand[i][0] == flush_suit and ( hand[i][1:] == '10' or hand[i][1:] == 'J' or hand[i][1:] == 'Q' or hand[i][1:] == 'K' or hand[i][1:] == 'A')) :
				count = count + 1

		if (count is 5) :
			royal_flush = 'yes'

	return royal_flush


#check for a straight given a set of 5 or more cards
#returning the sequence of consecutive cards if community cards are < 3 in order to inform the bot about the possibility of a straight formation
#returns the highest straight possible if count of community cards >= 3
#returns False if no straight is possible
#handling seperately the case for the straight between [10 J Q K A] seperately

def straight(hand) :
    hand = list(set(hand))
    #print "given hand = ",hand
    spl_hand = sorted(hand,key = lambda x : card_rank[''.join((list(x))[1:])],reverse = True) #list declared in order to seperately handle [10 J Q K A]
    hand = sorted(hand,key = lambda x : card_rank2[''.join((list(x))[1:])])

    #print "spl_hand = " + str(spl_hand)
    #print "hand = " + str(hand)

    spl_straight = []
    hand_value = []
    hand_rank = []		#list taken in order to make comparison easier
    for card in hand:
        hand_value.append(card_rank2[''.join((list(card))[1:])])

    for card in spl_hand:
        hand_rank.append(card_rank[''.join((list(card))[1:])])

    #print "hand_value = " + str(hand_value)
    #print "hand_rank = " + str(hand_rank)

    def evaluateStraight(check_list):
        count = 0

        for i in range(0,len(check_list)-1) :
            if (check_list[i+1] - check_list[i] == 1) :
                count = count + 1
            else :
                break
        if (count == len(check_list)-1) :
            return True
        else :
            return False

    # Straight of Highest order handled here
    if(hand_rank[0:5] == [13, 12, 11, 10, 9]):
        spl_straight = (spl_hand[0:5])
        spl_straight.reverse()
        return ['10','J','Q','K','A']

    else :
        straight_list = []
        index = 0
        straight_flag = 0
        hand_value = list(set(hand_value))
        hand_value.sort()
        for i in range(0,(len(hand_value))%5 + 1):
            check_list = hand_value[i : 5 + i]
            #print "check_list = " + str(check_list)
            if (evaluateStraight(check_list) and (check_list > straight_list)) :
                straight_list = check_list
                index = i
                straight_flag = 1

        if (straight_flag) :
            return valuetoCard(straight_list,hand)
        else :
            return []

#check for straight flush in a hand of 5 or more cards
#returns False if not a straight flush else returns the hand sequence
#handled the case where i have 2 cards with same number say [CA,HA] on which makes a straight flush and other just a straight. Function returns the hand with straight flush
# Test case => ['CA', 'HA', 'CK', 'CQ', 'CJ', 'C10', 'H2']
def straightFlush(hand):
	straight_flush  = []
	if flush(hand) == 'null':
		if straight(hand) == []:
			return straight_flush

	suit_flush = flush(hand)
	for card in hand:
		if list(card)[0] == suit_flush:
			straight_flush.append(card)

	straight_flush = sorted(straight_flush,key = lambda x : card_rank[''.join((list(x))[1:])])
	return straight_flush





#function to check whether there is a full house in a given hand of cards returns empty or the full house sequence
def fullHouse(hand):
	temp = hand
	full_house = []
	three_card_val = threeOfAKind(temp)

	if (not three_card_val) :
		return full_house

	three_cards = cardScrapper(hand,three_card_val)

	for card in three_cards :
		temp.remove(card)

	one_pair_val = onePair(temp)

	if (not one_pair_val ):
		return full_house

	one_pair_list = cardScrapper(temp,one_pair_val)

	full_house = three_cards + one_pair_list
	return full_house

#hand = ['D4','SA','DA','H4','C4','DA']
# hand = ['D1','H2','S5','C4','H3','S6','D7']
#hand = ['DJ','SA','H10','H7','CK','D4','SQ']
# hand = ['DJ', 'H7', 'S2', 'SJ', 'S2', 'C7']
# hand = ['D10','HQ','H10','SJ','CQ','HJ','C9']

# print twoPair(hand)
# print fullHouse(hand)
# hand = ['D10','HQ','H10','S10','CQ','HJ','CQ']
hand  = ['DJ', 'C9', 'S10', 'H8', 'D6','S7','H9']
# hand = ['DK', 'C3', 'D7', 'HQ', 'HA']
#hand = ['D10','HQ','H10','S10','CQ','HJ','CQ']
# hand  = ['DA','D7','H6','S8','S9','C10','HK']
hand = ['DJ','C9','S10','H8','D6','S7','H9']
print straight(hand)
# print twoPair(hand),hand
# print straight(hand)
# print twoPair(hand)
# print straightFlush(hand)
# print threeOfAKind(hand)
#print fullHouse(hand)
#print straight(hand)

# hand = ['D10','HQ','H10','S10','CQ','HJ','C9']

#print threeOfAKind(hand)
# print fullHouse(hand)

from likelihood_prob import *
from handEvaluator import *
# from gameArena import *

u_wi = []

for p in prior_probabilities:
    u_wi.append(1/p)

strength = []


def check_best_hand(hand):
    if royalFlush(hand) != 'null':
        return 0
    elif straightFlush(hand) != []:
        return 1
    elif fourOfAKind(hand) != []:
        return 2
    elif fullHouse(hand) != []:
        return 3
    elif flush(hand) != []:
        return 4
    elif straight(hand) != []:
        return 5
    elif threeOfAKind(hand) != []:
        return 6
    elif twoPair(hand) != []:
        return 7
    elif onePair(hand) != []:
        return 8
    else:
        return 9

def calc_strength(hand) :
    prob_x = 0.0
    for i in range (0,10) :
        p = 1
        for j in range (0,len(hand)) :
            p *= likelihood[hand[j]][i]
        # print p
        p *= prior_probabilities[i]
        # print p
        prob_x += p
    #print "*** ",prob_x

    prob_wi_given_x = 0.0
    for i in range (0,10) :
        prob_wi_given_x = 1
        for j in range (0,len(hand)) :
            prob_wi_given_x *= likelihood[hand[j]][i]
        prob_wi_given_x *= prior_probabilities[i]
        prob_wi_given_x /= prob_x


        #print prob_wi_given_x

        strength.append(prob_wi_given_x)

    max_strength = max(strength)
    max_index = strength.index(max_strength)

    # print max_index
    #print max_strength,max_index

    max_hand_index = check_best_hand(hand)
    print "mhi = ",max_hand_index
    u_x = u_wi[max_hand_index]

    print "u_x = ",u_x

    prob_p_for_lower_max_index = 0.0


    for i in range (0,max_hand_index) :
        prob_wi_given_x = strength[i];
        prob_wi_given_x *= (u_wi[i])

        prob_p_for_lower_max_index += prob_wi_given_x


    print "pblm = ",prob_p_for_lower_max_index

    s_x = u_x + prob_p_for_lower_max_index

    return s_x


# hand = ['DA','D10','DJ','DQ','DK','C3','H4']
# hand = ['DA','HA','C3','DK','SA','C2','HJ']
# hand = ['D3','H3','C3','S4','H7','S8','H9']
# print calc_strength(hand)

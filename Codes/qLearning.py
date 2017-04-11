from handStrength import *
from knowledgeBase import *
from handEvaluator import *
import random


def actionValueGenerator(act):
    action_dict = {}
    for action in actions:
        if(action == act):
            action_dict[action] = reward
        else:
            action_dict[action] = 0

    print action_dict
    return action_dict


for i in range(4):

    print "Current round is ========>> %s" %(rounds[i])


    if(i == 1):
        if(hand_strength not in flop_base.keys()):
            act = random.choice(actions)
            print "Random Chosen Action Flop = ",act
            money = money - act[1]
            #perform action
            #updation of knowledge Base
            flop_base[hand_strength] = actionValueGenerator(act)

        else:
            action_dict = flop_base[hand_strength]
            max_value = max(action_dict.values())
            act = 0
            for action in action_dict:
                if(action_dict[action] == max_value):
                    act = action
                    break
            print "Flop Chosen Action = ",act
            money = money - act[1]


    if(i == 2):
        if(hand_strength not in river_base.keys()):
            act = random.choice(actions)
            print "Random Chosen Action River = ",act
            money = money - act[1]
            #perform action
            #updation of knowledge Base
            river_base[hand_strength] = actionValueGenerator(act)

        else:
            action_dict = river_base[hand_strength]
            max_value = max(action_dict.values())
            act = 0
            for action in action_dict:
                if(action_dict[action] == max_value):
                    act = action
                    break
            print "River Chosen Action = ",act
            money = money - act[1]


    if(i == 3):
        if(hand_strength not in turn_base.keys()):
            act = random.choice(actions)
            print "Random Chosen Action Turn = ",act
            money = money - act[1]
            #perform action
            #updation of knowledge Base
            turn_base[hand_strength] = actionValueGenerator(act)

        else:
            action_dict = turn_base[hand_strength]
            max_value = max(action_dict.values())
            act = 0
            for action in action_dict:
                if(action_dict[action] == max_value):
                    act = action
                    break
            print "Turn Chosen Action = ",act
            money = money - act[1]



    print "Current hand = " + str(hand) + '\n'

    #PRINTING  CURRENT KNOWLEDGE BASE

    print "Flop Knowledge Base = " +  str(flop_base) + '\n'

    print "River Knowledge Base = " + str(river_base) + '\n'

    print "Turn Knowledge Base = " + str(turn_base) + '\n'

    print "Current Money Left = " + str(money) + '\n'

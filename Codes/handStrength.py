from likelihood_prob import *
# from gameArena import *

strength = []

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
    print "*** ",prob_x

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

    #print max_strength,max_index

    u_x = 1/(prior_probabilities[max_index] * 1.0)

    #print u_x

    prob_p_for_lower_max_index = 0.0

    for i in range (0,max_index) :
        prob_wi_given_x = strength[i];
        prob_wi_given_x *= (1/(prior_probabilities[i]))

        prob_p_for_lower_max_index += prob_wi_given_x

    #print prob_p_for_lower_max_index

    s_x = u_x + prob_p_for_lower_max_index

    return s_x

hand = ['DA','DK','DJ','DQ','D10','C10','HK']
print "**",calc_strength(hand)

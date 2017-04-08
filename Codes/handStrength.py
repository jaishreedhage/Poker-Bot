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
        # print "*** ",prob_x

    prob_x_given_wi = 0.0
    for i in range (0,10) :
        prob_x_given_wi = 1
        for j in range (0,len(hand)) :
            prob_x_given_wi *= likelihood[hand[j]][i]
        prob_x_given_wi *= prior_probabilities[i]
        prob_x_given_wi /= prob_x

        print prob_x_given_wi

        strength.append(prob_x_given_wi)

    max_strength = max(strength)
    max_index = strength.index(max_strength)

    print max_strength,max_index

    u_x = 1/(prior_probabilities[max_index] * 1.0)

    print u_x

    prob_p_for_lower_max_index = 0.0

    for i in range (0,max_index) :
        prob_x_given_wi = 1
        for j in range (0,len(hand)) :
            prob_x_given_wi *= likelihood[hand[j]][i]
        prob_x_given_wi *= prior_probabilities[i]
        prob_x_given_wi /= prob_x
        prob_x_given_wi *= 1/(prior_probabilities[i])

        prob_p_for_lower_max_index += prob_x_given_wi

    print prob_p_for_lower_max_index

    s_x = u_x + prob_p_for_lower_max_index

    return s_x

hand = ['DA','DK','DJ','DQ','D10','D10','S10']
print "**",calc_strength(hand)

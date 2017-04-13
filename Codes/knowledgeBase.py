import pandas as pd

file_extn = ".csv"


headers = ['Fold','Check','Call','Bet-1','Bet-2','Bet-5','Bet-7']
index = [0,200,500,2000,10000]

knowledge_update = {"flop_base" : [0,0],"river_base" : [0,0],"turn_base" : [0,0]}

def read_file(csv_file,hand_strength) :

    csv_file += file_extn

    idx = 4

    for i in range (0,4) :
        if hand_strength>=index[i] and hand_strength<index[i+1] :
            idx = i
            break

    df = pd.read_csv(csv_file)
    choice = []
    for i in range (0,7) :
        choice.append(df[ headers[i] ][idx])

    max_choice = max(choice)
    max_choice_idx = choice.index(max_choice)


    return max_choice,max_choice_idx,idx            #returning value,column and row

def write_file(csv_file,reward) :

    csv_key = csv_file
    csv_file += file_extn

    df = pd.read_csv(csv_file)
    idx = knowledge_update[csv_key][1]
    col = headers[knowledge_update[csv_key][0]]

    df.set_value(idx,col,reward)
    df.to_csv(csv_file,index=False)

#
# read_file(csv_flop,500)
# write_file(csv_flop,1,2)
# read_file(csv_flop,500)

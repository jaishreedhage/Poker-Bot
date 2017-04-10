import pandas as pd

file_extn = ".csv"

headers = ['Fold','Check','Call','Bet-1','Bet-2','Bet-5','Bet-7']
index = [0,200,500,2000,10000]

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

def write_file(csv_file,idx,head) :

    csv_file += file_extn

    df = pd.read_csv(csv_file)
    df.set_value(idx, headers[head],240)
    df.to_csv(csv_file, index=False)

#
# read_file(csv_flop,500)
# write_file(csv_flop,1,2)
# read_file(csv_flop,500)

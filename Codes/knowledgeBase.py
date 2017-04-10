# flop_base = {}
#
# river_base = {}
#
# turn_base = {}
#
# actions = [('Fold',0),('Check',0),('Call',0),('Bet',1),('Bet',2),('Bet',5),('Bet',7)]

import csv

file_extn = ".csv"
csv_flop = "flop_base"
csv_turn = 'turn_base'
csv_river = 'river_base'

def read_file(csv_file) :

    with open(csv_file) as obj:
        reader = csv.DictReader(obj, delimiter=',')
        for line in reader:
            print line
            print(line["Fold"])
            print(line["Hand_Strength"])

def write_file(csv_file) :

    reader = csv.DictReader(csv_file, delimiter=',')
    for line in reader:
        print line
        print(line["Fold"])
        print(line["Hand_Strength"])

read_file(csv_flop+file_extn)

from HandEvaluator import *
from pokerUI import *
import random
import sys



#global variables
image_dir = "Images/"
png = ".png"
game = 1
round = ["Preflop","Flop","Turn","River"]
buy_in = 200
pot = 0



#setup UI
app = QtGui.QApplication(sys.argv)
MainWindow = QtGui.QMainWindow()
ui = Ui_MainWindow(MainWindow)
ui.setupUi(MainWindow)

ui.NameOfRound(MainWindow,round[0])
ui.GameNumber(MainWindow,str(game))

ui.cc1(MainWindow,image_dir+"facedown"+png)
ui.cc2(MainWindow,image_dir+"facedown"+png)
ui.cc3(MainWindow,image_dir+"facedown"+png)
ui.cc4(MainWindow,image_dir+"facedown"+png)
ui.cc5(MainWindow,image_dir+"facedown"+png)
ui.p1c1(MainWindow,image_dir+"facedown"+png)
ui.p1c2(MainWindow,image_dir+"facedown"+png)
ui.p2c1(MainWindow,image_dir+"facedown"+png)
ui.p2c2(MainWindow,image_dir+"facedown"+png)
ui.bc1(MainWindow,image_dir+"facedown"+png)
ui.bc2(MainWindow,image_dir+"facedown"+png)

ui.p1OptionsHideShow(MainWindow,True);
ui.p2OptionsHideShow(MainWindow,False);

ui.p1Money(MainWindow,str(buy_in))
ui.p2Money(MainWindow,str(buy_in))
ui.BotMoney(MainWindow,str(buy_in))

ui.PotMoney(MainWindow,str(pot))

MainWindow.show()
sys.exit(app.exec_())



deck = cards

#shuffle cards
def shuffle () :
	random.shuffle(deck)


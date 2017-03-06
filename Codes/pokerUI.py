# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Jaishree\Documents\p1\mainwindow.ui'
#
# Created: Mon Feb 27 00:01:05 2017
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QThread

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class MyThread(QThread):

    def __init__(self):
        QThread.__init__(self)

    def __delay__(self):
        self.wait()

    def run(self):
        i = 0
        while(1):
            i = i+1
            print "i = " + str(i)

class Ui_MainWindow(object):

	#function to stop game
	def StopGame(self,Mainwindow):
        print "**"
		return 2

	#function to change the name of round
	def NameOfRound(self,Mainwindow,round):
		self.nameOfRound.setText(round)

	#function to change game number
	def GameNumber(self,Mainwindow,number) :
		self.gameNumber.setText(number)

	#function to change cards
	def cc1(self,Mainwindow,value) :
		self.communityCard1.setPixmap(QtGui.QPixmap(_fromUtf8(value)))

	def cc2(self,Mainwindow,value) :
		self.communityCard2.setPixmap(QtGui.QPixmap(_fromUtf8(value)))

	def cc3(self,Mainwindow,value) :
		self.communityCard3.setPixmap(QtGui.QPixmap(_fromUtf8(value)))

	def cc4(self,Mainwindow,value) :
		self.communityCard4.setPixmap(QtGui.QPixmap(_fromUtf8(value)))

	def cc5(self,Mainwindow,value) :
		self.communityCard5.setPixmap(QtGui.QPixmap(_fromUtf8(value)))

	def p1c1(self,Mainwindow,value) :
		self.player1Card1.setPixmap(QtGui.QPixmap(_fromUtf8(value)))

	def p1c2(self,Mainwindow,value) :
		self.player1Card2.setPixmap(QtGui.QPixmap(_fromUtf8(value)))

	def p2c1(self,Mainwindow,value) :
		self.player2Card1.setPixmap(QtGui.QPixmap(_fromUtf8(value)))

	def p2c2(self,Mainwindow,value) :
		self.player2Card2.setPixmap(QtGui.QPixmap(_fromUtf8(value)))

	def bc1(self,Mainwindow,value) :
		self.botCard1.setPixmap(QtGui.QPixmap(_fromUtf8(value)))

	def bc2(self,Mainwindow,value) :
		self.botCard2.setPixmap(QtGui.QPixmap(_fromUtf8(value)))

	#function to hide or show options
	def p1OptionsHideShow(self,MainWindow,toggle) :
		self.player1Opt1.setVisible(toggle)
		self.player1Opt2.setVisible(toggle)
		self.player1Opt2Ok.setVisible(toggle)
		self.player1Opt3.setVisible(toggle)
		self.dollar1.setVisible(toggle)
		self.player1bet.setVisible(toggle)

	def p2OptionsHideShow(self,MainWindow,toggle) :
		self.player2Opt1.setVisible(toggle)
		self.player2Opt2.setVisible(toggle)
		self.player2Opt2Ok.setVisible(toggle)
		self.player2Opt3.setVisible(toggle)
		self.dollar2.setVisible(toggle)
		self.player2bet.setVisible(toggle)

	#set call/check for player 1 and 2
	def setP1Opt1(self,Mainwindow,callCheck) :
		player1Opt1.setText(callCheck)

	def setP2Opt1(self,Mainwindow,callCheck) :
		player2Opt1.setText(callCheck)

	#set bet/raise for player 1 and 2
	def setP1Opt2(self,Mainwindow,betRaise) :
		player1Opt2.setText(betRaise)
		player1Opt2Ok.setText(betRaise)

	def setP2Opt2(self,Mainwindow,betRaise) :
		player2Opt2.setText(betRaise)
		player1Opt2Ok.setText(betRaise)


	#functions to update money left with each player
	def p1Money(self,Mainwindow,money):
		self.player1Money.setText("$" + money)

	def p2Money(self,Mainwindow,money):
		self.player2Money.setText("$" + money)

	def BotMoney(self,Mainwindow,money):
		self.botMoney.setText("$" + money)

	#function to update pot money
	def PotMoney(self,Mainwindow,money) :
		self.potMoney.setText("$" + money)

	#function to display pot's decision
	def BotPlays(self,Mainwindow,decision) :
		self.botPlays.setText("Poker bot" + decision)

	#function to get the raise/bet money from players
	def p1GetRaise(self,MainWindow) :
		value = self.player1bet.text()
		print value

	def p2GetRaise(self,MainWindow) :
		value = self.player2bet.text()
		print value

	#functions to handle what happens when call/check button is pressed for each player
	def p1CallCheck(self,Mainwindow) :
		pass

	def p2CallCheck(self,Mainwindow) :
		pass

	#function to handle what happens when fold button is pressed for each player
	def p1Fold(self,Mainwindow) :
		pass

	def p2Fold(self,Mainwindow) :
		pass





	#initialise the UI --- constant UI components
	def __init__(self, MainWindow):


		#Mainwindow
		MainWindow.setObjectName(_fromUtf8("MainWindow"))
		MainWindow.resize(930, 722)


		#central widget
		self.centralWidget = QtGui.QWidget(MainWindow)
		self.centralWidget.setObjectName(_fromUtf8("centralWidget"))

		MainWindow.setWindowTitle("Texas Hold'em Poker")
		MainWindow.setWindowIcon(QtGui.QIcon("Images/logo.jpg"))
		MainWindow.setCentralWidget(self.centralWidget)

		#community cards name
		self.CommunityCards = QtGui.QLabel(self.centralWidget)
		self.CommunityCards.setGeometry(QtCore.QRect(250, 30, 181, 21))
		font = QtGui.QFont()
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.CommunityCards.setFont(font)
		self.CommunityCards.setObjectName(_fromUtf8("CommunityCards"))
		self.CommunityCards.setText("Community Cards")

		#Round title
		self.Round = QtGui.QLabel(self.centralWidget)
		self.Round.setGeometry(QtCore.QRect(760, 40, 71, 16))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.Round.setFont(font)
		self.Round.setObjectName(_fromUtf8("Round"))
		self.Round.setText("Round :")

		#Game number
		self.Round_2 = QtGui.QLabel(self.centralWidget)
		self.Round_2.setGeometry(QtCore.QRect(730, 10, 101, 20))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.Round_2.setFont(font)
		self.Round_2.setObjectName(_fromUtf8("Round_2"))
		self.Round_2.setText("Game No. :")

		#player1 title
		self.Player1 = QtGui.QLabel(self.centralWidget)
		self.Player1.setGeometry(QtCore.QRect(130, 320, 51, 16))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.Player1.setFont(font)
		self.Player1.setObjectName(_fromUtf8("Player1"))
		self.Player1.setText("Player1")


		#player2 title
		self.Player2 = QtGui.QLabel(self.centralWidget)
		self.Player2.setGeometry(QtCore.QRect(420, 320, 51, 16))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.Player2.setFont(font)
		self.Player2.setObjectName(_fromUtf8("Player2"))
		self.Player2.setText("Player2")


		#poker bot title
		self.PokerBot = QtGui.QLabel(self.centralWidget)
		self.PokerBot.setGeometry(QtCore.QRect(740, 320, 71, 16))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.PokerBot.setFont(font)
		self.PokerBot.setObjectName(_fromUtf8("PokerBot"))
		self.PokerBot.setText("Poker Bot")


		#Pot title
		self.PotValue = QtGui.QLabel(self.centralWidget)
		self.PotValue.setGeometry(QtCore.QRect(760, 100, 47, 13))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.PotValue.setFont(font)
		self.PotValue.setObjectName(_fromUtf8("PotValue"))
		self.PotValue.setText("POT")

		#stop game button
		self.stopGame = QtGui.QPushButton(self.centralWidget)
		self.stopGame.setGeometry(QtCore.QRect(814, 680, 81, 23))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.stopGame.setFont(font)
		self.stopGame.setObjectName(_fromUtf8("stopGame"))
		self.stopGame.setText("STOP GAME")
		self.stopGame.clicked.connect(self.StopGame)

        thread = MyThread()
        thread.start()




	#initialise the non-constant UI components
	def setupUi(self,Mainwindow) :

		#name of current round
		self.nameOfRound = QtGui.QLabel(self.centralWidget)
		self.nameOfRound.setGeometry(QtCore.QRect(840, 30, 51, 31))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.nameOfRound.setFont(font)
		self.nameOfRound.setObjectName(_fromUtf8("nameOfRound"))

		#game number
		self.gameNumber = QtGui.QLabel(self.centralWidget)
		self.gameNumber.setGeometry(QtCore.QRect(840, 10, 51, 21))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.gameNumber.setFont(font)
		self.gameNumber.setObjectName(_fromUtf8("numberOfRound"))

		#community card 1
		self.communityCard1 = QtGui.QLabel(self.centralWidget)
		self.communityCard1.setGeometry(QtCore.QRect(40, 80, 101, 171))
		self.communityCard1.setText(_fromUtf8(""))

		# self.communityCard1.setPixmap(QtGui.QPixmap(_fromUtf8("Images/C2.png")))
		self.communityCard1.setObjectName(_fromUtf8("communityCard1"))
		self.communityCard1.setScaledContents(True);

		#community card 2
		self.communityCard2 = QtGui.QLabel(self.centralWidget)
		self.communityCard2.setGeometry(QtCore.QRect(160, 80, 101, 171))
		self.communityCard2.setText(_fromUtf8(""))
		self.communityCard2.setPixmap(QtGui.QPixmap(_fromUtf8("Images/C2.png")))
		self.communityCard2.setObjectName(_fromUtf8("communityCard2"))
		self.communityCard2.setScaledContents(True);

		#community card 3
		self.communityCard3 = QtGui.QLabel(self.centralWidget)
		self.communityCard3.setGeometry(QtCore.QRect(280, 80, 101, 171))
		self.communityCard3.setText(_fromUtf8(""))
		self.communityCard3.setPixmap(QtGui.QPixmap(_fromUtf8("Images/C2.png")))
		self.communityCard3.setObjectName(_fromUtf8("communityCard3"))
		self.communityCard3.setScaledContents(True);

		#community card 4
		self.communityCard4 = QtGui.QLabel(self.centralWidget)
		self.communityCard4.setGeometry(QtCore.QRect(400, 80, 101, 171))
		self.communityCard4.setText(_fromUtf8(""))
		self.communityCard4.setPixmap(QtGui.QPixmap(_fromUtf8("Images/C2.png")))
		self.communityCard4.setObjectName(_fromUtf8("communityCard4"))
		self.communityCard4.setScaledContents(True);

		#community card 5
		self.communityCard5 = QtGui.QLabel(self.centralWidget)
		self.communityCard5.setGeometry(QtCore.QRect(520, 80, 101, 171))
		self.communityCard5.setText(_fromUtf8(""))
		self.communityCard5.setPixmap(QtGui.QPixmap(_fromUtf8("Images/C2.png")))
		self.communityCard5.setObjectName(_fromUtf8("communityCard5"))
		self.communityCard5.setScaledContents(True);

		#player 1 card 1
		self.player1Card1 = QtGui.QLabel(self.centralWidget)
		self.player1Card1.setGeometry(QtCore.QRect(30, 350, 111, 171))
		self.player1Card1.setText(_fromUtf8(""))
		self.player1Card1.setPixmap(QtGui.QPixmap(_fromUtf8("Images/C2.png")))
		self.player1Card1.setObjectName(_fromUtf8("player1Card1"))
		self.player1Card1.setScaledContents(True);

		#player 1 card 2
		self.player1Card2 = QtGui.QLabel(self.centralWidget)
		self.player1Card2.setGeometry(QtCore.QRect(160, 350, 111, 171))
		self.player1Card2.setText(_fromUtf8(""))
		self.player1Card2.setPixmap(QtGui.QPixmap(_fromUtf8("Images/C2.png")))
		self.player1Card2.setObjectName(_fromUtf8("player1Card2"))
		self.player1Card2.setScaledContents(True);

		#player 2 card 1
		self.player2Card1 = QtGui.QLabel(self.centralWidget)
		self.player2Card1.setGeometry(QtCore.QRect(320, 350, 111, 171))
		self.player2Card1.setText(_fromUtf8(""))
		self.player2Card1.setPixmap(QtGui.QPixmap(_fromUtf8("Images/C2.png")))
		self.player2Card1.setObjectName(_fromUtf8("player2Card1"))
		self.player2Card1.setScaledContents(True);

		#player 2 card 2
		self.player2Card2 = QtGui.QLabel(self.centralWidget)
		self.player2Card2.setGeometry(QtCore.QRect(450, 350, 111, 171))
		self.player2Card2.setText(_fromUtf8(""))
		self.player2Card2.setPixmap(QtGui.QPixmap(_fromUtf8("Images/C2.png")))
		self.player2Card2.setObjectName(_fromUtf8("player2Card2"))
		self.player2Card2.setScaledContents(True);

		#bot card 1
		self.botCard1 = QtGui.QLabel(self.centralWidget)
		self.botCard1.setGeometry(QtCore.QRect(640, 350, 111, 171))
		self.botCard1.setText(_fromUtf8(""))
		self.botCard1.setPixmap(QtGui.QPixmap(_fromUtf8("Images/C2.png")))
		self.botCard1.setObjectName(_fromUtf8("botCard1"))
		self.botCard1.setScaledContents(True);

		#bot card 2
		self.botCard2 = QtGui.QLabel(self.centralWidget)
		self.botCard2.setGeometry(QtCore.QRect(770, 350, 111, 171))
		self.botCard2.setText(_fromUtf8(""))
		self.botCard2.setPixmap(QtGui.QPixmap(_fromUtf8("Images/C2.png")))
		self.botCard2.setObjectName(_fromUtf8("botCard2"))
		self.botCard2.setScaledContents(True);



		#player 1 option 1 -> call or check
		self.player1Opt1 = QtGui.QPushButton(self.centralWidget)
		self.player1Opt1.setGeometry(QtCore.QRect(50, 580, 75, 23))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.player1Opt1.setFont(font)
		self.player1Opt1.setText(_fromUtf8(""))
		self.player1Opt1.setObjectName(_fromUtf8("player1Opt1"))
		self.player1Opt1.clicked.connect(self.p1CallCheck)

		#label to show option for bet or raise for player 1
		self.player1Opt2 = QtGui.QLabel(self.centralWidget)
		self.player1Opt2.setGeometry(QtCore.QRect(20, 620, 71, 20))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.player1Opt2.setFont(font)
		self.player1Opt2.setObjectName(_fromUtf8("player1Opt2"))

		#player 1 dolloar symbol
		self.dollar1 = QtGui.QLabel(self.centralWidget)
		self.dollar1.setGeometry(QtCore.QRect(100, 620, 16, 16))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.dollar1.setFont(font)
		self.dollar1.setText("$")
		self.dollar1.setObjectName(_fromUtf8("dollar1"))

		#player 1 money he enters for bet/raise
		self.player1bet = QtGui.QLineEdit(self.centralWidget)
		self.player1bet.setGeometry(QtCore.QRect(120, 620, 71, 21))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.player1bet.setFont(font)
		self.player1bet.setObjectName(_fromUtf8("player1bet"))

		#player 1 button to agree on raise/bet
		self.player1Opt2Ok = QtGui.QPushButton(self.centralWidget)
		self.player1Opt2Ok.setGeometry(QtCore.QRect(210, 620, 51, 23))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.player1Opt2Ok.setFont(font)
		self.player1Opt2Ok.setText(_fromUtf8(""))
		self.player1Opt2Ok.setObjectName(_fromUtf8("player1Opt2Ok"))
		self.player1Opt2Ok.clicked.connect(self.p1GetRaise)

		#player 1 option 3 -> fold
		self.player1Opt3 = QtGui.QPushButton(self.centralWidget)
		self.player1Opt3.setGeometry(QtCore.QRect(160, 580, 75, 23))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.player1Opt3.setFont(font)
		self.player1Opt3.setText(_fromUtf8(""))
		self.player1Opt3.setObjectName(_fromUtf8("player1Opt3"))
		self.player1Opt3.setText("Fold")
		self.player1Opt3.clicked.connect(self.p1Fold)

		#player 1 money
		self.player1Money = QtGui.QLabel(self.centralWidget)
		self.player1Money.setGeometry(QtCore.QRect(86, 540, 131, 20))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.player1Money.setFont(font)
		self.player1Money.setAlignment(QtCore.Qt.AlignCenter)
		self.player1Money.setWordWrap(False)
		self.player1Money.setObjectName(_fromUtf8("player1Money"))




		#player 2 option 1 -> call or check
		self.player2Opt1 = QtGui.QPushButton(self.centralWidget)
		self.player2Opt1.setGeometry(QtCore.QRect(350, 580, 75, 23))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.player2Opt1.setFont(font)
		self.player2Opt1.setText(_fromUtf8(""))
		self.player2Opt1.setObjectName(_fromUtf8("player2Opt1"))
		self.player2Opt1.clicked.connect(self.p2CallCheck)

		#label to show option for bet or raise for player 2
		self.player2Opt2 = QtGui.QLabel(self.centralWidget)
		self.player2Opt2.setGeometry(QtCore.QRect(310, 620, 71, 20))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.player2Opt2.setFont(font)
		self.player2Opt2.setObjectName(_fromUtf8("player2Opt2"))

		#player 1 dolloar symbol
		self.dollar2 = QtGui.QLabel(self.centralWidget)
		self.dollar2.setGeometry(QtCore.QRect(400, 620, 16, 16))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.dollar2.setFont(font)
		self.dollar2.setText("$")
		self.dollar2.setObjectName(_fromUtf8("dollar2"))

		#player 2 money he enters for bet/raise
		self.player2bet = QtGui.QLineEdit(self.centralWidget)
		self.player2bet.setGeometry(QtCore.QRect(430, 620, 71, 20))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.player2bet.setFont(font)
		self.player2bet.setObjectName(_fromUtf8("player2bet"))

		#player 2 button to agree on raise/bet
		self.player2Opt2Ok = QtGui.QPushButton(self.centralWidget)
		self.player2Opt2Ok.setGeometry(QtCore.QRect(510, 620, 51, 23))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.player2Opt2Ok.setFont(font)
		self.player2Opt2Ok.setText(_fromUtf8(""))
		self.player2Opt2Ok.setCheckable(False)
		self.player2Opt2Ok.setObjectName(_fromUtf8("player2Opt2Ok"))
		self.player2Opt2Ok.clicked.connect(self.p2GetRaise)

		#player 2 option 3 -> fold
		self.player2Opt3 = QtGui.QPushButton(self.centralWidget)
		self.player2Opt3.setGeometry(QtCore.QRect(460, 580, 75, 23))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.player2Opt3.setFont(font)
		self.player2Opt3.setText(_fromUtf8(""))
		self.player2Opt3.setObjectName(_fromUtf8("player2Opt3"))
		self.player2Opt3.setText("Fold")
		self.player2Opt3.clicked.connect(self.p2Fold)

		#player 2 money
		self.player2Money = QtGui.QLabel(self.centralWidget)
		self.player2Money.setGeometry(QtCore.QRect(376, 540, 141, 20))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.player2Money.setFont(font)
		self.player2Money.setAlignment(QtCore.Qt.AlignCenter)
		self.player2Money.setObjectName(_fromUtf8("player2Money"))




		#label to show what bot has done
		self.botPlays = QtGui.QLabel(self.centralWidget)
		self.botPlays.setGeometry(QtCore.QRect(646, 570, 241, 61))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.botPlays.setFont(font)
		self.botPlays.setWordWrap(True)
		self.botPlays.setObjectName(_fromUtf8("Botplays"))

		#bot money
		self.botMoney = QtGui.QLabel(self.centralWidget)
		self.botMoney.setGeometry(QtCore.QRect(696, 540, 131, 20))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.botMoney.setFont(font)
		self.botMoney.setAlignment(QtCore.Qt.AlignCenter)
		self.botMoney.setObjectName(_fromUtf8("player3Money"))


		#money in POT
		self.potMoney = QtGui.QPushButton(self.centralWidget)
		self.potMoney.setEnabled(False)
		self.potMoney.setGeometry(QtCore.QRect(720, 133, 111, 111))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.potMoney.setFont(font)
		self.potMoney.setStyleSheet(_fromUtf8(" background-color: rgb(255, 255, 255);\n"
		" border-style: solid;\n"
		" border-width:2px;\n"
		" border-radius:50px;\n"
		" border-color: black;\n"
		" max-width:110px;\n"
		" max-height:110px;\n"
		" min-width:100px;\n"
		" min-height:100px;\n"
		"color : rgb(170, 0, 0)\n"
		""))
		self.potMoney.setObjectName(_fromUtf8("potMoney"))

		# QtCore.QMetaObject.connectSlotsByName(MainWindow)       ----- wtf is this.??

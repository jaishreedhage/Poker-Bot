# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Jaishree\Documents\p1\mainwindow.ui'
#
# Created: Mon Feb 27 00:01:05 2017
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(930, 722)

        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.CommunityCards = QtGui.QLabel(self.centralWidget)
        self.CommunityCards.setGeometry(QtCore.QRect(250, 30, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.CommunityCards.setFont(font)
        self.CommunityCards.setObjectName(_fromUtf8("CommunityCards"))


        self.Round = QtGui.QLabel(self.centralWidget)
        self.Round.setGeometry(QtCore.QRect(760, 40, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Round.setFont(font)
        self.Round.setObjectName(_fromUtf8("Round"))


        self.nameOfRound = QtGui.QLabel(self.centralWidget)
        self.nameOfRound.setGeometry(QtCore.QRect(840, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nameOfRound.setFont(font)
        self.nameOfRound.setObjectName(_fromUtf8("nameOfRound"))


        self.Player1 = QtGui.QLabel(self.centralWidget)
        self.Player1.setGeometry(QtCore.QRect(130, 320, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Player1.setFont(font)
        self.Player1.setObjectName(_fromUtf8("Player1"))


        self.Player2 = QtGui.QLabel(self.centralWidget)
        self.Player2.setGeometry(QtCore.QRect(420, 320, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Player2.setFont(font)
        self.Player2.setObjectName(_fromUtf8("Player2"))


        self.PokerBot = QtGui.QLabel(self.centralWidget)
        self.PokerBot.setGeometry(QtCore.QRect(740, 320, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.PokerBot.setFont(font)
        self.PokerBot.setObjectName(_fromUtf8("PokerBot"))


        self.stopGame = QtGui.QPushButton(self.centralWidget)
        self.stopGame.setGeometry(QtCore.QRect(814, 680, 81, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.stopGame.setFont(font)
        self.stopGame.setObjectName(_fromUtf8("stopGame"))


        self.player1Card1 = QtGui.QLabel(self.centralWidget)
        self.player1Card1.setGeometry(QtCore.QRect(30, 350, 111, 171))
        self.player1Card1.setText(_fromUtf8(""))
        self.player1Card1.setPixmap(QtGui.QPixmap(_fromUtf8("Images/C2.png")))
        self.player1Card1.setObjectName(_fromUtf8("player1Card1"))
        self.player1Card1.setScaledContents(True);


        self.communityCard3 = QtGui.QLabel(self.centralWidget)
        self.communityCard3.setGeometry(QtCore.QRect(280, 80, 101, 171))
        self.communityCard3.setText(_fromUtf8(""))
        self.communityCard3.setPixmap(QtGui.QPixmap(_fromUtf8("Images/C2.png")))
        self.communityCard3.setObjectName(_fromUtf8("communityCard3"))
        self.communityCard3.setScaledContents(True);


        self.communityCard1 = QtGui.QLabel(self.centralWidget)
        self.communityCard1.setGeometry(QtCore.QRect(40, 80, 101, 171))
        self.communityCard1.setText(_fromUtf8(""))
        self.communityCard1.setPixmap(QtGui.QPixmap(_fromUtf8("Images/C2.png")))
        self.communityCard1.setObjectName(_fromUtf8("communityCard1"))
        self.communityCard1.setScaledContents(True);


        self.communityCard2 = QtGui.QLabel(self.centralWidget)
        self.communityCard2.setGeometry(QtCore.QRect(160, 80, 101, 171))
        self.communityCard2.setText(_fromUtf8(""))
        self.communityCard2.setPixmap(QtGui.QPixmap(_fromUtf8("Images/C2.png")))
        self.communityCard2.setObjectName(_fromUtf8("communityCard2"))
        self.communityCard2.setScaledContents(True);


        self.communityCard4 = QtGui.QLabel(self.centralWidget)
        self.communityCard4.setGeometry(QtCore.QRect(400, 80, 101, 171))
        self.communityCard4.setText(_fromUtf8(""))
        self.communityCard4.setPixmap(QtGui.QPixmap(_fromUtf8("Images/C2.png")))
        self.communityCard4.setObjectName(_fromUtf8("communityCard4"))
        self.communityCard4.setScaledContents(True);


        self.communityCard5 = QtGui.QLabel(self.centralWidget)
        self.communityCard5.setGeometry(QtCore.QRect(520, 80, 101, 171))
        self.communityCard5.setText(_fromUtf8(""))
        self.communityCard5.setPixmap(QtGui.QPixmap(_fromUtf8("Images/C2.png")))
        self.communityCard5.setObjectName(_fromUtf8("communityCard5"))
        self.communityCard5.setScaledContents(True);


        self.botCard2 = QtGui.QLabel(self.centralWidget)
        self.botCard2.setGeometry(QtCore.QRect(770, 350, 111, 171))
        self.botCard2.setText(_fromUtf8(""))
        self.botCard2.setPixmap(QtGui.QPixmap(_fromUtf8("Images/C2.png")))
        self.botCard2.setObjectName(_fromUtf8("botCard2"))
        self.botCard2.setScaledContents(True);


        self.player2Card2 = QtGui.QLabel(self.centralWidget)
        self.player2Card2.setGeometry(QtCore.QRect(450, 350, 111, 171))
        self.player2Card2.setText(_fromUtf8(""))
        self.player2Card2.setPixmap(QtGui.QPixmap(_fromUtf8("Images/C2.png")))
        self.player2Card2.setObjectName(_fromUtf8("player2Card2"))
        self.player2Card2.setScaledContents(True);


        self.botCard1 = QtGui.QLabel(self.centralWidget)
        self.botCard1.setGeometry(QtCore.QRect(640, 350, 111, 171))
        self.botCard1.setText(_fromUtf8(""))
        self.botCard1.setPixmap(QtGui.QPixmap(_fromUtf8("Images/C2.png")))
        self.botCard1.setObjectName(_fromUtf8("botCard1"))
        self.botCard1.setScaledContents(True);


        self.player2Card1 = QtGui.QLabel(self.centralWidget)
        self.player2Card1.setGeometry(QtCore.QRect(320, 350, 111, 171))
        self.player2Card1.setText(_fromUtf8(""))
        self.player2Card1.setPixmap(QtGui.QPixmap(_fromUtf8("Images/C2.png")))
        self.player2Card1.setObjectName(_fromUtf8("player2Card1"))
        self.player2Card1.setScaledContents(True);


        self.player1Card2 = QtGui.QLabel(self.centralWidget)
        self.player1Card2.setGeometry(QtCore.QRect(160, 350, 111, 171))
        self.player1Card2.setText(_fromUtf8(""))
        self.player1Card2.setPixmap(QtGui.QPixmap(_fromUtf8("Images/C2.png")))
        self.player1Card2.setObjectName(_fromUtf8("player1Card2"))
        self.player1Card2.setScaledContents(True);


        self.PotValue = QtGui.QLabel(self.centralWidget)
        self.PotValue.setGeometry(QtCore.QRect(760, 100, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.PotValue.setFont(font)
        self.PotValue.setObjectName(_fromUtf8("PotValue"))



        self.player1Opt1 = QtGui.QPushButton(self.centralWidget)
        self.player1Opt1.setGeometry(QtCore.QRect(50, 580, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.player1Opt1.setFont(font)
        self.player1Opt1.setText(_fromUtf8(""))
        self.player1Opt1.setObjectName(_fromUtf8("player1Opt1"))


        self.player1Opt2Ok = QtGui.QPushButton(self.centralWidget)
        self.player1Opt2Ok.setGeometry(QtCore.QRect(210, 620, 51, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.player1Opt2Ok.setFont(font)
        self.player1Opt2Ok.setText(_fromUtf8(""))
        self.player1Opt2Ok.setObjectName(_fromUtf8("player1Opt2Ok"))



        self.player1Opt2Ok.clicked.connect(self.btnclick)




        self.player1Opt3 = QtGui.QPushButton(self.centralWidget)
        self.player1Opt3.setGeometry(QtCore.QRect(160, 580, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.player1Opt3.setFont(font)
        self.player1Opt3.setText(_fromUtf8(""))
        self.player1Opt3.setObjectName(_fromUtf8("player1Opt3"))


        self.player2Opt1 = QtGui.QPushButton(self.centralWidget)
        self.player2Opt1.setGeometry(QtCore.QRect(350, 580, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.player2Opt1.setFont(font)
        self.player2Opt1.setText(_fromUtf8(""))
        self.player2Opt1.setObjectName(_fromUtf8("player2Opt1"))


        self.player2Opt2Ok = QtGui.QPushButton(self.centralWidget)
        self.player2Opt2Ok.setEnabled(False)
        self.player2Opt2Ok.setGeometry(QtCore.QRect(510, 620, 51, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.player2Opt2Ok.setFont(font)
        self.player2Opt2Ok.setText(_fromUtf8(""))
        self.player2Opt2Ok.setCheckable(False)
        self.player2Opt2Ok.setObjectName(_fromUtf8("player2Opt2Ok"))


        self.player2Opt3 = QtGui.QPushButton(self.centralWidget)
        self.player2Opt3.setGeometry(QtCore.QRect(460, 580, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.player2Opt3.setFont(font)
        self.player2Opt3.setText(_fromUtf8(""))
        self.player2Opt3.setObjectName(_fromUtf8("player2Opt3"))


        self.Botplays = QtGui.QLabel(self.centralWidget)
        self.Botplays.setGeometry(QtCore.QRect(646, 570, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Botplays.setFont(font)
        self.Botplays.setWordWrap(True)
        self.Botplays.setObjectName(_fromUtf8("Botplays"))


        self.player1Opt2 = QtGui.QLabel(self.centralWidget)
        self.player1Opt2.setGeometry(QtCore.QRect(20, 620, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.player1Opt2.setFont(font)
        self.player1Opt2.setObjectName(_fromUtf8("player1Opt2"))


        self.player1bet = QtGui.QLineEdit(self.centralWidget)
        self.player1bet.setGeometry(QtCore.QRect(120, 620, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.player1bet.setFont(font)
        self.player1bet.setObjectName(_fromUtf8("player1bet"))


        self.dollar1 = QtGui.QLabel(self.centralWidget)
        self.dollar1.setGeometry(QtCore.QRect(100, 620, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.dollar1.setFont(font)
        self.dollar1.setObjectName(_fromUtf8("dollar1"))


        self.player2Opt2 = QtGui.QLabel(self.centralWidget)
        self.player2Opt2.setGeometry(QtCore.QRect(310, 620, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.player2Opt2.setFont(font)
        self.player2Opt2.setObjectName(_fromUtf8("player2Opt2"))


        self.player2bet = QtGui.QLineEdit(self.centralWidget)
        self.player2bet.setGeometry(QtCore.QRect(430, 620, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.player2bet.setFont(font)
        self.player2bet.setObjectName(_fromUtf8("player2bet"))


        self.dollar2 = QtGui.QLabel(self.centralWidget)
        self.dollar2.setGeometry(QtCore.QRect(400, 620, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.dollar2.setFont(font)
        self.dollar2.setObjectName(_fromUtf8("dollar2"))


        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(720, 133, 111, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(_fromUtf8(" background-color: rgb(255, 255, 255);\n"
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
        self.pushButton.setObjectName(_fromUtf8("pushButton"))


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


        self.player2Money = QtGui.QLabel(self.centralWidget)
        self.player2Money.setGeometry(QtCore.QRect(376, 540, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.player2Money.setFont(font)
        self.player2Money.setAlignment(QtCore.Qt.AlignCenter)
        self.player2Money.setObjectName(_fromUtf8("player2Money"))


        self.player3Money = QtGui.QLabel(self.centralWidget)
        self.player3Money.setGeometry(QtCore.QRect(696, 540, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.player3Money.setFont(font)
        self.player3Money.setAlignment(QtCore.Qt.AlignCenter)
        self.player3Money.setObjectName(_fromUtf8("player3Money"))


        self.Round_2 = QtGui.QLabel(self.centralWidget)
        self.Round_2.setGeometry(QtCore.QRect(730, 10, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Round_2.setFont(font)
        self.Round_2.setObjectName(_fromUtf8("Round_2"))


        self.numberOfRound = QtGui.QLabel(self.centralWidget)
        self.numberOfRound.setGeometry(QtCore.QRect(840, 10, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.numberOfRound.setFont(font)
        self.numberOfRound.setObjectName(_fromUtf8("numberOfRound"))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def btnclick (self, MainWindow) :
        choice = QtGui.QMessageBox.question(self,'Extract',"Please just fucking work",QtGui.QMessageBox.Yes| QtGui.QMessageBox.No)

        if(choice == QtGui.QMessageBox.Yes) :
            print "hgdfghja"
        else : 
            pass


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Texas Hold'em Poker", None))
        self.CommunityCards.setText(_translate("MainWindow", "Community Cards", None))
        self.Round.setText(_translate("MainWindow", "Round :", None))
        self.nameOfRound.setText(_translate("MainWindow", "Preflop", None))
        self.Player1.setText(_translate("MainWindow", "Player1", None))
        self.Player2.setText(_translate("MainWindow", "Player2", None))
        self.PokerBot.setText(_translate("MainWindow", "Poker Bot", None))
        self.stopGame.setText(_translate("MainWindow", "STOP GAME", None))
        self.PotValue.setText(_translate("MainWindow", "POT", None))
        self.Botplays.setText(_translate("MainWindow", "Poker bot raised/folded/.......", None))
        self.player1Opt2.setText(_translate("MainWindow", "TextLabel", None))
        self.dollar1.setText(_translate("MainWindow", "$", None))
        self.player2Opt2.setText(_translate("MainWindow", "TextLabel", None))
        self.dollar2.setText(_translate("MainWindow", "$", None))
        self.pushButton.setText(_translate("MainWindow", "$", None))
        self.player1Money.setText(_translate("MainWindow", "$", None))
        self.player2Money.setText(_translate("MainWindow", "$", None))
        self.player3Money.setText(_translate("MainWindow", "$", None))
        self.Round_2.setText(_translate("MainWindow", "Game No. :", None))
        self.numberOfRound.setText(_translate("MainWindow", "Preflop", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


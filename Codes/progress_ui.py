from PyQt4 import QtCore, QtGui
import sys


class Ui_Dialog(object):
  def setupUi(self, MainWindow):
      MainWindow.setObjectName("MainWindow")
      MainWindow.resize(923, 619)
      self.centralwidget = QtGui.QWidget(MainWindow)
      self.centralwidget.setObjectName("centralwidget")
      MainWindow.setCentralWidget(self.centralwidget)
      self.statusbar = QtGui.QStatusBar(MainWindow)
      self.statusbar.setObjectName("statusbar")
      self.statusbar.showMessage('Welcome!')
      MainWindow.setStatusBar(self.statusbar)
      self.retranslateUi(MainWindow)
      QtCore.QMetaObject.connectSlotsByName(MainWindow)
  def retranslateUi(self, MainWindow):
      _translate = QtCore.QCoreApplication.translate
      MainWindow.setWindowTitle(_translate("MainWindow", "Test"))
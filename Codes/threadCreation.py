# from pokerUI import *

# class ThreadClass(QtCore.QThread) :

# 	def __init__(self) :
# 		super(ThreadClass,self). __init__()

# 	def run(self) :
# 		list = ['preflop','flop','turn','river']
# 		for i in list :
# 			self.emit(QtCore.SIGNAL('HEY'),i)

# class hope(QtGui.QMainWindow,pokerUI.Ui_MainWindow):
# 	def __init__ (self) :

# 		self.thread = ThreadClass()
# 		self.thread.start()
# 		self.connect(self.thread,QtCore.SIGNAL('HEY'),self.NameOfRound)

# 	#function to change the name of round
# 	def NameOfRound(self,Mainwindow,round):
# 		self.nameOfRound.setText(round)

import sys, time
from PyQt4 import QtCore, QtGui
 
class MyApp(QtGui.QWidget):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)

		self.setGeometry(300, 300, 280, 600)
		self.setWindowTitle('threads')

		self.layout = QtGui.QVBoxLayout(self)

		self.testButton = QtGui.QPushButton("test")
		self.connect(self.testButton, QtCore.SIGNAL("released()"), self.test)
		self.listwidget = QtGui.QListWidget(self)

		self.layout.addWidget(self.testButton)
		self.layout.addWidget(self.listwidget)

	def add(self, text):
		""" Add item to list widget """
		print "Add: " + text
		self.listwidget.addItem(text)
		self.listwidget.sortItems()

	def addBatch(self,text="test",iters=6,delay=0.3):
		""" Add several items to list widget """
		for i in range(iters):
			time.sleep(delay) # artificial time delay
			self.add(text+" "+str(i))

	def test(self):
		self.listwidget.clear()
		# adding entries just from main application: locks ui
		self.addBatch("_non_thread",iters=6,delay=0.3)
		# adding by emitting signal in different thread
		self.workThread = WorkThread()
		self.connect( self.workThread, QtCore.SIGNAL("update(QString)"), self.add )
		self.workThread.start()


class WorkThread(QtCore.QThread):
	def __init__(self):
		QtCore.QThread.__init__(self)

	def __del__(self):
		self.wait()

	def run(self):
		for i in range(6):
			time.sleep(0.3) # artificial time delay
			self.emit( QtCore.SIGNAL('update(QString)'), "from work thread " + str(i) )
		return

# run
app = QtGui.QApplication(sys.argv)
test = MyApp()
test.show()
sys.exit(app.exec_())
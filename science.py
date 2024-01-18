#!/usr/bin/python3

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
from std_msgs.msg import Int32,String
#from PyQt5.QtCore import QThread, pyqtSignal
import rospy
from pyqtgraph import PlotWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(4095, 4095)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lc1 = PlotWidget(self.centralwidget)
        self.lc1.setGeometry(QtCore.QRect(60, 110, 650, 350))
        self.lc1.setObjectName("lc1")
        self.lc1.setLabel('bottom', text='Time')
        self.lc1.setLabel('left', text='DHT(humidity(%))')

        self.sht1 = PlotWidget(self.centralwidget)

        self.sht1.setGeometry(QtCore.QRect(60, 500, 650, 350))
        self.sht1.setObjectName("sht1")
        self.sht1.setLabel('bottom', text='Time')
        self.sht1.setLabel('left', text='Temperature(deg)')

        self.sht2 = PlotWidget(self.centralwidget)
        self.sht2.setGeometry(QtCore.QRect(770, 110, 650, 350))
        self.sht2.setObjectName("sht2")
        self.sht2.setLabel('bottom', text='Time')
        self.sht2.setLabel('left', text='Humidity(%)')

        #self.jnz = PlotWidget(self.centralwidget)
        #self.jnz.setGeometry(QtCore.QRect(770, 500, 650, 350))
        #self.jnz.setObjectName("jnz")

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(60, 30, 1361, 27))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("DHT11")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)

        self.pushButton_2.setObjectName("SHT 10.1")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)

        self.pushButton_3.setObjectName("SHT 10.2")
        self.horizontalLayout.addWidget(self.pushButton_3)
        #self.pushButton_4 = QtWidgets.QPushButton(self.widget)

        #self.pushButton_4.setObjectName("pushButton_4")
        #self.horizontalLayout.addWidget(self.pushButton_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.lc1.show)
        self.pushButton_2.clicked.connect(self.sht1.show)
        self.pushButton_3.clicked.connect(self.sht2.show)
        #self.pushButton_4.clicked.connect(self.jnz.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "DHT11"))
        self.pushButton_2.setText(_translate("MainWindow", "SHT_10.1"))
        self.pushButton_3.setText(_translate("MainWindow", "SHT_10.2"))
        #self.pushButton_4.setText(_translate("MainWindow", "JUNK_GRAPH"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

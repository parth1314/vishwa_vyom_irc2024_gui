#!/usr/bin/python3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QSizePolicy
from pyqtgraph import PlotWidget
from std_msgs.msg import Int32,String
#from PyQt5.QtCore import QThread, pyqtSignal
import rospy
import sys

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        self.x_data = []  # Initialize x_data list
        self.y_data = []
        self.x1_data=[]
        self.y1_data=[]

        self.dht_g = PlotWidget(self.centralwidget)
        self.dht_g.setGeometry(QtCore.QRect(30, 160, 650, 350))
        self.dht_g.setObjectName("dht_g")
        self.dht_g.setLabel('bottom', text='Time')
        self.dht_g.setLabel('left', text='Temperature(deg)')

        self.mq135 = PlotWidget(self.centralwidget)
        self.mq135.setGeometry(QtCore.QRect(30, 540, 650, 350))
        self.mq135.setObjectName("mq135")
        self.mq135.setLabel('bottom', text='Time')
        self.mq135.setLabel('left', text='ppm') 


        self.frame = QtWidgets.QFrame(self.mq135)
        self.frame.setGeometry(QtCore.QRect(0, 0, 661, 371))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.mq135_2 = PlotWidget(self.centralwidget)
        self.mq135_2.setGeometry(QtCore.QRect(740, 160, 650, 350))
        self.mq135_2.setObjectName("mq135_2")
        self.mq135_2.setLabel('bottom', text='Time')
        self.mq135_2.setLabel('left', text='ppm')


        self.bmp = PlotWidget(self.centralwidget)
        self.bmp.setGeometry(QtCore.QRect(740, 540, 650, 350))
        self.bmp.setObjectName("bmp")
        self.bmp.setLabel('bottom', text='Time')
        self.bmp.setLabel('left', text='Pascal')


        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(40, 60, 1351, 27))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.DHT = QtWidgets.QPushButton(self.widget)
        self.DHT.setObjectName("DHT")
        self.horizontalLayout.addWidget(self.DHT)
        self.MQ135 = QtWidgets.QPushButton(self.widget)
        self.MQ135.setObjectName("MQ135")
        self.horizontalLayout.addWidget(self.MQ135)
        self.MQ135_2 = QtWidgets.QPushButton(self.widget)
        self.MQ135_2.setObjectName("MQ135_2")
        self.horizontalLayout.addWidget(self.MQ135_2)
        self.BMP = QtWidgets.QPushButton(self.widget)
        self.BMP.setObjectName("BMP")
        self.horizontalLayout.addWidget(self.BMP)
        #self.OTHR_BUTN = QtWidgets.QPushButton(self.widget)
        #self.OTHR_BUTN.setObjectName("OTHR_BUTN")
        #self.horizontalLayout.addWidget(self.OTHR_BUTN)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        self.DHT.clicked.connect(self.start_plotting)  # Connect the button to start plotting
        self.MQ135.clicked.connect(self.mq135_1)

        # ROS subscriber setup
        rospy.init_node('ros_gui_subscriber')
        self.subscriber = rospy.Subscriber('numbers', Int32, self.receive_data)
        self.subscriber1 = rospy.Subscriber('numbers2', Int32, self.receive_data1)
        
                                

    
        self.retranslateUi(MainWindow)
        self.DHT.clicked.connect(self.dht_g.show)
        self.MQ135_2.clicked.connect(self.mq135_2.show)
        self.MQ135.clicked.connect(self.mq135.show)
        self.BMP.clicked['bool'].connect(self.bmp.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def start_plotting(self):
        self.dht_g.clear()
    def mq135_1(self):
        self.mq135.clear()

    def receive_data(self,msg):
        data1=msg.data
        x = len(self.x_data) + 1
        self.x_data.append(x)
        self.y_data.append(data1)
        self.dht_g.plot(self.x_data, self.y_data, pen=(1, 3))
        
        # Check if the message has the format "dht11"
    def receive_data1(self,msg):
        data1=msg.data
        x1=len(self.x1_data)+1
        self.x1_data.append(x1)
        self.y1_data.append(data1)
        self.mq135.plot(self.x1_data,self.y1_data,pen=(1,3))
    
        

    
   
   

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.DHT.setText(_translate("MainWindow", "dht11"))
        self.MQ135.setText(_translate("MainWindow", "MQ135_1"))
        self.MQ135_2.setText(_translate("MainWindow", "MQ135_2"))
        self.BMP.setText(_translate("MainWindow", "BMP180"))
        #self.OTHR_BUTN.setText(_translate("MainWindow", "LAUNCH SCIENCE_2"))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

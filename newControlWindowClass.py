from PyQt5 import QtCore, QtGui, QtWidgets
from joystick import JoystickWidget

class NewControlWindow():

    def __init__(self):
        self.controlWindow = QtWidgets.QMainWindow()
        self.controlWindow.setObjectName("controlWindow")
        self.controlWindow.resize(1047, 626)
        self.controlWindow.setAutoFillBackground(False)
        
        self.centralwidget = QtWidgets.QWidget(self.controlWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")

        self.centralWidgetGrid = QtWidgets.QGridLayout(self.centralwidget)
        self.centralWidgetGrid.setObjectName("centralWidgetGrid")
        self.controlWindowHorizontalLay = QtWidgets.QHBoxLayout()
        self.controlWindowHorizontalLay.setObjectName("controlWindowHorizontalLay")
        
        self.joystickGrid = QtWidgets.QGridLayout(self.centralwidget)
        self.joystickGrid.setObjectName("joystickGrid")


        self.joystickWidgetLeftLayout = JoystickWidget("Left").getJoystickLayout()
        self.joystickWidgetRightLayout = JoystickWidget("Right").getJoystickLayout()


        self.joystickGrid.addLayout(self.joystickWidgetLeftLayout,1,0,1,1)
        self.joystickGrid.addLayout(self.joystickWidgetRightLayout,1,1,1,1)
        
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.centralWidgetGrid.addItem(spacerItem, 0,0,1,1)
        self.controlWindowHorizontalLay.addLayout(self.joystickGrid)
        self.centralWidgetGrid.addLayout(self.controlWindowHorizontalLay, 0,1,1,1)
        

        self.controlWindow.setCentralWidget(self.centralwidget)

        
        self.controlWindow.show()
from PyQt5 import QtCore, QtGui, QtWidgets

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
        self.controlWindow.show()

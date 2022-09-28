from PyQt5 import QtCore, QtWidgets
from ControlSettingWidget import *


def initPage2(self):
    
    self.page_2 = QtWidgets.QWidget()
    self.page_2.setObjectName("page_2")
    self.page2GridLay = QtWidgets.QGridLayout(self.page_2)
    self.page2GridLay.setObjectName("page2GridLay")
    self.settingVerticalLay = QtWidgets.QVBoxLayout()
    self.settingVerticalLay.setObjectName("settingVerticalLay")
    topSpacer= QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    self.settingVerticalLay.addItem(topSpacer)
    self.droneSysHorizontalLay = QtWidgets.QHBoxLayout()
    self.droneSysHorizontalLay.setObjectName("droneSysHorizontalLay")
    spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    self.droneSysHorizontalLay.addItem(spacerItem)
    self.label = QtWidgets.QLabel(self.page_2)
    self.label.setObjectName("label")
    self.droneSysHorizontalLay.addWidget(self.label)
    self.typeDropDown = QtWidgets.QComboBox(self.page_2)
    self.typeDropDown.setObjectName("typeDropDown")
    self.typeDropDown.addItem("")
    self.typeDropDown.addItem("")
    self.droneSysHorizontalLay.addWidget(self.typeDropDown)
    self.selectButton = QtWidgets.QPushButton(self.page_2)
    self.selectButton.setObjectName("selectButton")
    self.droneSysHorizontalLay.addWidget(self.selectButton)
    spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    self.droneSysHorizontalLay.addItem(spacerItem1)
    self.droneSysHorizontalLay.setStretch(0, 1)
    self.droneSysHorizontalLay.setStretch(2, 2)
    self.droneSysHorizontalLay.setStretch(4, 1)
    self.settingVerticalLay.addLayout(self.droneSysHorizontalLay)
    spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
    self.settingVerticalLay.addItem(spacerItem2)
    self.controlModeSetHorizontalLay = QtWidgets.QHBoxLayout()
    self.controlModeSetHorizontalLay.setObjectName("controlModeSetHorizontalLay")
    leftSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    self.controlModeSetHorizontalLay.addItem(leftSpacer)
    
    self.controlSetVerticalLay = ControlSettingWidget(self.page_2).getWidget()
    self.controlModeSetHorizontalLay.addLayout(self.controlSetVerticalLay)
    
    spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    self.controlModeSetHorizontalLay.addItem(spacerItem3)
    
    self.settingVerticalLay.addLayout(self.controlModeSetHorizontalLay)
    spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
    self.settingVerticalLay.addItem(spacerItem4)

    self.confirmSetButton = QtWidgets.QPushButton(self.page_2)
    self.confirmSetButton.setObjectName("confirmSetButton")
    self.settingVerticalLay.addWidget(self.confirmSetButton)
    self.settingVerticalLay.setStretch(0, 1)

    self.settingVerticalLay.setStretch(2, 1)
    self.settingVerticalLay.setStretch(3, 1)
    self.settingVerticalLay.setStretch(4, 1)    
    self.page2GridLay.addLayout(self.settingVerticalLay, 0, 0, 1, 1)
    self.stackedWidget.addWidget(self.page_2)


    retranslate(self)

def retranslate(self):
    _translate = QtCore.QCoreApplication.translate
    self.label.setText(_translate("MainWindow", "Please select drone system"))
    self.typeDropDown.setItemText(0, _translate("MainWindow", "Betaflight System Based Drones"))
    self.typeDropDown.setItemText(1, _translate("MainWindow", "Ardupilot System Based Drones"))
    self.selectButton.setText(_translate("MainWindow", "Select"))
    self.confirmSetButton.setText(_translate("MainWindow", "Confirm Your Settings"))

    self.selectButton.clicked.connect(self.changeInterfaceBasedOnModel)

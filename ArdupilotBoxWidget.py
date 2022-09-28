from PyQt5 import QtCore, QtWidgets

class ArdupilotBoxWidget(QtWidgets.QWidget):
     def __init__(self, page, parent=None):
        QtWidgets.QWidget.__init__(self, parent=parent)
        
        self.boxWidget = QtWidgets.QWidget(page)
        self.modeSetVerticalLay = QtWidgets.QVBoxLayout(self.boxWidget)
        self.modeSetVerticalLay.setObjectName("modeSetVerticalLay")
        self.modeSetLabel = QtWidgets.QLabel(self.boxWidget)
        self.modeSetLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.modeSetLabel.setObjectName("modeSetLabel")
        self.modeSetVerticalLay.addWidget(self.modeSetLabel)
        self.modeSetGrid = QtWidgets.QGridLayout()
        self.modeSetGrid.setObjectName("modeSetGrid")
        self.OSDSetSelect = QtWidgets.QComboBox(self.boxWidget)
        self.OSDSetSelect.setObjectName("OSDSetSelect")
        self.modeSetGrid.addWidget(self.OSDSetSelect, 4, 1, 1, 1)
        self.preArmSetLabel = QtWidgets.QLabel(self.boxWidget)
        self.preArmSetLabel.setObjectName("preArmSetLabel")
        self.modeSetGrid.addWidget(self.preArmSetLabel, 0, 0, 1, 1)
        self.armSetLabel = QtWidgets.QLabel(self.boxWidget)
        self.armSetLabel.setObjectName("armSetLabel")
        self.modeSetGrid.addWidget(self.armSetLabel, 1, 0, 1, 1)
        self.flightModeSetLabel = QtWidgets.QLabel(self.boxWidget)
        self.flightModeSetLabel.setObjectName("flightModeSetLabel")
        self.modeSetGrid.addWidget(self.flightModeSetLabel, 2, 0, 1, 1)
        self.OSDSetLabel = QtWidgets.QLabel(self.boxWidget)
        self.OSDSetLabel.setObjectName("OSDSetLabel")
        self.modeSetGrid.addWidget(self.OSDSetLabel, 4, 0, 1, 1)
        self.preArmSetSelect = QtWidgets.QComboBox(self.boxWidget)
        self.preArmSetSelect.setObjectName("preArmSetSelect")
        self.modeSetGrid.addWidget(self.preArmSetSelect, 0, 1, 1, 1)
        self.armSetSelect = QtWidgets.QComboBox(self.boxWidget)
        self.armSetSelect.setObjectName("armSetSelect")
        self.modeSetGrid.addWidget(self.armSetSelect, 1, 1, 1, 1)
        self.beeperSetSelect = QtWidgets.QComboBox(self.boxWidget)
        self.beeperSetSelect.setObjectName("beeperSetSelect")
        self.modeSetGrid.addWidget(self.beeperSetSelect, 3, 1, 1, 1)
        self.beeperSetLabel = QtWidgets.QLabel(self.boxWidget)
        self.beeperSetLabel.setObjectName("beeperSetLabel")
        self.modeSetGrid.addWidget(self.beeperSetLabel, 3, 0, 1, 1)
        self.flightModeSetBut = QtWidgets.QPushButton(self.boxWidget)
        self.flightModeSetBut.setObjectName("flightModeSetBut")
        self.modeSetGrid.addWidget(self.flightModeSetBut, 2, 1, 1, 1)
        self.modeSetVerticalLay.addLayout(self.modeSetGrid)
        self.modeSetVerticalLay.setStretch(1, 1)

        # self.preArmSetLabel.setAlignment(QtCore.Qt.AlignCenter)
        # self.armSetLabel.setAlignment(QtCore.Qt.AlignCenter)
        # self.flightModeSetLabel.setAlignment(QtCore.Qt.AlignCenter)
        # self.OSDSetLabel.setAlignment(QtCore.Qt.AlignCenter)
        # self.beeperSetLabel.setAlignment(QtCore.Qt.AlignCenter)



        

        self.retranslateUi()

     def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

        self.modeSetLabel.setText(_translate("MainWindow", "Modes/Features"))
        self.preArmSetLabel.setText(_translate("MainWindow", "Prearm"))
        self.armSetLabel.setText(_translate("MainWindow", "Arm"))
        self.flightModeSetLabel.setText(_translate("MainWindow", "Flight Mode"))
        self.OSDSetLabel.setText(_translate("MainWindow", "ardu"))
        self.beeperSetLabel.setText(_translate("MainWindow", "Beeper"))
        self.flightModeSetBut.setText(_translate("MainWindow", "Flight Mode Key Setting"))
        
     def getWidget(self):
          return self.boxWidget
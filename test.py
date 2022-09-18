# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1026, 642)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1031, 581))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.flightmodeKey = QtWidgets.QLineEdit(self.page)
        self.flightmodeKey.setGeometry(QtCore.QRect(770, 280, 31, 31))
        self.flightmodeKey.setText("")
        self.flightmodeKey.setMaxLength(1)
        self.flightmodeKey.setObjectName("flightmodeKey")
        self.armLabel = QtWidgets.QLabel(self.page)
        self.armLabel.setGeometry(QtCore.QRect(720, 240, 31, 21))
        self.armLabel.setObjectName("armLabel")
        self.beeperKey = QtWidgets.QLineEdit(self.page)
        self.beeperKey.setGeometry(QtCore.QRect(770, 330, 31, 31))
        self.beeperKey.setText("")
        self.beeperKey.setMaxLength(1)
        self.beeperKey.setObjectName("beeperKey")
        self.beeperLabel = QtWidgets.QLabel(self.page)
        self.beeperLabel.setGeometry(QtCore.QRect(710, 340, 51, 21))
        self.beeperLabel.setObjectName("beeperLabel")
        self.angleLabel = QtWidgets.QLabel(self.page)
        self.angleLabel.setGeometry(QtCore.QRect(620, 290, 41, 21))
        self.angleLabel.setObjectName("angleLabel")
        self.currentMode = QtWidgets.QLineEdit(self.page)
        self.currentMode.setGeometry(QtCore.QRect(820, 280, 31, 31))
        self.currentMode.setText("")
        self.currentMode.setMaxLength(1)
        self.currentMode.setObjectName("currentMode")
        self.modesLabel = QtWidgets.QLabel(self.page)
        self.modesLabel.setGeometry(QtCore.QRect(720, 110, 121, 21))
        self.modesLabel.setObjectName("modesLabel")
        self.armKey = QtWidgets.QLineEdit(self.page)
        self.armKey.setGeometry(QtCore.QRect(770, 230, 31, 31))
        self.armKey.setText("")
        self.armKey.setMaxLength(1)
        self.armKey.setObjectName("armKey")
        self.prearmKey = QtWidgets.QLineEdit(self.page)
        self.prearmKey.setGeometry(QtCore.QRect(770, 180, 31, 31))
        self.prearmKey.setText("")
        self.prearmKey.setMaxLength(1)
        self.prearmKey.setObjectName("prearmKey")
        self.horizonLabel = QtWidgets.QLabel(self.page)
        self.horizonLabel.setGeometry(QtCore.QRect(670, 290, 51, 21))
        self.horizonLabel.setObjectName("horizonLabel")
        self.acroLabel = QtWidgets.QLabel(self.page)
        self.acroLabel.setGeometry(QtCore.QRect(730, 290, 31, 21))
        self.acroLabel.setObjectName("acroLabel")
        self.OSDKey = QtWidgets.QLineEdit(self.page)
        self.OSDKey.setGeometry(QtCore.QRect(770, 380, 31, 31))
        self.OSDKey.setText("")
        self.OSDKey.setMaxLength(1)
        self.OSDKey.setObjectName("OSDKey")
        self.displayFrame = QtWidgets.QLabel(self.page)
        self.displayFrame.setGeometry(QtCore.QRect(70, 10, 451, 451))
        self.displayFrame.setText("")
        self.displayFrame.setObjectName("displayFrame")
        self.Stop = QtWidgets.QPushButton(self.page)
        self.Stop.setGeometry(QtCore.QRect(170, 480, 80, 23))
        self.Stop.setObjectName("Stop")
        self.Start = QtWidgets.QPushButton(self.page)
        self.Start.setGeometry(QtCore.QRect(330, 480, 80, 23))
        self.Start.setObjectName("Start")
        self.prearmLabel = QtWidgets.QLabel(self.page)
        self.prearmLabel.setGeometry(QtCore.QRect(710, 190, 51, 21))
        self.prearmLabel.setObjectName("prearmLabel")
        self.OSDDisableLabel = QtWidgets.QLabel(self.page)
        self.OSDDisableLabel.setGeometry(QtCore.QRect(650, 390, 111, 21))
        self.OSDDisableLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.OSDDisableLabel.setObjectName("OSDDisableLabel")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.controlsSetLabel = QtWidgets.QLabel(self.page_2)
        self.controlsSetLabel.setGeometry(QtCore.QRect(190, 120, 57, 15))
        self.controlsSetLabel.setObjectName("controlsSetLabel")
        self.layoutWidget = QtWidgets.QWidget(self.page_2)
        self.layoutWidget.setGeometry(QtCore.QRect(260, 60, 481, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.typeBoxLabel = QtWidgets.QLabel(self.layoutWidget)
        self.typeBoxLabel.setObjectName("typeBoxLabel")
        self.horizontalLayout.addWidget(self.typeBoxLabel)
        self.typeDropDown = QtWidgets.QComboBox(self.layoutWidget)
        self.typeDropDown.setObjectName("typeDropDown")
        self.typeDropDown.addItem("")
        self.typeDropDown.addItem("")
        self.horizontalLayout.addWidget(self.typeDropDown)
        self.layoutWidget1 = QtWidgets.QWidget(self.page_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(260, 160, 51, 261))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.throttleSetUp = QtWidgets.QLineEdit(self.layoutWidget1)
        self.throttleSetUp.setText("")
        self.throttleSetUp.setMaxLength(1)
        self.throttleSetUp.setObjectName("throttleSetUp")
        self.gridLayout.addWidget(self.throttleSetUp, 0, 0, 1, 1)
        self.throttleSetDown = QtWidgets.QLineEdit(self.layoutWidget1)
        self.throttleSetDown.setText("")
        self.throttleSetDown.setMaxLength(1)
        self.throttleSetDown.setObjectName("throttleSetDown")
        self.gridLayout.addWidget(self.throttleSetDown, 0, 1, 1, 1)
        self.yawSetClockwise = QtWidgets.QLineEdit(self.layoutWidget1)
        self.yawSetClockwise.setText("")
        self.yawSetClockwise.setMaxLength(1)
        self.yawSetClockwise.setObjectName("yawSetClockwise")
        self.gridLayout.addWidget(self.yawSetClockwise, 1, 0, 1, 1)
        self.yawSetAnticlockwise = QtWidgets.QLineEdit(self.layoutWidget1)
        self.yawSetAnticlockwise.setText("")
        self.yawSetAnticlockwise.setMaxLength(1)
        self.yawSetAnticlockwise.setObjectName("yawSetAnticlockwise")
        self.gridLayout.addWidget(self.yawSetAnticlockwise, 1, 1, 1, 1)
        self.rollSetLeft = QtWidgets.QLineEdit(self.layoutWidget1)
        self.rollSetLeft.setText("")
        self.rollSetLeft.setMaxLength(1)
        self.rollSetLeft.setObjectName("rollSetLeft")
        self.gridLayout.addWidget(self.rollSetLeft, 2, 0, 1, 1)
        self.rollSetRight = QtWidgets.QLineEdit(self.layoutWidget1)
        self.rollSetRight.setText("")
        self.rollSetRight.setMaxLength(1)
        self.rollSetRight.setObjectName("rollSetRight")
        self.gridLayout.addWidget(self.rollSetRight, 2, 1, 1, 1)
        self.pitchSetFront = QtWidgets.QLineEdit(self.layoutWidget1)
        self.pitchSetFront.setText("")
        self.pitchSetFront.setMaxLength(1)
        self.pitchSetFront.setObjectName("pitchSetFront")
        self.gridLayout.addWidget(self.pitchSetFront, 3, 0, 1, 1)
        self.pitchSetBack = QtWidgets.QLineEdit(self.layoutWidget1)
        self.pitchSetBack.setText("")
        self.pitchSetBack.setMaxLength(1)
        self.pitchSetBack.setObjectName("pitchSetBack")
        self.gridLayout.addWidget(self.pitchSetBack, 3, 1, 1, 1)
        self.layoutWidget2 = QtWidgets.QWidget(self.page_2)
        self.layoutWidget2.setGeometry(QtCore.QRect(110, 170, 61, 241))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.throttleSetLabel = QtWidgets.QLabel(self.layoutWidget2)
        self.throttleSetLabel.setObjectName("throttleSetLabel")
        self.verticalLayout.addWidget(self.throttleSetLabel)
        self.yawSetLabel = QtWidgets.QLabel(self.layoutWidget2)
        self.yawSetLabel.setObjectName("yawSetLabel")
        self.verticalLayout.addWidget(self.yawSetLabel)
        self.rollSetLabel = QtWidgets.QLabel(self.layoutWidget2)
        self.rollSetLabel.setObjectName("rollSetLabel")
        self.verticalLayout.addWidget(self.rollSetLabel)
        self.pitchSetLabel = QtWidgets.QLabel(self.layoutWidget2)
        self.pitchSetLabel.setObjectName("pitchSetLabel")
        self.verticalLayout.addWidget(self.pitchSetLabel)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidget.addWidget(self.page_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1026, 20))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu_File.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.armLabel.setText(_translate("MainWindow", "Arm"))
        self.beeperLabel.setText(_translate("MainWindow", "Beeper"))
        self.angleLabel.setText(_translate("MainWindow", "Angle"))
        self.modesLabel.setText(_translate("MainWindow", "Modes/Features"))
        self.horizonLabel.setText(_translate("MainWindow", "Horizon"))
        self.acroLabel.setText(_translate("MainWindow", "Acro"))
        self.Stop.setText(_translate("MainWindow", "Stop"))
        self.Start.setText(_translate("MainWindow", "Start"))
        self.prearmLabel.setText(_translate("MainWindow", "Prearm"))
        self.OSDDisableLabel.setText(_translate("MainWindow", "OSD Disable SW"))
        self.controlsSetLabel.setText(_translate("MainWindow", "Controls"))
        self.typeBoxLabel.setText(_translate("MainWindow", "Please select drone system"))
        self.typeDropDown.setItemText(0, _translate("MainWindow", "Betaflight System Based Drones"))
        self.typeDropDown.setItemText(1, _translate("MainWindow", "Ardupilot System Based Drones"))
        self.throttleSetLabel.setText(_translate("MainWindow", "Throttle"))
        self.yawSetLabel.setText(_translate("MainWindow", "Yaw"))
        self.rollSetLabel.setText(_translate("MainWindow", "Roll"))
        self.pitchSetLabel.setText(_translate("MainWindow", "Pitch"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

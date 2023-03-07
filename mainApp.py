import sys
from Controls import *
from PyQt5.QtGui import QIcon, QPixmap
from SettingConfirmPopup import *
from copy import deepcopy
from dictionary import *
from newControlWindowClass import NewControlWindow

HOMEPAGE = 0
CONTROLPAGE = 1
SWARMPAGE = 2
SETTINGPAGE = 3
STARTCONTROL = "start control"
STOPCONTROL = "stop control"

class MainApp():

    def __init__(self, args):
        self.app = QtWidgets.QApplication(args)
        self.window = QtWidgets.QMainWindow()
        self.yamlHelper = YamlHelper()
        self.keySettingInfo = KeySettingsInfo()
        self.availableKeys = self.keySettingInfo.getAvailableKeys()
        self.ui = Controls(self.window, self.yamlHelper, self.keySettingInfo)
           
        self.createActions(self.window)
        
        self.retranslateUi()
        self.window.show()
        sys.exit(self.app.exec_())

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

        self.ui.flightDataLabel.setText(_translate("MainWindow", "Flight Data:"))


    #CREATE ACTIONS FOR TOOL BAR
    def createActions(self, mainWindowBase):
        oldPageNum = self.ui.stackedWidget.currentIndex()
        self.ui.homeAction = QtWidgets.QAction(mainWindowBase)
        self.ui.homeAction.setText("&Home")
        self.ui.homeAction.setIcon(QIcon(QPixmap("./icons/house-icon.webp")))
        self.ui.toolBar.addAction(self.ui.homeAction)
        self.ui.homeAction.triggered.connect(lambda: self.toPage(HOMEPAGE))

        self.ui.controlAction = QtWidgets.QAction(mainWindowBase)
        self.ui.controlAction.setText("&Drone Controls")
        self.ui.controlAction.setIcon(QIcon(QPixmap("./icons/control-panel-icon.webp")))
        self.ui.toolBar.addAction(self.ui.controlAction)
        self.ui.controlAction.triggered.connect(lambda: self.toPage(CONTROLPAGE))

        self.ui.swarmAction = QtWidgets.QAction(mainWindowBase)
        self.ui.swarmAction.setText("&Swarming")
        self.ui.swarmAction.setIcon(QIcon(QPixmap("./icons/air-drone-icon.png")))
        self.ui.toolBar.addAction(self.ui.swarmAction)
        self.ui.swarmAction.triggered.connect(lambda: self.toPage(SWARMPAGE))


        self.ui.settingAction = QtWidgets.QAction(mainWindowBase)
        self.ui.settingAction.setText("&Setting")
        self.ui.settingAction.setIcon(QIcon(QPixmap("./icons/setting-line-icon.webp")))
        self.ui.toolBar.addAction(self.ui.settingAction)
        self.ui.settingAction.triggered.connect(lambda: self.toPage(SETTINGPAGE))


        self.ui.flightDataLabel = QtWidgets.QLabel()
        self.ui.flightDataLabel.setGeometry(QtCore.QRect(720, 240, 31, 21))
        self.ui.flightDataLabel.setObjectName("flightDataLabel")
        self.ui.toolBar.addWidget(self.ui.flightDataLabel)

        right_spacer = QtWidgets.QWidget()
        right_spacer.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.ui.toolBar.addWidget(right_spacer)
    
        self.ui.startAction = QtWidgets.QAction(mainWindowBase)
        self.ui.startAction.setText("&Start Drone Control")
        self.ui.startAction.setIcon(QIcon(QPixmap("./icons/start-button-icon.png")))
        self.ui.toolBar.addAction(self.ui.startAction)
        self.ui.startAction.triggered.connect(self.startControl)

        self.ui.stopAction = QtWidgets.QAction(mainWindowBase)
        self.ui.stopAction.setText("&Start Drone Control")
        self.ui.stopAction.setIcon(QIcon(QPixmap("./icons/stop-road-sign-icon.png")))
        self.ui.toolBar.addAction(self.ui.stopAction)
        self.ui.stopAction.triggered.connect(self.stopControl)
        

        self.ui.toolBar.setIconSize(QtCore.QSize(48, 48))
        self.ui.toolBar.setStyleSheet("QToolBar{spacing:30px;}")

    def startControl(self):
        """
            To start the drone control. Eg. record user pressed key
        """
        self.controlWindow = NewControlWindow()
        self.ui.trackKeyThread.start()

    def stopControl(self):
        """
            To stop the drone control. Eg. stop recording user pressed key
        """
        self.ui.trackKeyThread.stop()

    #REDIRECT PAGE AFTER CLICKING TOOLBAR ICONS
    def toPage(self, pageNumber):
        oldPageNum = self.ui.stackedWidget.currentIndex()
        self.keySettingInfo.didUserIgnoreChanges = False #reset user ignore changes flag

        if self.keySettingInfo.hasControlChanged:
            if self.keySettingInfo.hasSetConfirmClicked:

                self.keySettingInfo.hasSetConfirmClicked = False
                self.keySettingInfo.hasControlChanged = False
                self.ui.stackedWidget.setCurrentIndex(pageNumber)

            else:
                #POP UP MSG SAYING CLICK CONFIRM FIRST
                messageBox = SettingConfirmPopup(self.window)
                if messageBox.getResult() == "Ignore Changes":
                    self.keySettingInfo.didUserIgnoreChanges = True #make ignore changes flag = T so the system won't detect revert keys as changed key
                    self.keySettingInfo.hasControlChanged = False
                    
                    #reset control setting to old setting (previously saved setting)
                    #-----------------------------------------------------------
                    conSetting = self.ui.controlSettingWidget

                    oldControlSetting = self.ui.oldControlSetting
                    conSetting.resetControlToOldSetting(oldControlSetting)
                    #-----------------------------------------------------------

                    #reset current drone system based feature key assignment setting
                    #to old previously saved setting
                    #-----------------------------------------------------------
                    currentSys = self.ui.currentSys
                    featureWidgetClass = self.ui.getSysClass(currentSys)

                    featureWidgetClass.resetFeatureToOldSetting(oldControlSetting)
                    #-----------------------------------------------------------
                    
                    self.keySettingInfo.didUserIgnoreChanges = False #reset ignore changes flag

                #GO BACK
                else:
                    
                    pass


                print(messageBox.getResult())
                pass
        else:
            self.ui.stackedWidget.setCurrentIndex(pageNumber)
        

        #IF NOT AT SETTING PAGE BEFORE AND SWITCHES TO SETTING PAGE
        if oldPageNum != 1 and pageNumber == 1:
            print(" old page num", oldPageNum)
            #RECORD OLD SETTINGS WHEN WE ARRIVED IN THE SETTING PAGE
            self.ui.oldControlSetting.clear()

            temp = self.ui.controlSettingWidget
            controlSetting = {}
            controlSetting[PF] = temp.pitchSetFront.currentText()
            controlSetting[PB] = temp.pitchSetBack.currentText()
            controlSetting[RL] = temp.rollSetLeft.currentText()
            controlSetting[RR] = temp.rollSetRight.currentText()
            controlSetting[YC] = temp.yawSetClockwise.currentText()
            controlSetting[YA] = temp.yawSetAnticlockwise.currentText()
            controlSetting[TD] = temp.throttleSetDown.currentText()
            controlSetting[TU] = temp.throttleSetUp.currentText()

            #record feature key settings
            #----------------------------------------------------------
            currentSys = self.ui.currentSys
            featureWidgetClass = self.ui.getSysClass(currentSys)
            
            for key,value in featureWidgetClass.dictOfComboBox.items():
                comboBox = value.getComboBox()
                controlSetting[key] = comboBox.currentText()
            #-----------------------------------------------------------

            self.ui.oldControlSetting = controlSetting #TODO change this here to keysetting info


if __name__ == "__main__":
   MainApp(sys.argv)
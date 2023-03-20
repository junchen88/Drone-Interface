from test import *
import QThreadClass
import cv2
import usefulFunctions as uf
import TrackKeyClass
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from BetaFlightBoxWidget import *
from ArdupilotBoxWidget import *
from initPage2 import *
from yamlHelper import YamlHelper
from keySettingClass import KeySettingsInfo
from sysBasedFeatureSettingWidget import SysBasedFeatureSettingWidget
from SettingConfirmPopup import SettingConfirmPopup

DEFAULT_MODEL = 'Betaflight'
MODELSINITDICT = {"Betaflight":False, "Ardupilot":False}
MODELMAPPING = ['Betaflight', 'Ardupilot']


class Drone_system():
    def __init__(self, droneSysStr):
        self.isInitialised = False
        self.droneSysStr = droneSysStr


class Controls(Ui_MainWindow):
    def __init__(self, mainWindowBase, yamlHelper:YamlHelper, keySettingInfo:KeySettingsInfo):
        Ui_MainWindow.setupUi(self, mainWindowBase, yamlHelper, keySettingInfo)
        self.window = mainWindowBase
        self.availableKeys = keySettingInfo.getAvailableKeys()
        self.oldControlSetting = {}   #TO STORE OLD SETTING AND TO REVERT SETTINGS

        #Init for camera display thread
        #------------------------------------------------------------------
        self.Start.clicked.connect(self.start)
        self.Stop.clicked.connect(self.stop)

        # create the video capture thread
        self.camThread = QThreadClass.QThreadClass()

        # connect its signal to the update_image slot
        self.camThread.change_pixmap_signal.connect(self.update_image)
        self.camThread.setCurrentFunction(uf.runCamera)
        # start the thread
        self.camThread.start()
        #------------------------------------------------------------------

        self.trackKeyThread = TrackKeyClass.TrackKeyClass(keySettingInfo)
        initPage2(self, self.availableKeys, self.oldControlSetting, yamlHelper, keySettingInfo)
        
        self.yamlHelper = yamlHelper
        self.keySettingInfo = keySettingInfo
        self.chooseInit(DEFAULT_MODEL)
        self.confirmSetButton.clicked.connect(lambda: self.clickedConfirmBut())

        self.currentSys = DEFAULT_MODEL

        self.keySettingInfo.getAllComboBox(self.controlSettingWidget, self.getSysClass(self.currentSys))

       

    #HELPER FUNCTION TO INITIALISE INTERFACE BASED ON DRONE SYSTEM
    def chooseInit(self, model):
        MODELSINITDICT[model] = True
        if model == 'Betaflight':
            
            self.groupBoxHome = SysBasedFeatureSettingWidget(self.page, self.keySettingInfo, self.yamlHelper, "Betaflight", HOME)
            self.groupBoxHomeBeta = self.groupBoxHome.getWidget()
            self.betaClass = SysBasedFeatureSettingWidget(self.page_2, self.keySettingInfo, self.yamlHelper, "Betaflight", SETTING, self.groupBoxHome)
            self.groupBoxBeta = self.betaClass.getWidget()
            
            self.controlModeSetHorizontalLay.addWidget(self.groupBoxBeta)
           
            rightSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.controlModeSetHorizontalLay.addItem(rightSpacer)
            self.controlModeSetHorizontalLay.setStretch(0, 1)
            self.controlModeSetHorizontalLay.setStretch(1, 1)
            self.controlModeSetHorizontalLay.setStretch(3, 1)
            self.controlModeSetHorizontalLay.setStretch(4, 1)

            self.homeSettingVerticalLay.addWidget(self.groupBoxHomeBeta)

        elif model == 'Ardupilot':
            groupBoxHome = SysBasedFeatureSettingWidget(self.page, self.keySettingInfo, self.yamlHelper, "Ardupilot", HOME)
            self.groupBoxHomeArdu = groupBoxHome.getWidget()
            self.arduClass =SysBasedFeatureSettingWidget(self.page_2, self.keySettingInfo, self.yamlHelper, "Ardupilot", SETTING, groupBoxHome)
            self.groupBoxArdu = self.arduClass.getWidget()
            self.controlModeSetHorizontalLay.insertWidget(3,self.groupBoxArdu)
            self.homeSettingVerticalLay.insertWidget(1, self.groupBoxHomeArdu)



        else:
            print("Something's wrong - using default system")
            
            self.groupBoxHome = SysBasedFeatureSettingWidget(self.page, self.keySettingInfo, self.yamlHelper, "Betaflight", HOME)
            self.groupBoxHomeBeta = self.groupBoxHome.getWidget()
            self.betaClass = SysBasedFeatureSettingWidget(self.page_2, self.keySettingInfo,self.yamlHelper, "Betaflight", SETTING, self.groupBoxHome)
            self.groupBoxBeta = self.betaClass.getWidget()
        

    #RETURNS THE INTERFACE BASED ON THE DRONE SYSTEM
    #IN THE FORMAT OF SETTING BOX, HOME BOX
    def getModel(self, model):
        if model == 'Betaflight':
            return self.groupBoxBeta, self.groupBoxHomeBeta

        elif model == 'Ardupilot':
            return self.groupBoxArdu, self.groupBoxHomeArdu


    def getSysClass(self, nameOfSys):
        if nameOfSys == 'Betaflight':
            return self.betaClass

        elif nameOfSys == 'Ardupilot':
            return self.arduClass
        

    #FUNCTION FOR CHANGING INTERFACE BASED ON THE DRONE SYSTEM
    #SELECTED - ASSIGNED TO CONFIRM BUTTOM
    #This is for changing dropdown menu in setting page
    def changeInterfaceBasedOnModel(self):
        currentIndex = self.typeDropDown.currentIndex()
        selectedModel = MODELMAPPING[currentIndex]

        #if system didn't change, don't do anything
        if selectedModel == self.currentSys:
            return

        #if control has changed
        if self.keySettingInfo.hasControlChanged:
            
            #Clicked the confirm button
            if self.keySettingInfo.hasSetConfirmClicked:
                self.currentSys = selectedModel
                self.keySettingInfo.hasSetConfirmClicked = False
                self.keySettingInfo.hasControlChanged = False
                
            
            else:

                #create pop up msg box if the user didn't click confirm
                #after changing data
                #POP UP MSG SAYING CLICK CONFIRM FIRST
                messageBox = SettingConfirmPopup(self.window)
                if messageBox.getResult() == "Ignore Changes":
                    self.keySettingInfo.didUserIgnoreChanges = True #make ignore changes flag = T so the system won't detect revert keys as changed key
                    self.keySettingInfo.hasControlChanged = False
                    conSetting = self.controlSettingWidget

                    oldControlSetting = self.oldControlSetting
                    conSetting.resetControlToOldSetting(oldControlSetting)

                    featureWidgetClass = self.getSysClass(self.currentSys)

                    featureWidgetClass.resetFeatureToOldSetting(oldControlSetting)
                    self.keySettingInfo.didUserIgnoreChanges = False #reset ignore changes flag

                    #convert dropdown element back to changed value
                    for i, value in enumerate(MODELMAPPING):
                        if value == self.currentSys:
                            self.typeDropDown.setCurrentIndex(i)
                            break

                #GO BACK
                else:
                    
                    pass


                print(messageBox.getResult())
                pass

        else:
            #HIDE CURRENT, SHOW SELECTED SYSTEM INTERFACE
            currentSysBox = self.getModel(self.currentSys)
            currentSysBox[0].hide()
            currentSysBox[1].hide()
            self.currentSys = selectedModel



            #TODO reduce code by creating common code

            if not MODELSINITDICT[selectedModel]:
                #INITIALISE IF IT IS NOT INITIALISED
                self.chooseInit(selectedModel)

            newSysBox = self.getModel(selectedModel)
            newSysBox[0].show()
            newSysBox[1].show()

            #Read feature keys
            #--------------------------------------
            featureWidgetClass = self.getSysClass(self.currentSys)
        
            for key,value in featureWidgetClass.dictOfComboBox.items():
                comboBox = value.getComboBox()
                self.oldControlSetting[key] = comboBox.currentText()
            #------------------------------------------
        


    
    def confirmSettings(self):
        """
            Method for clicking on confirm setting button: saves
            the current setting to a yaml file
        """
        currentIndex = self.typeDropDown.currentIndex()
        selectedModel = MODELMAPPING[currentIndex]
        # gets current selected drone system
        #----------------------------------------------------------------------
        currentSelectedSys = self.currentSys
        currentSysClass = self.getSysClass(currentSelectedSys)
        currentControlSettings = self.controlSettingWidget.getCurrentControls()
        #----------------------------------------------------------------------

        currentSysBasedSettings = currentSysClass.getCurrentSettings()
        self.keySettingInfo.setUpdateControlSetting(currentControlSettings) #record the updated control setting
        self.yamlHelper.setSysBasedSettings(currentSysBasedSettings, currentSelectedSys)
        self.yamlHelper.setControlSettings(currentControlSettings)
        self.yamlHelper.writeSettings(selectedModel)


    def clickedConfirmBut(self):
        self.keySettingInfo.hasSetConfirmClicked = True
        #SAVE SETTING IN SETTING FILE
        self.confirmSettings()
        self.keySettingInfo.didUserIgnoreChanges = False #reset user ignore changes flag

        

    #FOR CAMERA COMPONENT
    #___________________________________________________________________________________
    def start(self):
        if not self.camThread.isRunning():

            # connect its signal to the update_image slot
            self.camThread.change_pixmap_signal.connect(self.update_image)
            # start the thread
            self.camThread.start()

        else:
            print("camera is already running")
            

    def stop(self):
        if self.camThread.isRunning():
            self.camThread.disconnect()

            self.camThread.stop()

        else:
            print("no camera is running")

    def connectToUpdateImage(self):
        """
            connect signal to update image function for the main page
        """
        self.camThread.disconnect()

        self.camThread.change_pixmap_signal.connect(self.update_image)

    def update_image(self, frame):
        """Updates the image_label with a new opencv image"""
        qtPix = self.camThread.convert_cv_qt_show(frame)
        #self.displayFrame.setPixmap(qt_img)

        # Scale the image to fit the pane then display
        targetWidth = self.displayFrame.width()
        targetHeight = self.displayFrame.height()
        self.displayFrame.setPixmap(
        qtPix.scaled(targetWidth, targetHeight, Qt.KeepAspectRatio)
        )

    def setCameraButtonStatus(self, status):
        """
            Disable/enable camera button
        """
        self.Start.setEnabled(status)
        self.Stop.setEnabled(status)
        
from PyQt5 import QtCore, QtWidgets
import string
from dictionary import *
from yamlHelper import YamlHelper
from keySettingClass import KeySettingsInfo



#availableKeys are all the keys that are available to set (letters+digits)
class ControlSettingWidget(QtWidgets.QWidget):
    def __init__(self, page, availableKeys, type, homeWidget=None, oldControlSetting=None, parent=None, yamlHelper:YamlHelper=None, keySettingInfo:KeySettingsInfo=None):
        QtWidgets.QWidget.__init__(self, parent=parent)
        self.controlSetVerticalLay = QtWidgets.QVBoxLayout()
        self.controlSetVerticalLay.setObjectName("controlSetVerticalLay")
        self.controlsSetLabel = QtWidgets.QLabel(page)
        self.controlsSetLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.controlsSetLabel.setObjectName("controlsSetLabel")
        self.controlSetVerticalLay.addWidget(self.controlsSetLabel)
        self.controlSetGrid = QtWidgets.QGridLayout()
        self.controlSetGrid.setObjectName("controlSetGrid")
        self.throttleSetDown = QtWidgets.QComboBox(page)
        self.throttleSetDown.setObjectName("throttleSetDown")
        self.controlSetGrid.addWidget(self.throttleSetDown, 0, 1, 1, 1)
        self.yawSetLabel = QtWidgets.QLabel(page)
        # self.yawSetLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.yawSetLabel.setObjectName("yawSetLabel")
        self.controlSetGrid.addWidget(self.yawSetLabel, 1, 0, 1, 1)
        self.yawSetAnticlockwise = QtWidgets.QComboBox(page)
        self.yawSetAnticlockwise.setObjectName("yawSetAnticlockwise")
        self.controlSetGrid.addWidget(self.yawSetAnticlockwise, 1, 1, 1, 1)
        self.rollSetLabel = QtWidgets.QLabel(page)
        # self.rollSetLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rollSetLabel.setObjectName("rollSetLabel")
        self.controlSetGrid.addWidget(self.rollSetLabel, 2, 0, 1, 1)
        self.throttleSetLabel = QtWidgets.QLabel(page)
        # self.throttleSetLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.throttleSetLabel.setObjectName("throttleSetLabel")
        self.controlSetGrid.addWidget(self.throttleSetLabel, 0, 0, 1, 1)
        self.pitchSetBack = QtWidgets.QComboBox(page)
        self.pitchSetBack.setObjectName("pitchSetBack")
        self.controlSetGrid.addWidget(self.pitchSetBack, 3, 1, 1, 1)
        self.pitchSetLabel = QtWidgets.QLabel(page)
        # self.pitchSetLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pitchSetLabel.setObjectName("pitchSetLabel")
        self.controlSetGrid.addWidget(self.pitchSetLabel, 3, 0, 1, 1)
        self.rollSetLeft = QtWidgets.QComboBox(page)
        self.rollSetLeft.setObjectName("rollSetLeft")
        self.controlSetGrid.addWidget(self.rollSetLeft, 2, 1, 1, 1)
        self.throttleSetUp = QtWidgets.QComboBox(page)
        self.throttleSetUp.setObjectName("throttleSetUp")
        self.controlSetGrid.addWidget(self.throttleSetUp, 0, 2, 1, 1)
        self.yawSetClockwise = QtWidgets.QComboBox(page)
        self.yawSetClockwise.setObjectName("yawSetClockwise")
        self.controlSetGrid.addWidget(self.yawSetClockwise, 1, 2, 1, 1)
        self.rollSetRight = QtWidgets.QComboBox(page)
        self.rollSetRight.setObjectName("rollSetRight")
        self.controlSetGrid.addWidget(self.rollSetRight, 2, 2, 1, 1)
        self.pitchSetFront = QtWidgets.QComboBox(page)
        self.pitchSetFront.setObjectName("pitchSetFront")
        self.controlSetGrid.addWidget(self.pitchSetFront, 3, 2, 1, 1)
        self.controlSetGrid.setColumnStretch(0, 1)
        self.controlSetGrid.setColumnStretch(1, 1)
        self.controlSetGrid.setColumnStretch(2, 1)
        self.controlSetVerticalLay.addLayout(self.controlSetGrid)
        self.controlSetVerticalLay.setStretch(1, 1)
        self.retranslateUi()
        self.setStyle()

        # self.oldControlSetting = oldControlSetting

        self.yamlHelper = yamlHelper
        self.keySettingInfo = keySettingInfo

        #CONTROL WIDGET IS AT SETTING PAGE
        if type == SETTING:
            self.addAllKeys(availableKeys)

            #READ FROM SETTING PAGE
            #controlDefault store the key as key and value as the combo box type string
            self.keySettingInfo.convertToKeyboardAsKey(self.yamlHelper.getControlSettings())
            controlDefaults = self.keySettingInfo.getControlDefaultKeys()
            print(f"controlDefaults: {controlDefaults}")
            self.setUserDefaultKeys(controlDefaults, availableKeys)
        
            self.initUpdateHomeControl(homeWidget)
            self.pitchSetFront.currentIndexChanged.connect(lambda: self.updateHomeControl(self.pitchSetFront.currentText(), homeWidget, PF))
            self.pitchSetBack.currentIndexChanged.connect(lambda: self.updateHomeControl(self.pitchSetBack.currentText(), homeWidget, PB))
            self.rollSetLeft.currentIndexChanged.connect(lambda: self.updateHomeControl(self.rollSetLeft.currentText(), homeWidget, RL))
            self.rollSetRight.currentIndexChanged.connect(lambda: self.updateHomeControl(self.rollSetRight.currentText(), homeWidget, RR))
            self.yawSetClockwise.currentIndexChanged.connect(lambda: self.updateHomeControl(self.yawSetClockwise.currentText(), homeWidget, YC))
            self.yawSetAnticlockwise.currentIndexChanged.connect(lambda: self.updateHomeControl(self.yawSetAnticlockwise.currentText(), homeWidget, YA))
            self.throttleSetDown.currentIndexChanged.connect(lambda: self.updateHomeControl(self.throttleSetDown.currentText(), homeWidget, TD))
            self.throttleSetUp.currentIndexChanged.connect(lambda: self.updateHomeControl(self.throttleSetUp.currentText(), homeWidget, TU))


    def initUpdateHomeControl(self, homeWidget):
        homeWidget.pitchSetFront.clear()
        homeWidget.pitchSetBack.clear()
        homeWidget.rollSetLeft.clear()
        homeWidget.rollSetRight.clear()
        homeWidget.yawSetClockwise.clear()
        homeWidget.yawSetAnticlockwise.clear()
        homeWidget.throttleSetDown.clear()
        homeWidget.throttleSetUp.clear()

        homeWidget.pitchSetFront.addItem(self.pitchSetFront.currentText())
        homeWidget.pitchSetBack.addItem(self.pitchSetBack.currentText())
        homeWidget.rollSetLeft.addItem(self.rollSetLeft.currentText())
        homeWidget.rollSetRight.addItem(self.rollSetRight.currentText())
        homeWidget.yawSetClockwise.addItem(self.yawSetClockwise.currentText())
        homeWidget.yawSetAnticlockwise.addItem(self.yawSetAnticlockwise.currentText())
        homeWidget.throttleSetDown.addItem(self.throttleSetDown.currentText())
        homeWidget.throttleSetUp.addItem(self.throttleSetUp.currentText())



    def updateHomeControl(self, currentData, homeWidget, boxType):

        print(f"self.keySettingInfo.didUserIgnoreChanges: {self.keySettingInfo.didUserIgnoreChanges}")
        #it will only become True when user ignore changes
        if not self.keySettingInfo.didUserIgnoreChanges:
            self.keySettingInfo.hasControlChanged = True
            self.keySettingInfo.hasSetConfirmClicked = False #TODO solve this

        #CLEAR THE HOME CONTROL COMBO BOX CONTENT
        currentHomeComboBox = self.getRelevantComboBox(boxType, homeWidget)

        if currentData:

            oldFunc = self.keySettingInfo.recordUsedKeys(currentData, boxType)
            if oldFunc is not None:
                oldComboBox = self.getRelevantComboBox(oldFunc)
                if isinstance(oldComboBox, str):
                    #PRINT OUT ERROR HERE?
                    #IGNORE 
                    return
                oldComboBox.setCurrentIndex(0) #set to ""
            
        # self.oldControlSetting[currentHomeComboBox] = currentHomeComboBox.currentText()
        currentHomeComboBox.clear()
        
        #THEN ADD THE CHANGED ITEM TO THE RELEVANT HOME PAGE
        currentHomeComboBox.addItem(currentData)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.controlsSetLabel.setText(_translate("MainWindow", "Controls"))
        self.yawSetLabel.setText(_translate("MainWindow", "Yaw"))
        self.rollSetLabel.setText(_translate("MainWindow", "Roll"))
        self.throttleSetLabel.setText(_translate("MainWindow", "Throttle"))
        self.pitchSetLabel.setText(_translate("MainWindow", "Pitch"))

        
    def getLayout(self):
        return self.controlSetVerticalLay

    
    def getRelevantComboBox(self, boxType, homeWidget=None):
        if homeWidget is None:
            if boxType == PF:
                return self.pitchSetFront

            elif boxType == PB:
                return self.pitchSetBack

            elif boxType == RL:
                return self.rollSetLeft

            elif boxType == RR:
                return self.rollSetRight

            elif boxType == TU:
                return self.throttleSetUp

            elif boxType == TD:
                
                return self.throttleSetDown

            elif boxType == YC:
                return self.yawSetClockwise

            elif boxType == YA:
                return self.yawSetAnticlockwise

            else:
                #PRINT OUT ERROR HERE?
                #IGNORE 
                return ""
        
        else:
            if boxType == PF:
                return homeWidget.pitchSetFront

            elif boxType == PB:
                return homeWidget.pitchSetBack

            elif boxType == RL:
                return homeWidget.rollSetLeft

            elif boxType == RR:
                return homeWidget.rollSetRight

            elif boxType == TU:
                return homeWidget.throttleSetUp

            elif boxType == TD:
                return homeWidget.throttleSetDown

            elif boxType == YC:
                return homeWidget.yawSetClockwise

            elif boxType == YA:
                return homeWidget.yawSetAnticlockwise

            else:
                #PRINT OUT ERROR HERE?
                #IGNORE 
                return ""



    def setStyle(self):
        self.pitchSetFront.setStyleSheet("QComboBox { combobox-popup: 0; }")
        self.pitchSetFront.setMaxVisibleItems(10)
        self.pitchSetBack.setStyleSheet("QComboBox { combobox-popup: 0; }")
        self.pitchSetBack.setMaxVisibleItems(10)
        self.yawSetClockwise.setStyleSheet("QComboBox { combobox-popup: 0; }")
        self.yawSetClockwise.setMaxVisibleItems(10)
        self.yawSetAnticlockwise.setStyleSheet("QComboBox { combobox-popup: 0; }")
        self.yawSetAnticlockwise.setMaxVisibleItems(10)
        self.rollSetLeft.setStyleSheet("QComboBox { combobox-popup: 0; }")
        self.rollSetLeft.setMaxVisibleItems(10)
        self.rollSetRight.setStyleSheet("QComboBox { combobox-popup: 0; }")
        self.rollSetRight.setMaxVisibleItems(10)
        self.throttleSetDown.setStyleSheet("QComboBox { combobox-popup: 0; }")
        self.throttleSetDown.setMaxVisibleItems(10)
        self.throttleSetUp.setStyleSheet("QComboBox { combobox-popup: 0; }")
        self.throttleSetUp.setMaxVisibleItems(10)

    def addAllKeys(self, availableKeys):
        self.pitchSetFront.addItem("")
        self.pitchSetBack.addItem("")
        self.rollSetLeft.addItem("")
        self.rollSetRight.addItem("")
        self.yawSetClockwise.addItem("")
        self.yawSetAnticlockwise.addItem("")
        self.throttleSetDown.addItem("")
        self.throttleSetUp.addItem("")
        for key in availableKeys:
            self.pitchSetFront.addItem(key)
            self.pitchSetBack.addItem(key)
            self.rollSetLeft.addItem(key)
            self.rollSetRight.addItem(key)
            self.yawSetClockwise.addItem(key)
            self.yawSetAnticlockwise.addItem(key)
            self.throttleSetDown.addItem(key)
            self.throttleSetUp.addItem(key)

    def setAppDefaultControlKeys(self):
        """
            To assign key using the default setting when there are no
            user setting available
        """
        self.pitchSetFront.setCurrentIndex(32+1) #SET AS w
        self.pitchSetBack.setCurrentIndex(28+1) #SET AS s
        self.rollSetLeft.setCurrentIndex(10+1) #SET AS a
        self.rollSetRight.setCurrentIndex(13+1) #SET AS d

        self.throttleSetUp.setCurrentIndex(18+1) #SET AS i
        self.throttleSetDown.setCurrentIndex(20+1) #SET AS k
        self.yawSetClockwise.setCurrentIndex(21+1) #SET AS l
        self.yawSetAnticlockwise.setCurrentIndex(19+1) #SET AS j


        self.keySettingInfo.recordAppDefaultControlKeys()

        
    def clearControlKeys(self):
        self.pitchSetFront.setCurrentIndex(0) #SET AS w
        self.pitchSetBack.setCurrentIndex(0) #SET AS s
        self.rollSetLeft.setCurrentIndex(0) #SET AS a
        self.rollSetRight.setCurrentIndex(0) #SET AS d

        self.throttleSetUp.setCurrentIndex(0) #SET AS i
        self.throttleSetDown.setCurrentIndex(0) #SET AS k
        self.yawSetClockwise.setCurrentIndex(0) #SET AS l
        self.yawSetAnticlockwise.setCurrentIndex(0) #SET AS j
        self.keySettingInfo.resetUsedKeys()
        

    def setUserDefaultKeys(self, controlDefaults, availableKeys):
        usedKeys = self.keySettingInfo.getUsedKeys() #list of keys as the dict key with value as the relevant combo box
        #WHEN DICT IS NOT EMPTY
        if not self.keySettingInfo.isUserSetDefault:
            self.setAppDefaultControlKeys()
            self.keySettingInfo.isUserSetDefault = False

        else:
            # listOfUsedKeys = usedKeys.keys() #get the list of used keys
            listOfUserKeys = controlDefaults.keys()
            #for each default key
            for userKey in listOfUserKeys:
                oldFunc = self.keySettingInfo.recordUsedKeys(userKey, controlDefaults[userKey])

                #controlDefault store the key as key and value as the combo box type string
                #available keys are empty string + letters + digits
                index = -1

                #when the user key is "", we use index = -1 so we can get empty string
                if userKey != "":
                    
                    #GETS THE INDEX OF THE KEY IN AVAILABLEKEYS
                    try:
                        index = availableKeys.index(userKey)

                    except Exception as e:
                        print(f"invalid key set, using empty string instead: {e}")

                currentComboBox = self.getRelevantComboBox(controlDefaults[userKey]) #gets the relavant dropdown list
                #return "" if it doesn't matches any combobox/dropdown list
                if isinstance(currentComboBox, str):
                    #PRINT OUT ERROR HERE?
                    #IGNORE 
                    raise Exception("element doesn't exist")

                    

                else:
                    if oldFunc is not None:
                        oldComboBox = self.getRelevantComboBox(oldFunc)
                        if isinstance(oldComboBox, str):
                            #PRINT OUT ERROR HERE?
                            #IGNORE 
                            raise Exception("element doesn't exist")
                        oldComboBox.setCurrentIndex(0)

                    #SINCE THE COMBO BOX IS POPULATED WITH AVAILABLEKEYS + "",
                    #THEY HAVE THE SAME ORDER
                    currentComboBox.setCurrentIndex(index+1)


    def resetControlToOldSetting(self, oldControlSetting):
        self.clearControlKeys()
        #GO THROUGH AVAILABLE KEY AND 
        availableKeys = self.keySettingInfo.availableKeys
        for boxType in CONTROLELEMENTSSTR:
            oldAssignedKey = oldControlSetting[boxType]
            element = self.getRelevantComboBox(boxType)
            if isinstance(element, str):
                raise Exception("element doesn't exist")

            element.setCurrentIndex(availableKeys.index(oldAssignedKey)+1)
            self.keySettingInfo.recordUsedKeys(oldAssignedKey, boxType)

                        
    def getCurrentControls(self):
        """
            returns the current control setting in a dict
        """
        controlSetting = {}
        controlSetting[PF] = self.pitchSetFront.currentText()
        controlSetting[PB] = self.pitchSetBack.currentText()
        controlSetting[RL] = self.rollSetLeft.currentText()
        controlSetting[RR] = self.rollSetRight.currentText()
        controlSetting[YC] = self.yawSetClockwise.currentText()
        controlSetting[YA] = self.yawSetAnticlockwise.currentText()
        controlSetting[TD] = self.throttleSetDown.currentText()
        controlSetting[TU] = self.throttleSetUp.currentText()
        return controlSetting

from PyQt5 import QtCore, QtWidgets
import string
from PyQt5.QtCore import Qt
from dictionary import *
from keySettingClass import KeySettingsInfo
from yamlHelper import YamlHelper
from functools import partial
from usefulFunctions import *

class ComboBoxWithLabel():
    def __init__(self, comboBoxName, boxWidget, parent=None):


        self.comboBox = QtWidgets.QComboBox(boxWidget)
        self.comboBox.setObjectName(comboBoxName)
        self.comboBoxLabel = QtWidgets.QLabel(boxWidget)
        self.comboBoxLabel.setObjectName(f"{comboBoxName}Label")
        self.retranslateUi(comboBoxName)

    def getComboBox(self):
        """
            To get the combo box
        """
        return self.comboBox
    
    def getComboBoxLabel(self):
        """
            To get the combo box label
        """
        return self.comboBoxLabel
    
    def retranslateUi(self, comboBoxName):
        _translate = QtCore.QCoreApplication.translate

        self.comboBoxLabel.setText(_translate("MainWindow", comboBoxName))
       

class SysBasedFeatureSettingWidget(QtWidgets.QWidget):
    """
        Class for displaying the system based feature settings
    """
    def __init__(self, page, keySettingInfo:KeySettingsInfo, yamlHelper:YamlHelper, droneSys, type=None, homeWidget=None, parent=None):
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

        #4 default combo box setting!
        #TODO show only the first 4 combobox settings with an extra button to show all feature settings
        #TODO read config file so we know which 4 combo box to show
        self.dictOfComboBox = {PREARM:ComboBoxWithLabel(PREARM, self.boxWidget),
                          ARM:ComboBoxWithLabel(ARM, self.boxWidget),
                          BEEPER:ComboBoxWithLabel(BEEPER, self.boxWidget),
                          OSD:ComboBoxWithLabel(OSD,self.boxWidget)}


        self.addFourComboBoxAndLabelsToBoxWidget() #add 4 combobox to box widget
        
        self.allModeSetLabel = QtWidgets.QLabel(self.boxWidget)
        self.allModeSetLabel.setObjectName("allModeSetLabel")
        self.allModeSetBut = QtWidgets.QPushButton(self.boxWidget)
        self.allModeSetBut.setObjectName("allModeSetBut")

        #add widget to the 5th row of box widget
        self.modeSetGrid.addWidget(self.allModeSetBut, 5, 1, 1, 1)
        self.modeSetGrid.addWidget(self.allModeSetLabel, 5, 0, 1, 1)

        
        self.modeSetVerticalLay.addLayout(self.modeSetGrid)
        self.modeSetVerticalLay.setStretch(1, 1)
        self.setStyle()

        self.keySettingInfo = keySettingInfo
        self.yamlHelper = yamlHelper
        availableKeys = self.keySettingInfo.getAvailableKeys()



        self.retranslateUi()

        #if the current widget is from the setting page, we fill the combo box
        #and track the key assignment
        if type == SETTING:
            self.fillValue(availableKeys)


            #READ FROM SETTING PAGE
            #controlDefault store the key as key and value as the combo box type string
            self.keySettingInfo.convertToKeyboardAsKeySysBased(self.yamlHelper.getSysBasedSettings(droneSys), droneSys, self.dictOfComboBox)
            featureDefaults = self.keySettingInfo.getSysBasedDefaultKeys(droneSys)
            self.setUserDefaultKeys(featureDefaults, availableKeys, droneSys)
        
            self.initUpdateHomeControl(homeWidget)

            #TODO only return the current text of last combobox element
            #reason: lambda function is parsed and compiled but not executed until we actually call the lambda function
            #keyword: Connecting multiples signal/slot in a for loop
            for key, value in self.dictOfComboBox.items():
                
                comboBox = value.getComboBox()

                #we supply the combobox here instead of the currenttext since we need to specify
                #a solid variable, if we use current text, it will only pass the inital value
                #and not the current text! So we need to supply the whole combobox and read the
                #current text
                comboBox.currentIndexChanged.connect(lambda _, currentComboBox=comboBox, widget=homeWidget, dictKey=key: self.updateHomeControl(currentComboBox, widget, dictKey))
                # comboBox.currentIndexChanged.connect(partial(self.updateHomeControl, comboBox.currentText, homeWidget, key))
 
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

        self.modeSetLabel.setText(_translate("MainWindow", "Modes/Features"))
        self.modeSetLabel.setStyleSheet(TITLESTYLE)
        self.allModeSetLabel.setText(_translate("MainWindow", "Additional Features Setting"))
        self.allModeSetBut.setText(_translate("MainWindow", "Additional Features Setting"))

    def initUpdateHomeControl(self, homeWidget):
        for key, value in homeWidget.dictOfComboBox.items():
            comboBox = value.getComboBox()
            comboBox.clear()
            comboBox.addItem(self.dictOfComboBox[key].getComboBox().currentText())

    def updateHomeControl(self, currentComboBox:QtWidgets.QComboBox, homeWidget, boxType):
        currentData = currentComboBox.currentText()

        #it will only become True when user ignore changes
        if not self.keySettingInfo.didUserIgnoreChanges:
            self.keySettingInfo.hasControlChanged = True
            self.keySettingInfo.hasSetConfirmClicked = False #TODO solve this
        
        #CLEAR THE HOME CONTROL COMBO BOX CONTENT
        currentHomeComboBox = self.getRelevantComboBox(boxType, homeWidget)

        self.checkForRepeatedKey(currentData, boxType)
            
        currentHomeComboBox.clear()
        
        #THEN ADD THE CHANGED ITEM TO THE RELEVANT HOME PAGE
        currentHomeComboBox.addItem(currentData)

    def addFourComboBoxAndLabelsToBoxWidget(self):
        """
            To add the main 4 features to be displayed in the setting page/home page
        """
        iteration = 0 #record the loop interation so we can place it at the correct row
        for key, value in self.dictOfComboBox.items():
            self.addSingleComboBoxAndLabelToBoxWidget(value, iteration)
            iteration +=1

    def addSingleComboBoxAndLabelToBoxWidget(self, comboInfo, row):
        """
            Add one comboBox to the box widget (widget that shows the 4 main key settings)
        """
        comboBox = comboInfo.getComboBox()
        comboBoxLabel = comboInfo.getComboBoxLabel()
        self.modeSetGrid.addWidget(comboBox, row, 1, 1, 1) #add comboBox
        self.modeSetGrid.addWidget(comboBoxLabel, row, 0, 1, 1) #add comboBox label

    def setStyle(self):
        """
            set the style of the combobox/dropdown menu
        """

        for key, value in self.dictOfComboBox.items():
            comboBox = value.getComboBox()
            comboBox.setStyleSheet("QComboBox { combobox-popup: 0; }")
            comboBox.setMaxVisibleItems(10)

    def getWidget(self):
        """
            return the container box containing the settings
        """
        return self.boxWidget
    
    
    def fillValue(self, availableKeys):
        """
            fill the dropdown menu options
        """


        for key, value in self.dictOfComboBox.items():
            comboBox = value.getComboBox()
            comboBox.addItem("")
            for key in availableKeys:
                comboBox.addItem(key)

    def getCurrentSettings(self):
        """
            return the current 4 main Betaflight based system
            features setting
        """
        currentSetting = {}
        for key, value in self.dictOfComboBox.items():
            comboBox = value.getComboBox()
            currentSetting[key] = comboBox.currentText()
        return currentSetting
    

    def checkForRepeatedKey(self, currentData, boxType):
        """
            To check for any repeated assigned key and make it as
            empty string.
        """

        if currentData:
            currentComboBox = self.getRelevantComboBox(boxType)
            oldFunc = self.keySettingInfo.recordUsedKeys(currentData, boxType, currentComboBox)
            #if it is not none, then there are repeated assigned key
            if oldFunc is not None:
                oldComboBox = self.keySettingInfo.getRelevantComboBox(oldFunc)
                if isinstance(oldComboBox, str):
                    #PRINT OUT ERROR HERE?
                    #IGNORE 
                    raise Exception("element doesn't exist")

                oldComboBox.setCurrentIndex(0) #set to ""



    def getRelevantComboBox(self, boxType, homeWidget=None):
        """
            To get the relevant combobox/dropdown list based
            on the provided box type / feature name
        """
        if homeWidget is None:
            for key, value in self.dictOfComboBox.items():
                if boxType == key:
                    return value.getComboBox()
                
        else:
            for key, value in homeWidget.dictOfComboBox.items():
                if boxType == key:
                    return value.getComboBox()
            
        
        return ""
    

    def setAppDefaultSysBasedKey(self, droneSys):
        """
            To assign key using the default setting when there are no
            user setting available
        """
        print("inside default")
        i = 0
        #loop through the dict containing the combo boxes
        for _,value in self.dictOfComboBox.items():
            box = value.getComboBox()

            #use 0-9 first
            if i < 10:
                box.setCurrentIndex(i+1)

            #use z,x,c,v,b,n,m if all the digits are used
            else:
                alphaKeys = ALPHAKEY.copy()
                try:
                    key = alphaKeys.pop(0)
                    index = self.keySettingInfo.availableKeys.index(key)
                    
                    box.setCurrentIndex(index+1)

                except Exception as e:
                    print(f"ran out of preset keys, making it as empty string: {e}")

            i +=1

        self.keySettingInfo.recordAppDefaultSysBasedFeaturesKeys(self.dictOfComboBox)


    def setUserDefaultKeys(self, controlDefaults, availableKeys, droneSys):
        """
            To set user default keys if there are user settings
            in the config file, otherwise use the system default
            setting
        """
        
        #WHEN THERE ARE NO USER SETTINGS IN THE CONFIG FILE
        status = None
        try:
            status = self.keySettingInfo.isUserSetDefaultFeature[droneSys]
        except:
            status = False
        
        if not status:
            self.setAppDefaultSysBasedKey(droneSys)
            self.keySettingInfo.isUserSetDefaultFeature[droneSys] = False #reset flag

        else:
            listOfUserKeys = controlDefaults.keys()
            #for each default key
            for userKey in listOfUserKeys:
                currentComboBox = self.getRelevantComboBox(controlDefaults[userKey])
                oldFunc = self.keySettingInfo.recordUsedKeys(userKey, controlDefaults[userKey], currentComboBox)

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

    def clearFeatureKeys(self):
        """
            Clear the assigned keys
        """
        for key, value in self.dictOfComboBox.items():
            comboBox = value.getComboBox()
            comboBox.setCurrentIndex(0) #set as ""

        self.keySettingInfo.resetUsedKeys()

    def resetFeatureToOldSetting(self, oldFeatureSetting):
        """
            Resets the feature key assignment seeting
            to old setting (when user decides to ignore changes)
        """
        self.clearFeatureKeys()
        #GO THROUGH AVAILABLE KEY AND 
        availableKeys = self.keySettingInfo.availableKeys
        for key, value in self.dictOfComboBox.items():
            
            oldAssignedKey = oldFeatureSetting[key]
            element = value.getComboBox()

            index = -1
            if oldAssignedKey != "":

                index = availableKeys.index(oldAssignedKey)

            element.setCurrentIndex(index+1)

            self.keySettingInfo.recordUsedKeys(oldAssignedKey, key, element)

    def getAllComboBoxes(self):
        """
            Returns all the combo box for the current widget
            using the dict format {key:combobox}
        """
        dictCombo = {}
        for key, value in self.dictOfComboBox.items():
            dictCombo[key] = value.getComboBox()
        return dictCombo
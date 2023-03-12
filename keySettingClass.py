from dictionary import *
import string

#TODO allow user to dynamically add drone system + feature instead of hardcoding them

class KeySettingsInfo():
    """
        Stores the information relating to 
        key assignment setting
    """
    def __init__(self):
        
        self.usedKeys = {} #to store the used keys
        self.defaultControlKeyAsKey = {} #to store the default control setting when we first load the app
        self.defaultSysBasedKeyAsKey = {} #to store the default sys based feature setting when we first load the app
        self.isUserSetDefault = False #flag to indicate whether the default setting is set by the user or not
        self.didUserIgnoreChanges = False #flag to indicate whether users have ignore new changes in the setting page
        self.hasControlChanged = False #flag to indicate whether settings have been changed or not in the setting [age]
        self.hasSetConfirmClicked = False #flag to indicate whetehr users have clicked save setting button
        self.isUserSetDefaultFeature = {} #dict containing flag for different drone system based feature setting to indicate whether the default setting is set by the user or not

        self.allSettingComboBox = {}

        self.updatedControlSetting = {}
        letters = string.ascii_lowercase
        digits = string.digits
        self.availableKeys = digits + letters 

    def setUpdateControlSetting(self, currentControlSettings):
        """
            To record the updated key control setting
        """
        self.updatedControlSetting = {y: x for x, y in currentControlSettings.items()}

    def getUpdateControlSetting(self):
        """
            Return first load up control setting if user didn't
            changed the settings or return the updated settings
        """
        if self.updatedControlSetting:
            return self.updatedControlSetting
        
        else:
            return self.defaultControlKeyAsKey

    def convertToKeyboardAsKey(self, defaultKeysFromYaml):
        """
            Switch dict value as key and key as dict value
        """
        self.defaultControlKeyAsKey = {y: x for x, y in defaultKeysFromYaml.items()}
        if not self.defaultControlKeyAsKey:
            self.defaultControlKeyAsKey["w"] = PF
            self.defaultControlKeyAsKey["s"] = PB
            self.defaultControlKeyAsKey["a"] = RL
            self.defaultControlKeyAsKey["d"] = RR
            self.defaultControlKeyAsKey["i"] = TU
            self.defaultControlKeyAsKey["k"] = TD
            self.defaultControlKeyAsKey["j"] = YC
            self.defaultControlKeyAsKey["l"] = YA
            #add default keys for other items here
        else:
            self.isUserSetDefault = True


    def convertToKeyboardAsKeySysBased(self, defaultKeysFromYaml, boxType, comboBoxDict):
        """
            Switch dict value as key and key as dict value
        """
        self.defaultSysBasedKeyAsKey[boxType] = {y: x for x, y in defaultKeysFromYaml.items()}
        
        if not self.defaultSysBasedKeyAsKey[boxType]:
            i = 0
            alphaKeys = ALPHAKEY.copy()
            for comboBoxLabel, value in comboBoxDict.items():
                if i < 10:
                    self.recordUsedKeys(str(i), comboBoxLabel, value.getComboBox())
                    i+=1
                else:
                    try:
                        key = alphaKeys.pop(0)
                        self.recordUsedKeys(key, comboBoxLabel, value.getComboBox())

                    except Exception as e:
                        print(f"ran out of preset keys, making it as empty string: {e}")

            #add default keys for other items here
        else:
            print('NONONONNO')
            self.isUserSetDefaultFeature[boxType] = True
    


    def recordUsedKeys(self, usedKey, keyFunction, comboBox):
        """
            record a used key and return the old key function if the key has already been used
            before
        """
        returnValue = None #if the returned value is not none, then we return the old keyFunction and change that function to empty.
        if usedKey in self.usedKeys.keys():
            returnValue = self.usedKeys[usedKey] if self.usedKeys[usedKey] != keyFunction else None
        self.usedKeys[usedKey] = keyFunction #change/add key & value pair
        self.allSettingComboBox[keyFunction] = comboBox
        return returnValue
    
    def getComboBox(self, funcName):
        try:
            return self.allSettingComboBox[funcName]
        
        except:
            return ""

    def removeUsedKeys(self, usedKey):
        """
            remove a used key when user selects a different key
        """

        try:
            del self.usedKeys[usedKey]

        except Exception as e:
            print(f"current key is not used:{e}")

    def getUsedKeys(self):
        """
            return the used keys
        """
        return self.usedKeys
    
    def getAvailableKeys(self):
        """
            return the not allocated keys
        """
        return self.availableKeys

    def recordAppDefaultControlKeys(self, comboBoxDict):
        """
            record app default used key for controls
        """        

        self.recordUsedKeys('w',PF, comboBoxDict[PF])
        self.recordUsedKeys('s',PB, comboBoxDict[PB])
        self.recordUsedKeys('a',RL, comboBoxDict[RL])
        self.recordUsedKeys('d',RR, comboBoxDict[RR])
        self.recordUsedKeys('i',TU, comboBoxDict[TU])
        self.recordUsedKeys('k',TD, comboBoxDict[TD])
        self.recordUsedKeys('l',YC, comboBoxDict[YC])
        self.recordUsedKeys('j',YA, comboBoxDict[YA])


    def recordAppDefaultSysBasedFeaturesKeys(self, comboBoxDict):
        """
            record app default used key for sys based
            features
        """
        i = 0
        alphaKeys = ALPHAKEY.copy()
        for key, value in comboBoxDict.items():
            sysBasedFeature = key
            comboBox = value.getComboBox()
            if i < 10:
                self.recordUsedKeys(str(i), sysBasedFeature, comboBox)
                i+=1
            else:
                try:
                    key = alphaKeys.pop(0)
                    self.recordUsedKeys(key, sysBasedFeature, comboBox)

                except Exception as e:
                    print(f"ran out of preset keys, making it as empty string: {e}")


    def getControlDefaultKeys(self):
        """
            returns the default key for control
            with the assigned key as the dict key
            and combobox/dropdown menu type as the value
        """
        return self.defaultControlKeyAsKey
    
    def getSysBasedDefaultKeys(self, boxType):
        """
            returns the default key for drone system based features
            with the assigned key as the dict key
            and combobox/dropdown menu type as the value
        """
        try:
            return self.defaultSysBasedKeyAsKey[boxType]
        
        except:
            return {}
    
    def resetUsedKeys(self):
        """
            reset used keys
        """
        self.usedKeys = {}

    def resetControlDefaultKeys(self):
        """
            reset control default keys
        """
        self.defaultControlKeyAsKey = {}

    def resetSysBasedDefaultKeys(self, boxType):
        """
            reset drone sys based features default keys 
        """
        self.defaultSysBasedKeyAsKey[boxType] = {}

    def getAllComboBox(self, controlWidget, featureWidget):
        """
            To get the relevant combo box from all combo boxes for key settings
        """
        allComboBoxDict = {}

        controlComboBoxDict = controlWidget.getAllComboBoxes()
        featureComboBoxDict = featureWidget.getAllComboBoxes()
        allComboBoxDict = {**controlComboBoxDict, **featureComboBoxDict}
        self.allSettingComboBox = allComboBoxDict

    def getRelevantComboBox(self,boxfunc):
        comboBox = self.allSettingComboBox[boxfunc]
        return comboBox

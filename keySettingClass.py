from dictionary import *
import string

#TODO allow user to dynamically add drone system + feature instead of hardcoding them

class KeySettingsInfo():
    def __init__(self):
        
        self.usedKeys = {}
        self.defaultControlKeyAsKey = {}
        self.defaultSysBasedKeyAsKey = {}
        self.isUserSetDefault = False
        self.didUserIgnoreChanges = False
        self.hasControlChanged = False
        self.hasSetConfirmClicked = False

        letters = string.ascii_lowercase
        digits = string.digits
        self.availableKeys = digits + letters 

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


    def convertToKeyboardAsKeySysBased(self, defaultKeysFromYaml, boxType):
        """
            Switch dict value as key and key as dict value
        """
        self.defaultSysBasedKeyAsKey[boxType] = {y: x for x, y in defaultKeysFromYaml.items()}
        if not self.defaultSysBasedKeyAsKey:
            i = 0
            alphaKeys = ALPHAKEY.copy()
            for sysBasedFeature in SYSBASEDELEMENTSSTR:
                if i < 10:
                    self.recordUsedKeys(str(i), sysBasedFeature)
                    i+=1
                else:
                    try:
                        key = alphaKeys.pop(0)
                        self.recordUsedKeys(key, sysBasedFeature)

                    except Exception as e:
                        print(f"ran out of preset keys, making it as empty string: {e}")

            #add default keys for other items here
        else:
            self.isUserSetDefault = True
    


    def recordUsedKeys(self, usedKey, keyFunction):
        """
            record a used key and return the old key function if the key has already been used
            before
        """
        print(keyFunction)
        returnValue = None #if the returned value is not none, then we return the old keyFunction and change that function to empty.
        if usedKey in self.usedKeys.keys():
            returnValue = self.usedKeys[usedKey] if self.usedKeys[usedKey] != keyFunction else None
        self.usedKeys[usedKey] = keyFunction #change/add key & value pair
        print(returnValue)

        return returnValue

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

    def recordAppDefaultControlKeys(self):
        """
            record app default used key for controls
        """        

        self.recordUsedKeys('w',PF)
        self.recordUsedKeys('s',PB)
        self.recordUsedKeys('a',RL)
        self.recordUsedKeys('d',RR)
        self.recordUsedKeys('i',TU)
        self.recordUsedKeys('k',TD)
        self.recordUsedKeys('l',YC)
        self.recordUsedKeys('j',YA)


    def recordAppDefaultSysBasedFeaturesKeys(self, boxType):
        """
            record app default used key for sys based
            features
        """
        i = 0
        alphaKeys = ALPHAKEY.copy()
        for sysBasedFeature in SYSBASEDELEMENTSSTR:
            if i < 10:
                self.recordUsedKeys(str(i), sysBasedFeature)
                i+=1
            else:
                try:
                    key = alphaKeys.pop(0)
                    self.recordUsedKeys(key, sysBasedFeature)

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

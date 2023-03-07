import yaml
import os

class YamlHelper():
    
    def __init__(self):
        self.currentWorkingDir = os.getcwd()
        self.defaultSysBasedSettings = {} #stores the updated setting
        self.appSettings = {}
        self.allSettings = {} #stores the setting from yaml file/updated when setting is saved into a file
        self.readFromYamlFile()
        self.defaultControlSettings = {}
        try:
            self.defaultControlSettings = self.allSettings['control'] #stores the updated setting

        except Exception as e:
            print(e)
            self.defaultControlSettings = {}

    def writeSettings(self, selectedSys):
        """
            write setting to a file using yaml format
        """
        with open(f"{self.currentWorkingDir}/user_settings.yaml", "w") as file:
            #only add data into yaml if setting is not empty
            #update setting
            if self.defaultControlSettings:
                self.allSettings["control"] = self.defaultControlSettings
            if self.defaultSysBasedSettings:
                self.allSettings[selectedSys] = self.defaultSysBasedSettings[selectedSys]
            if self.appSettings:
                self.allSettings["app"] = self.appSettings
            yaml.dump(self.allSettings, file)
    
    def readFromYamlFile(self):
        """
            read setting from user config file
        """
        try:
            with open(f"{self.currentWorkingDir}/user_settings.yaml", "r") as file:
                self.allSettings = yaml.safe_load(file)
                print(f"self.allSettings: {self.allSettings}")

            try:
                self.defaultControlSettings = self.allSettings['control']

            except Exception as e:
                print(f"no control settings from user config file: {e}")
                self.defaultControlSettings = {}

            try:
                self.defaultSysBasedSettings['Betaflight'] = self.allSettings['Betaflight']

            except Exception as e:
                print(f"no feature settings from user config file: {e}")
                self.defaultSysBasedSettings['Betaflight'] = {}

        except Exception as e:
            print(f"failed to read from config file: {e}")
            self.allSettings = {}

    def setControlSettings(self, controlSettings):
        """
            record the control key settings
        """
        self.defaultControlSettings = controlSettings

    def setSysBasedSettings(self, sysBasedSettings, selectedSys):
        """
            record the drone system based key settings
        """
        self.defaultSysBasedSettings[selectedSys] = sysBasedSettings

    def getControlSettings(self):
        """
            return the default control settings
        """
        return self.defaultControlSettings
    
    def getFeatureSettings(self, sysType):
        """
            return the default feature settings
            for sysType based drone system
        """

        #tries to get the information
        try:
            return self.defaultSysBasedSettings[sysType]

        except:
            return {}

    def getSysBasedSettings(self, selectedSys):
        """
            return the drone sys based setting
        """
        #tries to get the information
        try:
            return self.allSettings[selectedSys]
        except:
            return {}
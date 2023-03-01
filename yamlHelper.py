import yaml
import os

class YamlHelper():
    
    def __init__(self):
        self.currentWorkingDir = os.getcwd()
        self.defaultControlSettings = {}
        self.defaultSysBasedSettings = {}
        self.appSettings = {}
        self.allSettings = {}


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
                self.allSettings[selectedSys] = self.defaultSysBasedSettings
            if self.appSettings:
                self.allSettings["app"] = self.appSettings
            yaml.dump(self.allSettings, file)
    
    def readFromYamlFile(self):
        """
            read setting from user config file
        """
        try:

            with open(f"{self.currentWorkingDir}/user_settings.yaml", "w") as file:
                self.allSettings = yaml.load(file, yaml.full_load)
                

        except Exception as e:
            print(f"failed to read from config file: {e}")
            self.allSettings = {}

    def setControlSettings(self, controlSettings):
        """
            record the control key settings
        """
        self.defaultControlSettings = controlSettings

    def setSysBasedSettings(self, sysBasedSettings):
        """
            record the drone system based key settings
        """
        self.defaultSysBasedSettings = sysBasedSettings
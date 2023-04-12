from pynput import keyboard
import PyQt5.QtWidgets as QtWidgets
from PyQt5.QtCore import pyqtSignal, QThread
from dictionary import *

class TrackKeyClass(QThread):
    featureChanged = pyqtSignal(str,bool)

    def __init__(self, joystickLeft, joystickRight, keySettingInfo=None):
        super().__init__()

        self.isTracking = False
        self.keySettingInfo = keySettingInfo
        self.joystickLeft = joystickLeft
        self.joystickRight = joystickRight
        self.featureStatusDict = self.initFeatureValue()

    def on_press(self, key):
        """
            On key press
        """

        currentControlSetting = self.keySettingInfo.getUpdateControlSetting()
        currentFeatureSetting = self.keySettingInfo.getUpdatedDroneFeaturesSetting()
        reservedKeyDict = self.keySettingInfo.getReservedKey()

        control = None

        #momentary key event
        try:
            feature = currentFeatureSetting[key.char]
            if feature == PREARM:
                self.featureStatusDict[feature] = True
                self.featureChanged.emit(feature, self.featureStatusDict[feature])

                return#function has completed!

        except Exception as e:
            print(f"not momentary key: {e}")


        #control key event
        try:
            #check for whether joystick is enabled or not
            if self.joystickLeft.isEnabled() or self.joystickRight.isEnabled():


                control = currentControlSetting[key.char] #TODO prob for special key like ctrl

                print(f'alphanumeric key {key.char} pressed, function = {control}')


                #TODO call function here to move joystick
                self.joystickLeft.moveJoystick(control)

                self.joystickRight.moveJoystick(control)

                #receive changed data here and send out command
            else:
                print("joystick is not enabled")
        
            
        except Exception as e:
            print(f"not control key: {e}")

        try:

            
            feature = currentFeatureSetting[key.char]
            
            # if the key pressed is for arming the drone
            # we need to check whether it's prearmed first or not
            if feature==ARM:
                if self.featureStatusDict[PREARM] != True and self.featureStatusDict[feature] != True:
                    raise Exception("You need to enable prearm first!")
                

            self.featureStatusDict[feature] = not self.featureStatusDict[feature]
            
            # if the drone is armed, we enable the joystick widgets
            # else otherwise
            if self.featureStatusDict[ARM]:
                self.joystickLeft.setEnabled(True)
                self.joystickRight.setEnabled(True)
            else:
                self.joystickLeft.setEnabled(False)
                self.joystickRight.setEnabled(False)
            print(f'alphanumeric key {key.char} pressed, function = {feature}')
            #send out command here
            print({feature:self.featureStatusDict[feature]})
            self.featureChanged.emit(feature, self.featureStatusDict[feature]) #emit signal for updating status ocpm

        except Exception as e:
            print(f"not feature key: {e}")

        #reserved key event
        try:
            self.joystickLeft.reservedKeyEvent(reservedKeyDict, key.char)
            self.joystickRight.reservedKeyEvent(reservedKeyDict, key.char)

            #receive value here and send out command

        except Exception as e:
            print(f"error in reserved key: {e}")


    def on_release(self, key):
        """
            on key release
        """
        print('{0} released'.format(
            key))
        
        currentFeatureSetting = self.keySettingInfo.getUpdatedDroneFeaturesSetting()

        #momentary key event for key release
        try:
            feature = currentFeatureSetting[key.char]
            if feature == PREARM:
                self.featureStatusDict[feature] = False
                self.featureChanged.emit(feature, self.featureStatusDict[feature])

                return#function has completed!

        except Exception as e:
            print(f"not momentary key: {e}")
        
    def initFeatureValue(self):
        currentFeatureSetting = self.keySettingInfo.getUpdatedDroneFeaturesSetting()
        featureDict = {}

        for key, value in currentFeatureSetting.items():
            featureDict[value] = False

        return featureDict

    def start(self):
        """
            Start tracking key
        """
        self.isTracking = True
        self.listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release)
        self.listener.start()


    def stop(self):
        """
            Stop tracking key
        """
        self.isTracking = False
        self.listener.stop()
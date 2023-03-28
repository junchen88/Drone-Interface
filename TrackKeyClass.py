from pynput import keyboard
import PyQt5.QtWidgets as QtWidgets

class TrackKeyClass():
    
    def __init__(self, joystickLeft, joystickRight, keySettingInfo=None):
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

        #control key event
        try:

            control = currentControlSetting[key.char] #TODO prob for special key like ctrl

            print(f'alphanumeric key {key.char} pressed, function = {control}')


            #TODO call function here to move joystick
            self.joystickLeft.moveJoystick(control)

            self.joystickRight.moveJoystick(control)

            #receive changed data here and send out command
        
            
        except Exception as e:
            print(f"not control key: {e}")

        try:

            feature = currentFeatureSetting[key.char]
            self.featureStatusDict[feature] = not self.featureStatusDict[feature]
            print(f'alphanumeric key {key.char} pressed, function = {feature}')
            #send out command here
            print({feature:self.featureStatusDict[feature]})

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
        if key == keyboard.Key.esc:
            # Stop listener
            return False
        
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
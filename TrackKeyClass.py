from pynput import keyboard
import PyQt5.QtWidgets as QtWidgets

class TrackKeyClass():
    
    def __init__(self, joystickLeft, joystickRight, keySettingInfo=None):
        self.isTracking = False
        self.keySettingInfo = keySettingInfo
        self.joystickLeft = joystickLeft
        self.joystickRight = joystickRight

    def on_press(self, key):
        """
            On key press
        """

        currentControlSetting = self.keySettingInfo.getUpdateControlSetting()
        reservedKeyDict = self.keySettingInfo.getReservedKey()

        control = None

        #control key event
        try:
            print(f'alphanumeric key {key.char} pressed, function = {control}')

            control = currentControlSetting[key.char] #TODO prob for special key like ctrl

            #TODO call function here to move joystick
            self.joystickLeft.moveJoystick(control)

            self.joystickRight.moveJoystick(control)
        
            
        except Exception as e:
            print(f"error: {e}")

        #reserved key event
        try:
            self.joystickLeft.reservedKeyEvent(reservedKeyDict, key.char)
            self.joystickRight.reservedKeyEvent(reservedKeyDict, key.char)

        except Exception as e:
            print(f"error: {e}")


    def on_release(self, key):
        """
            on key release
        """
        print('{0} released'.format(
            key))
        if key == keyboard.Key.esc:
            # Stop listener
            return False

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
from pynput import keyboard
from newControlWindowClass import NewControlWindow
import PyQt5.QtWidgets as QtWidgets

class TrackKeyClass():
    
    def __init__(self, keySettingInfo=None):
        self.isTracking = False
        self.keySettingInfo = keySettingInfo
        self.controlWindow = None

    def on_press(self, key):
        """
            On key press
        """

        currentControlSetting = self.keySettingInfo.getUpdateControlSetting()
        reservedKeyDict = self.keySettingInfo.getReservedKey()

        control = None

        #get left and right joystick components
        joystickLeft = self.controlWindow.centralwidget.findChild(QtWidgets.QWidget, "left-joystick-widget")
        joystickRight = self.controlWindow.centralwidget.findChild(QtWidgets.QWidget, "right-joystick-widget")

        #control key event
        try:
            print(f'alphanumeric key {key.char} pressed, function = {control}')

            control = currentControlSetting[key.char] #TODO prob for special key like ctrl

            #TODO call function here to move joystick
            joystickLeft.moveJoystick(control)

            joystickRight.moveJoystick(control)
        
            
        except Exception as e:
            print(f"error: {e}")

        #reserved key event
        try:
            joystickLeft.reservedKeyEvent(reservedKeyDict, key.char)
            joystickRight.reservedKeyEvent(reservedKeyDict, key.char)

        except Exception as e:
            print(f"error: {e}")


    def on_release(self, key):
        print('{0} released'.format(
            key))
        if key == keyboard.Key.esc:
            # Stop listener
            return False

    def start(self, controlWindow:NewControlWindow):
        self.isTracking = True
        self.listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release)
        self.listener.start()

        self.controlWindow = controlWindow #create new control window

    def stop(self):
        self.isTracking = False
        self.listener.stop()
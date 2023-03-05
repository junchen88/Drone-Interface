from pynput import keyboard

class TrackKeyClass():
    
    def __init__(self, keySettings=None):
        self.isTracking = False
        self.keySettings = keySettings

    def on_press(self, key):
        try:
            print('alphanumeric key {0} pressed'.format(
                key.char))
            #TODO check for key here and do work
        except AttributeError:
            print('special key {0} pressed'.format(
                key))

    def on_release(self, key):
        print('{0} released'.format(
            key))
        if key == keyboard.Key.esc:
            # Stop listener
            return False

    def start(self):
        self.isTracking = True
        self.listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release)
        self.listener.start()

    def stop(self):
        self.isTracking = False
        self.listener.stop()
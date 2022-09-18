import sys
from Controls import *


class MainApp():

    def __init__(self, args):
        self.app = QtWidgets.QApplication(args)
        self.window = QtWidgets.QMainWindow()
        self.ui = Controls(self.window)
        self.window.show()
        sys.exit(self.app.exec_())


if __name__ == "__main__":
   MainApp(sys.argv)

from PyQt5.QtCore import pyqtSignal, QThread
import numpy as np

##IF USING VMWARE, NEED TO MAKE USB CONTROLLER AS 3.0

class QThreadClass(QThread):

    change_pixmap_signal = pyqtSignal(np.ndarray)


    def __init__(self):
        super().__init__()
        self.isWorkerRunning = True
        self.currentFunction = None

    def isRunning(self):
        return self.isWorkerRunning

    def setCurrentFunction(self, function):
        self.currentFunction = function

    def run(self):
        self.isWorkerRunning = True #change running status to true
        self.currentFunction(self)

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self.isWorkerRunning = False #change running status to false
        print("exit!")
        self.exit()

    
        

        
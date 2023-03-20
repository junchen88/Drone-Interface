
from PyQt5.QtCore import pyqtSignal, QThread
import numpy as np
import cv2
from PyQt5.QtGui import QPixmap, QImage


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
        print("exit thread!")
        self.exit()

    def convert_cv_qt_show(self, frame):
        """Convert from an opencv image to QPixmap"""
        
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        height, width, depth = rgb_image.shape
        if depth != 3:
            raise ValueError("Ui_ControlGui: Expected frame in RGB888 format")

        # Construct the showable pixel data
        bytesPerRow = 3 * width
        
        qtImg = QImage(rgb_image.data, width, height, bytesPerRow, QImage.Format_RGB888)
        qtPix = QPixmap(qtImg)

        return qtPix
    
        

        

import sys
import cv2
from PyQt5.QtCore import pyqtSignal, QThread
import numpy as np

##IF USING VMWARE, NEED TO MAKE USB CONTROLLER AS 3.0

class videoStreamThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def __init__(self):
        super().__init__()
        self.isRunning = True

    def isRunning(self):
        return self.isRunning

    def run(self):
        # 0 IS FOR THE PRIMARY CAMERA DEVICE
        self.isRunning = True #change running status to true
        cap = cv2.VideoCapture(0)
        while self.isRunning:
            status, frame = cap.read()
            if status:
                self.change_pixmap_signal.emit(frame)
        # shut down capture system
        cap.release()

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self.isRunning = False #change running status to false
        self.exit()

    
        

        
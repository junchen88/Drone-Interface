from test import *
import webCamQThreadClass
import cv2
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt



class Controls(Ui_MainWindow):
    def __init__(self, mainWindowBase):
        Ui_MainWindow.setupUi(self, mainWindowBase)

        self.Start.clicked.connect(self.start)
        self.Stop.clicked.connect(self.stop)

        # create the video capture thread
        self.thread = webCamQThreadClass.videoStreamThread()
        # connect its signal to the update_image slot
        self.thread.change_pixmap_signal.connect(self.update_image)
        # start the thread
        self.thread.start()


    def start(self):
        if not self.thread.isRunning:
            # create the video capture thread
            self.thread = webCamQThreadClass.videoStreamThread()
            # connect its signal to the update_image slot
            self.thread.change_pixmap_signal.connect(self.update_image)
            # start the thread
            self.thread.start()

        else:
            print("camera is already running")
            

    def stop(self):
        if self.thread.isRunning:
            self.thread.stop()

        else:
            print("no camera is running")


    def update_image(self, frame):
            """Updates the image_label with a new opencv image"""
            qt_img = self.convert_cv_qt_show(frame)
            #self.displayFrame.setPixmap(qt_img)
        
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

        # Scale the image to fit the pane then display
        targetWidth = self.displayFrame.width()
        targetHeight = self.displayFrame.height()
        self.displayFrame.setPixmap(
            qtPix.scaled(targetWidth, targetHeight, Qt.KeepAspectRatio)
        )


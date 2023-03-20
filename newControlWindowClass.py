from PyQt5 import QtCore, QtGui, QtWidgets
from joystick import JoystickWidget
import QThreadClass
import usefulFunctions as uf
from PyQt5.QtCore import Qt, pyqtSignal
import time
from TrackKeyClass import TrackKeyClass

class NewControlWindow(QtWidgets.QMainWindow):
    closed = pyqtSignal() #signal for closed window
    def __init__(self, camThread, keySettingInfo):
        super(NewControlWindow, self).__init__() #init QMainWIndow and self is the window here
        self.setObjectName("controlWindow")
        self.resize(1047, 626)
        self.setAutoFillBackground(False)
        
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")

        self.centralWidgetGrid = QtWidgets.QGridLayout(self.centralwidget)
        self.centralWidgetGrid.setObjectName("centralWidgetGrid")
        self.controlWindowHorizontalLay = QtWidgets.QHBoxLayout()
        self.controlWindowHorizontalLay.setObjectName("controlWindowHorizontalLay")
        
        self.joystickGrid = QtWidgets.QGridLayout()
        self.joystickGrid.setObjectName("joystickGrid")

        self.joystickWidgetLeft = JoystickWidget("Left")
        self.joystickWidgetRight = JoystickWidget("Right")
        self.joystickWidgetLeft.setObjectName("left-joystick-widget")
        self.joystickWidgetRight.setObjectName("right-joystick-widget")

        self.joystickGrid.addWidget(self.joystickWidgetLeft,1,0,1,1)
        self.joystickGrid.addWidget(self.joystickWidgetRight,1,1,1,1)

        self.trackKeyThread = TrackKeyClass(self.joystickWidgetLeft, self.joystickWidgetRight, keySettingInfo)
        self.trackKeyThread.start() #start tracking key
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.centralWidgetGrid.addItem(spacerItem, 0,0,1,1)
        self.controlWindowHorizontalLay.addLayout(self.joystickGrid)
        self.centralWidgetGrid.addLayout(self.controlWindowHorizontalLay, 0,1,1,1)
        
        self.camThread = camThread
        self.displayFrame = QtWidgets.QLabel()
        self.displayFrame.setStyleSheet("")
        self.displayFrame.setText("")
        self.displayFrame.setObjectName("newDisplayFrame")
        self.displayFrame.setMinimumSize(1, 1)
        self.centralWidgetGrid.addWidget(self.displayFrame, 0,0,1,1)


        # connect its signal to the new window update_image slot
        try:
            self.camThread.disconnect()
        
        except Exception as e:
            print(f"camera is not displayed, so no need to connect the signal slot: {e}")
        self.camThread.change_pixmap_signal.connect(self.update_image)


        self.setCentralWidget(self.centralwidget)

        
        self.show()

    
    def update_image(self, frame):
        """Updates the image_label with a new opencv image"""
        qtPix = self.camThread.convert_cv_qt_show(frame)
        #self.displayFrame.setPixmap(qt_img)

        # Scale the image to fit the pane then display
        targetWidth = self.displayFrame.width()
        targetHeight = self.displayFrame.height()
        self.displayFrame.setPixmap(
        qtPix.scaled(targetWidth, targetHeight, Qt.KeepAspectRatio)
        )

    def closeEvent(self, event):
        """
            Emits signal when window is closed
        """
        self.trackKeyThread.stop() #stop tracking key
        self.closed.emit()

        
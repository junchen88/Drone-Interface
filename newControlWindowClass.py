from PyQt5 import QtCore, QtGui, QtWidgets
from joystick import JoystickWidget
import QThreadClass
import usefulFunctions as uf
from PyQt5.QtCore import Qt, pyqtSignal
import time
from TrackKeyClass import TrackKeyClass
from dictionary import *

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

        self.joystickWidgetLeft = JoystickWidget("Left", keySettingInfo)
        self.joystickWidgetRight = JoystickWidget("Right", keySettingInfo)
        self.joystickWidgetLeft.setObjectName("left-joystick-widget")
        self.joystickWidgetRight.setObjectName("right-joystick-widget")

        #disable joystick widget at the start
        self.joystickWidgetLeft.setEnabled(False)
        self.joystickWidgetRight.setEnabled(False)

        
        self.joystickGrid.addWidget(self.joystickWidgetLeft,2,0,1,1)
        self.joystickGrid.addWidget(self.joystickWidgetRight,2,1,1,1)

        self.titleLayout = QtWidgets.QVBoxLayout()
        self.featureTitle = QtWidgets.QLabel("Feature Key Settings")
        self.featureTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.featureTitle.setStyleSheet(TITLESTYLE) 


        self.titleLayout.addWidget(self.featureTitle)
        self.joystickGrid.addLayout(self.titleLayout,0,0,1,2)

        self.trackKeyThread = TrackKeyClass(self.joystickWidgetLeft, self.joystickWidgetRight, keySettingInfo)
        self.trackKeyThread.start() #start tracking key

        #Get available features and its status
        self.featureGrid = self.getFeatureSettingLabelGrid(keySettingInfo)
        self.joystickGrid.addLayout(self.featureGrid,1,0,1,1)

        self.featureStatusBox, self.featureLabelsDict = self.getFeatureSettingStatus(keySettingInfo)
        self.joystickGrid.addLayout(self.featureStatusBox,1,1,1,1)
        self.trackKeyThread.featureChanged.connect(self.changeFeatureStatusDisplay)


        self.joystickGrid.setRowStretch(0,1)
        self.joystickGrid.setRowStretch(1,2)
        self.joystickGrid.setRowStretch(2,2)


        
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.centralWidgetGrid.addItem(spacerItem, 0,0,1,1)
        self.controlWindowHorizontalLay.addLayout(self.joystickGrid)
        self.centralWidgetGrid.addLayout(self.controlWindowHorizontalLay, 0,1,1,1)
        
        self.camThread = camThread
        self.displayFrame = QtWidgets.QLabel()
        self.displayFrame.setStyleSheet("")
        self.displayFrame.setText("")
        self.displayFrame.setObjectName("newDisplayFrame")
        self.displayFrame.setMinimumSize(680, 480)
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

    def getFeatureSettingLabelGrid(self, keySettingInfo):
        """
            Return a QGridLayout object containing information
            about the available drone features and the key setting
        """
        currentFeatureSetting = keySettingInfo.getUpdatedDroneFeaturesSetting()
        featureGrid = QtWidgets.QGridLayout()

        row = 0 #to keep track on the row number for grid location
        
        #loop for getting features and its key setting
        #plus assigning it onto the grid
        for key, value in currentFeatureSetting.items():
            labelWidget = QtWidgets.QLabel(f"{value}: ")
            combobox = QtWidgets.QComboBox()
            combobox.addItem(key)
            
            labelWidget.setObjectName(f"{value}-control-window-label")
            featureGrid.addWidget(labelWidget,row,0,1,1)
            featureGrid.addWidget(combobox,row,1,1,1)
            row += 1

        return featureGrid
    
    def getFeatureSettingStatus(self, keySettingInfo):
        """
            Get all the feature status and return
            the QVBoxLayout containing the status
            with the icons
        """
        featureStatusDict = self.trackKeyThread.featureStatusDict
        currentFeatureSetting = keySettingInfo.getUpdatedDroneFeaturesSetting()
        featureStatusBox = QtWidgets.QVBoxLayout()
        featureLabels = {}
        for key, value in currentFeatureSetting.items():
            featureStatus = featureStatusDict[value]

            statusLabel = QtWidgets.QLabel()
            pixmap = QtGui.QPixmap(CROSSLOCATION)
            pixmap = pixmap.scaled(16,16)
            statusLabel.setPixmap(pixmap)
            statusLabel.setObjectName(f"{value}-control-window-status-label")
            featureStatusBox.addWidget(statusLabel)
            featureLabels[value] = statusLabel


        return featureStatusBox, featureLabels

    def changeFeatureStatusDisplay(self, feature, status):
        """
            This function is triggered by the change in feature
            status caused by key pressed.
        """
        featureLabel = self.featureLabelsDict[feature]
        if status == True:

            featureLabel.setPixmap(QtGui.QPixmap(TICKLOCATION).scaled(16, 16))
        else:
            featureLabel.setPixmap(QtGui.QPixmap(CROSSLOCATION).scaled(16, 16))


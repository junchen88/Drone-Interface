from test import *
import webCamQThreadClass
import cv2
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
import string
from BetaFlightBoxWidget import *
from ArdupilotBoxWidget import *
from initPage2 import *

DEFAULT_MODEL = 'Betaflight'
MODELSINITDICT = {"Betaflight":False, "Ardupilot":False}
MODELMAPPING = ['Betaflight', 'Ardupilot']


class Drone_system():
    def __init__(self, droneSysStr):
        self.isInitialised = False
        self.droneSysStr = droneSysStr


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

        initPage2(self)
        self.chooseInit(DEFAULT_MODEL)


        self.currentSys = DEFAULT_MODEL

 

    #HELPER FUNCTION TO INITIALISE INTERFACE BASED ON DRONE SYSTEM
    def chooseInit(self, model):
        MODELSINITDICT[model] = True
        if model == 'Betaflight':
            self.groupBoxBeta = BetaFlightBoxWidget(self.page_2).getWidget()
            self.groupBoxHomeBeta = BetaFlightBoxWidget(self.page).getWidget()
            self.controlModeSetHorizontalLay.addWidget(self.groupBoxBeta)
           
            rightSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.controlModeSetHorizontalLay.addItem(rightSpacer)
            self.controlModeSetHorizontalLay.setStretch(0, 1)
            self.controlModeSetHorizontalLay.setStretch(1, 1)
            self.controlModeSetHorizontalLay.setStretch(3, 1)
            self.controlModeSetHorizontalLay.setStretch(4, 1)

            self.homeSettingVerticalLay.addWidget(self.groupBoxHomeBeta)

        elif model == 'Ardupilot':
            self.groupBoxHomeArdu = ArdupilotBoxWidget(self.page).getWidget()
            self.groupBoxArdu = ArdupilotBoxWidget(self.page_2).getWidget()
            self.controlModeSetHorizontalLay.insertWidget(3,self.groupBoxArdu)
            self.homeSettingVerticalLay.insertWidget(1, self.groupBoxHomeArdu)


        else:
            print("Something's wrong - using default system")
            self.groupBoxBeta = BetaFlightBoxWidget(self.page_2).groupBoxBeta
            self.groupBoxHomeBeta = BetaFlightBoxWidget(self.page).groupBoxBeta

        

    #RETURNS THE INTERFACE BASED ON THE DRONE SYSTEM
    #IN THE FORMAT OF SETTING BOX, HOME BOX
    def getModel(self, model):
        if model == 'Betaflight':
            return self.groupBoxBeta, self.groupBoxHomeBeta

        elif model == 'Ardupilot':
            return self.groupBoxArdu, self.groupBoxHomeArdu


    #FUNCTION FOR CHANGING INTERFACE BASED ON THE DRONE SYSTEM
    #SELECTED - ASSIGNED TO CONFIRM BUTTOM
    def changeInterfaceBasedOnModel(self):
        currentIndex = self.typeDropDown.currentIndex()
        selectedModel = MODELMAPPING[currentIndex]
        print(MODELSINITDICT[selectedModel])

        #HIDE CURRENT, SHOW SELECTED SYSTEM INTERFACE
        currentSysBox = self.getModel(self.currentSys)
        currentSysBox[0].hide()
        currentSysBox[1].hide()
        
        if not MODELSINITDICT[selectedModel]:
            #INITIALISE IF IT IS NOT INITIALISED
            self.chooseInit(selectedModel)

        newSysBox = self.getModel(selectedModel)
        newSysBox[0].show()
        newSysBox[1].show()
        self.currentSys = selectedModel
        
        

    
    def confirmSettings(self):
        currentSelectedSys = self.currentSys
        currentSysBox = self.getModel(currentSelectedSys)
        self.throttleSetUp
        self.throttleSetDown
        self.yawSetClockwise
        self.yawSetAnticlockwise
        self.rollSetLeft
        self.rollSetRight
        self.pitchSetFront
        self.pitchSetBack

        if currentSelectedSys == 'Betaflight':
            self.getBetaSettings()

        elif currentSelectedSys == 'Ardupilot':
            self.getArduSettings()

        else:
            self.getBetaSettings()




    def getBetaSettings(self):
        pass  
    
    def getArduSettings(self):
        pass

    #FOR CAMERA COMPONENT
    #___________________________________________________________________________________
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
    #_______________________________________________________________________________________________________-

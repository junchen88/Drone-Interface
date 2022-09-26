from test import *
import webCamQThreadClass
import cv2
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
import string
from BetaFlightBoxWidget import *
from ArdupilotBoxWidget import *

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

        self.initPage2(mainWindowBase)
        self.chooseInit(DEFAULT_MODEL)
        self.currentSys = DEFAULT_MODEL

        



    def initPage2(self, MainWindow):
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.controlsSetLabel = QtWidgets.QLabel(self.page_2)
        self.controlsSetLabel.setGeometry(QtCore.QRect(190, 120, 57, 15))
        self.controlsSetLabel.setObjectName("controlsSetLabel")
        self.layoutWidget = QtWidgets.QWidget(self.page_2)
        self.layoutWidget.setGeometry(QtCore.QRect(200, 60, 481, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.typeBoxLabel = QtWidgets.QLabel(self.layoutWidget)
        self.typeBoxLabel.setObjectName("typeBoxLabel")
        self.horizontalLayout.addWidget(self.typeBoxLabel)
        self.typeDropDown = QtWidgets.QComboBox(self.layoutWidget)
        self.typeDropDown.setObjectName("typeDropDown")
        self.typeDropDown.addItem("")
        self.typeDropDown.addItem("")
        self.horizontalLayout.addWidget(self.typeDropDown)
        self.layoutWidget1 = QtWidgets.QWidget(self.page_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(260, 160, 64, 261))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.throttleSetUp = QtWidgets.QLineEdit(self.layoutWidget1)
        self.throttleSetUp.setText("")
        self.throttleSetUp.setMaxLength(1)
        self.throttleSetUp.setObjectName("throttleSetUp")
        self.gridLayout.addWidget(self.throttleSetUp, 0, 0, 1, 1)
        self.throttleSetDown = QtWidgets.QLineEdit(self.layoutWidget1)
        self.throttleSetDown.setText("")
        self.throttleSetDown.setMaxLength(1)
        self.throttleSetDown.setObjectName("throttleSetDown")
        self.gridLayout.addWidget(self.throttleSetDown, 0, 1, 1, 1)
        self.yawSetClockwise = QtWidgets.QLineEdit(self.layoutWidget1)
        self.yawSetClockwise.setText("")
        self.yawSetClockwise.setMaxLength(1)
        self.yawSetClockwise.setObjectName("yawSetClockwise")
        self.gridLayout.addWidget(self.yawSetClockwise, 1, 0, 1, 1)
        self.yawSetAnticlockwise = QtWidgets.QLineEdit(self.layoutWidget1)
        self.yawSetAnticlockwise.setText("")
        self.yawSetAnticlockwise.setMaxLength(1)
        self.yawSetAnticlockwise.setObjectName("yawSetAnticlockwise")
        self.gridLayout.addWidget(self.yawSetAnticlockwise, 1, 1, 1, 1)
        self.rollSetLeft = QtWidgets.QLineEdit(self.layoutWidget1)
        self.rollSetLeft.setText("")
        self.rollSetLeft.setMaxLength(1)
        self.rollSetLeft.setObjectName("rollSetLeft")
        self.gridLayout.addWidget(self.rollSetLeft, 2, 0, 1, 1)
        self.rollSetRight = QtWidgets.QLineEdit(self.layoutWidget1)
        self.rollSetRight.setText("")
        self.rollSetRight.setMaxLength(1)
        self.rollSetRight.setObjectName("rollSetRight")
        self.gridLayout.addWidget(self.rollSetRight, 2, 1, 1, 1)
        self.pitchSetFront = QtWidgets.QLineEdit(self.layoutWidget1)
        self.pitchSetFront.setText("")
        self.pitchSetFront.setMaxLength(1)
        self.pitchSetFront.setObjectName("pitchSetFront")
        self.gridLayout.addWidget(self.pitchSetFront, 3, 0, 1, 1)
        self.pitchSetBack = QtWidgets.QLineEdit(self.layoutWidget1)
        self.pitchSetBack.setText("")
        self.pitchSetBack.setMaxLength(1)
        self.pitchSetBack.setObjectName("pitchSetBack")
        self.gridLayout.addWidget(self.pitchSetBack, 3, 1, 1, 1)
        self.layoutWidget2 = QtWidgets.QWidget(self.page_2)
        self.layoutWidget2.setGeometry(QtCore.QRect(110, 170, 61, 241))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.throttleSetLabel = QtWidgets.QLabel(self.layoutWidget2)
        self.throttleSetLabel.setObjectName("throttleSetLabel")
        self.verticalLayout.addWidget(self.throttleSetLabel)
        self.yawSetLabel = QtWidgets.QLabel(self.layoutWidget2)
        self.yawSetLabel.setObjectName("yawSetLabel")
        self.verticalLayout.addWidget(self.yawSetLabel)
        self.rollSetLabel = QtWidgets.QLabel(self.layoutWidget2)
        self.rollSetLabel.setObjectName("rollSetLabel")
        self.verticalLayout.addWidget(self.rollSetLabel)
        self.pitchSetLabel = QtWidgets.QLabel(self.layoutWidget2)
        self.pitchSetLabel.setObjectName("pitchSetLabel")
        self.verticalLayout.addWidget(self.pitchSetLabel)
        self.selectButton = QtWidgets.QPushButton(self.page_2)
        self.selectButton.setGeometry(QtCore.QRect(700, 60, 80, 31))
        self.selectButton.setObjectName("selectButton")
        self.confirmSetButton = QtWidgets.QPushButton(self.page_2)
        self.confirmSetButton.setGeometry(QtCore.QRect(440, 460, 161, 31))
        self.confirmSetButton.setObjectName("confirmSetButton")
        self.stackedWidget.addWidget(self.page_2)

        _translate = QtCore.QCoreApplication.translate
        self.controlsSetLabel.setText(_translate("MainWindow", "Controls"))
        self.typeBoxLabel.setText(_translate("MainWindow", "Please select drone system"))
        self.typeDropDown.setItemText(0, _translate("MainWindow", "Betaflight System Based Drones"))
        self.typeDropDown.setItemText(1, _translate("MainWindow", "Ardupilot System Based Drones"))
        self.throttleSetLabel.setText(_translate("MainWindow", "Throttle"))
        self.yawSetLabel.setText(_translate("MainWindow", "Yaw"))
        self.rollSetLabel.setText(_translate("MainWindow", "Roll"))
        self.pitchSetLabel.setText(_translate("MainWindow", "Pitch"))
        self.selectButton.setText(_translate("MainWindow", "Select"))
        self.confirmSetButton.setText(_translate("MainWindow", "Confirm Your Settings"))

        self.selectButton.clicked.connect(self.changeInterfaceBasedOnModel)

    #INITIALISE INTERFACE FOR BETAFLIGHT BASED SYSTEM
    # def initBetaflight(self):
    #     self.groupBoxBeta = QtWidgets.QGroupBox(self.page_2)
    #     self.groupBoxBeta.setGeometry(QtCore.QRect(530, 0, 451, 501))
    #     self.groupBoxBeta.setAutoFillBackground(False)
    #     self.groupBoxBeta.setStyleSheet("border:0")
    #     self.groupBoxBeta.setTitle("")
    #     self.groupBoxBeta.setObjectName("groupBoxBeta")
    #     self.groupBoxBeta.lower()

    #     self.flightmodeSetBetaKey = QtWidgets.QLineEdit(self.groupBoxBeta)
    #     self.flightmodeSetBetaKey.setGeometry(QtCore.QRect(260, 270, 31, 31))
    #     self.flightmodeSetBetaKey.setText("")
    #     self.flightmodeSetBetaKey.setMaxLength(1)
    #     self.flightmodeSetBetaKey.setObjectName("flightmodeSetBetaKey")
    #     self.armSetBetaLabel = QtWidgets.QLabel(self.groupBoxBeta)
    #     self.armSetBetaLabel.setGeometry(QtCore.QRect(210, 230, 31, 21))
    #     self.armSetBetaLabel.setObjectName("armSetBetaLabel")
    #     self.beeperSetBetaKey = QtWidgets.QLineEdit(self.groupBoxBeta)
    #     self.beeperSetBetaKey.setGeometry(QtCore.QRect(260, 320, 31, 31))
    #     self.beeperSetBetaKey.setText("")
    #     self.beeperSetBetaKey.setMaxLength(1)
    #     self.beeperSetBetaKey.setObjectName("beeperSetBetaKey")
    #     self.beeperSetBetaLabel = QtWidgets.QLabel(self.groupBoxBeta)
    #     self.beeperSetBetaLabel.setGeometry(QtCore.QRect(200, 330, 51, 21))
    #     self.beeperSetBetaLabel.setObjectName("beeperSetBetaLabel")
    #     self.angleSetBetaLabel = QtWidgets.QLabel(self.groupBoxBeta)
    #     self.angleSetBetaLabel.setGeometry(QtCore.QRect(90, 280, 41, 21))
    #     self.angleSetBetaLabel.setObjectName("angleSetBetaLabel")
    #     self.currentSetBetaMode = QtWidgets.QLineEdit(self.groupBoxBeta)
    #     self.currentSetBetaMode.setGeometry(QtCore.QRect(310, 270, 31, 31))
    #     self.currentSetBetaMode.setText("")
    #     self.currentSetBetaMode.setMaxLength(1)
    #     self.currentSetBetaMode.setObjectName("currentSetBetaMode")
    #     self.modesSetBetaLabel = QtWidgets.QLabel(self.groupBoxBeta)
    #     self.modesSetBetaLabel.setGeometry(QtCore.QRect(210, 100, 121, 21))
    #     self.modesSetBetaLabel.setObjectName("modesSetBetaLabel")
    #     self.armSetBetaKey = QtWidgets.QLineEdit(self.groupBoxBeta)
    #     self.armSetBetaKey.setGeometry(QtCore.QRect(260, 220, 31, 31))
    #     self.armSetBetaKey.setText("")
    #     self.armSetBetaKey.setMaxLength(1)
    #     self.armSetBetaKey.setObjectName("armSetBetaKey")
    #     self.prearmSetBetaKey = QtWidgets.QLineEdit(self.groupBoxBeta)
    #     self.prearmSetBetaKey.setGeometry(QtCore.QRect(260, 170, 31, 31))
    #     self.prearmSetBetaKey.setText("")
    #     self.prearmSetBetaKey.setMaxLength(1)
    #     self.prearmSetBetaKey.setObjectName("prearmSetBetaKey")
    #     self.horizonSetBetaLabel = QtWidgets.QLabel(self.groupBoxBeta)
    #     self.horizonSetBetaLabel.setGeometry(QtCore.QRect(150, 280, 61, 21))
    #     self.horizonSetBetaLabel.setObjectName("horizonSetBetaLabel")
    #     self.acroSetBetaLabel = QtWidgets.QLabel(self.groupBoxBeta)
    #     self.acroSetBetaLabel.setGeometry(QtCore.QRect(220, 280, 31, 21))
    #     self.acroSetBetaLabel.setObjectName("acroSetBetaLabel")
    #     self.OSDSetBetaKey = QtWidgets.QLineEdit(self.groupBoxBeta)
    #     self.OSDSetBetaKey.setGeometry(QtCore.QRect(260, 370, 31, 31))
    #     self.OSDSetBetaKey.setText("")
    #     self.OSDSetBetaKey.setMaxLength(1)
    #     self.OSDSetBetaKey.setObjectName("OSDSetBetaKey")
    #     self.prearmSetBetaLabel = QtWidgets.QLabel(self.groupBoxBeta)
    #     self.prearmSetBetaLabel.setGeometry(QtCore.QRect(200, 180, 51, 21))
    #     self.prearmSetBetaLabel.setObjectName("prearmSetBetaLabel")
    #     self.OSDDisableSetBetaLabel = QtWidgets.QLabel(self.groupBoxBeta)
    #     self.OSDDisableSetBetaLabel.setGeometry(QtCore.QRect(140, 380, 111, 21))
    #     self.OSDDisableSetBetaLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
    #     self.OSDDisableSetBetaLabel.setObjectName("OSDDisableSetBetaLabel")



    #     _translate = QtCore.QCoreApplication.translate
    #     self.armSetBetaLabel.setText(_translate("MainWindow", "Arm"))
    #     self.beeperSetBetaLabel.setText(_translate("MainWindow", "Beeper"))
    #     self.angleSetBetaLabel.setText(_translate("MainWindow", "Angle"))
    #     self.modesSetBetaLabel.setText(_translate("MainWindow", "Modes/Features"))
    #     self.horizonSetBetaLabel.setText(_translate("MainWindow", "Horizon"))
    #     self.acroSetBetaLabel.setText(_translate("MainWindow", "Acro"))
    #     self.prearmSetBetaLabel.setText(_translate("MainWindow", "Prearm"))
    #     self.OSDDisableSetBetaLabel.setText(_translate("MainWindow", "OSD Disable SW"))

    #INITIALISE INTERFACE FOR ARDUPILOT BASED SYSTEM DRONES
    # def initArdupilot(self):
    #     self.groupBoxArdu = QtWidgets.QGroupBox(self.page_2)
    #     self.groupBoxArdu.setGeometry(QtCore.QRect(530, 0, 451, 501))
    #     self.groupBoxArdu.setAutoFillBackground(False)
    #     self.groupBoxArdu.setStyleSheet("border:0")
    #     self.groupBoxArdu.setTitle("")
    #     self.groupBoxArdu.setObjectName("groupBoxArdu")
    #     self.groupBoxArdu.lower()

    #     self.flightmodeSetArduKey = QtWidgets.QLineEdit(self.groupBoxArdu)
    #     self.flightmodeSetArduKey.setGeometry(QtCore.QRect(260, 270, 31, 31))
    #     self.flightmodeSetArduKey.setText("")
    #     self.flightmodeSetArduKey.setMaxLength(1)
    #     self.flightmodeSetArduKey.setObjectName("flightmodeSetArduKey")
    #     self.armSetArduLabel = QtWidgets.QLabel(self.groupBoxArdu)
    #     self.armSetArduLabel.setGeometry(QtCore.QRect(210, 230, 31, 21))
    #     self.armSetArduLabel.setObjectName("armSetArduLabel")
    #     self.beeperSetArduKey = QtWidgets.QLineEdit(self.groupBoxArdu)
    #     self.beeperSetArduKey.setGeometry(QtCore.QRect(260, 320, 31, 31))
    #     self.beeperSetArduKey.setText("")
    #     self.beeperSetArduKey.setMaxLength(1)
    #     self.beeperSetArduKey.setObjectName("beeperSetArduKey")
    #     self.beeperSetArduLabel = QtWidgets.QLabel(self.groupBoxArdu)
    #     self.beeperSetArduLabel.setGeometry(QtCore.QRect(200, 330, 51, 21))
    #     self.beeperSetArduLabel.setObjectName("beeperSetArduLabel")
    #     # self.angleSetArduLabel = QtWidgets.QLabel(self.groupBoxArdu)
    #     # self.angleSetArduLabel.setGeometry(QtCore.QRect(90, 280, 41, 21))
    #     # self.angleSetArduLabel.setObjectName("angleSetArduLabel")
    #     self.currentSetArduMode = QtWidgets.QLineEdit(self.groupBoxArdu)
    #     self.currentSetArduMode.setGeometry(QtCore.QRect(310, 270, 31, 31))
    #     self.currentSetArduMode.setText("")
    #     self.currentSetArduMode.setMaxLength(1)
    #     self.currentSetArduMode.setObjectName("currentSetArduMode")
    #     self.modesSetArduLabel = QtWidgets.QLabel(self.groupBoxArdu)
    #     self.modesSetArduLabel.setGeometry(QtCore.QRect(210, 100, 121, 21))
    #     self.modesSetArduLabel.setObjectName("modesSetArduLabel")
    #     self.armSetArduKey = QtWidgets.QLineEdit(self.groupBoxArdu)
    #     self.armSetArduKey.setGeometry(QtCore.QRect(260, 220, 31, 31))
    #     self.armSetArduKey.setText("")
    #     self.armSetArduKey.setMaxLength(1)
    #     self.armSetArduKey.setObjectName("armSetArduKey")
    #     self.prearmSetArduKey = QtWidgets.QLineEdit(self.groupBoxArdu)
    #     self.prearmSetArduKey.setGeometry(QtCore.QRect(260, 170, 31, 31))
    #     self.prearmSetArduKey.setText("")
    #     self.prearmSetArduKey.setMaxLength(1)
    #     self.prearmSetArduKey.setObjectName("prearmSetArduKey")
    #     self.flightModeSetArduLabel = QtWidgets.QLabel(self.groupBoxArdu)
    #     self.flightModeSetArduLabel.setGeometry(QtCore.QRect(170, 280, 100, 21))
    #     self.flightModeSetArduLabel.setObjectName("flightModeSetArduLabel")
    #     # self.acroSetArduLabel = QtWidgets.QLabel(self.groupBoxArdu)
    #     # self.acroSetArduLabel.setGeometry(QtCore.QRect(220, 280, 31, 21))
    #     # self.acroSetArduLabel.setObjectName("acroSetArduLabel")
    #     self.OSDSetArduKey = QtWidgets.QLineEdit(self.groupBoxArdu)
    #     self.OSDSetArduKey.setGeometry(QtCore.QRect(260, 370, 31, 31))
    #     self.OSDSetArduKey.setText("")
    #     self.OSDSetArduKey.setMaxLength(1)
    #     self.OSDSetArduKey.setObjectName("OSDSetArduKey")
    #     self.prearmSetArduLabel = QtWidgets.QLabel(self.groupBoxArdu)
    #     self.prearmSetArduLabel.setGeometry(QtCore.QRect(200, 180, 51, 21))
    #     self.prearmSetArduLabel.setObjectName("prearmSetArduLabel")
    #     self.OSDDisableSetArduLabel = QtWidgets.QLabel(self.groupBoxArdu)
    #     self.OSDDisableSetArduLabel.setGeometry(QtCore.QRect(140, 380, 111, 21))
    #     self.OSDDisableSetArduLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
    #     self.OSDDisableSetArduLabel.setObjectName("OSDDisableSetArduLabel")



    #     _translate = QtCore.QCoreApplication.translate
    #     self.armSetArduLabel.setText(_translate("MainWindow", "Arm"))
    #     self.beeperSetArduLabel.setText(_translate("MainWindow", "Beeper"))
    #     #self.angleSetArduLabel.setText(_translate("MainWindow", "Angle"))
    #     self.modesSetArduLabel.setText(_translate("MainWindow", "Modes/Features"))
    #     self.flightModeSetArduLabel.setText(_translate("MainWindow", "Flight Mode"))
    #     #self.acroSetArduLabel.setText(_translate("MainWindow", "Acro"))
    #     self.prearmSetArduLabel.setText(_translate("MainWindow", "Prearm"))
    #     self.OSDDisableSetArduLabel.setText(_translate("MainWindow", "OSD Disable SW"))
        

    #HELPER FUNCTION TO INITIALISE INTERFACE BASED ON DRONE SYSTEM
    def chooseInit(self, model):
        MODELSINITDICT[model] = True
        if model == 'Betaflight':
            self.groupBoxBeta = BetaFlightBoxWidget(self.page_2).groupBoxBeta

        elif model == 'Ardupilot':

            self.groupBoxArdu = ArdupilotBoxWidget(self.page_2).groupBoxArdu
                
        else:
            print("Something's wrong - using default model")
            self.groupBoxBeta = BetaFlightBoxWidget(self.page_2).groupBoxBeta

    def getModel(self, model):
        if model == 'Betaflight':
            return self.groupBoxBeta

        elif model == 'Ardupilot':
            return self.groupBoxArdu


    #FUNCTION FOR CHANGING INTERFACE BASED ON THE DRONE SYSTEM
    #SELECTED - ASSIGNED TO CONFIRM BUTTOM
    def changeInterfaceBasedOnModel(self):
        currentIndex = self.typeDropDown.currentIndex()
        selectedModel = MODELMAPPING[currentIndex]
        print(MODELSINITDICT[selectedModel])

        #HIDE CURRENT, SHOW SELECTED SYSTEM INTERFACE
        currentSysBox = self.getModel(self.currentSys)
        currentSysBox.hide()
        
        if not MODELSINITDICT[selectedModel]:
            #INITIALISE IF IT IS NOT INITIALISED
            self.chooseInit(selectedModel)

        newSysBox = self.getModel(selectedModel)
        newSysBox.show()
        self.currentSys = selectedModel
        childrenWidgets = self.page_2.children()
        print(type(childrenWidgets))
        

    
    def confirmSettings(self):
        currentSysBox = self.getModel(self.currentSys)
        self.throttleSetUp
        self.throttleSetDown
        self.yawSetClockwise
        self.yawSetAnticlockwise
        self.rollSetLeft
        self.rollSetRight
        self.pitchSetFront
        self.pitchSetBack

        sysBoxChildren = currentSysBox.children()

        
        
        print(type(childrenWidgets))

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

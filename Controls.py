from test import *
import webCamQThreadClass
import cv2
from PyQt5.QtGui import QPixmap, QImage, QIcon
from PyQt5.QtCore import Qt

HOMEPAGE = 0
CONTROLPAGE = 1
SWARMPAGE = 2
SETTINGPAGE = 3

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

        self.createActions(mainWindowBase)
        self.setupBetaflight(mainWindowBase)

        self.flightDataLabel = QtWidgets.QLabel()
        self.flightDataLabel.setGeometry(QtCore.QRect(720, 240, 31, 21))
        self.flightDataLabel.setObjectName("flightDataLabel")

        _translate = QtCore.QCoreApplication.translate
        self.flightDataLabel.setText(_translate("MainWindow", "Flight Data:"))
        self.toolBar.addWidget(self.flightDataLabel)



    
    


    def setupBetaflight(self, MainWindow):
        self.flightmodeSetKey = QtWidgets.QLineEdit(self.page_2)
        self.flightmodeSetKey.setGeometry(QtCore.QRect(770, 280, 31, 31))
        self.flightmodeSetKey.setText("")
        self.flightmodeSetKey.setMaxLength(1)
        self.flightmodeSetKey.setObjectName("flightmodeSetKey")
        self.armSetLabel = QtWidgets.QLabel(self.page_2)
        self.armSetLabel.setGeometry(QtCore.QRect(720, 240, 31, 21))
        self.armSetLabel.setObjectName("armSetLabel")
        self.beeperSetKey = QtWidgets.QLineEdit(self.page_2)
        self.beeperSetKey.setGeometry(QtCore.QRect(770, 330, 31, 31))
        self.beeperSetKey.setText("")
        self.beeperSetKey.setMaxLength(1)
        self.beeperSetKey.setObjectName("beeperSetKey")
        self.beeperSetLabel = QtWidgets.QLabel(self.page_2)
        self.beeperSetLabel.setGeometry(QtCore.QRect(710, 340, 51, 21))
        self.beeperSetLabel.setObjectName("beeperSetLabel")
        self.angleSetLabel = QtWidgets.QLabel(self.page_2)
        self.angleSetLabel.setGeometry(QtCore.QRect(620, 290, 41, 21))
        self.angleSetLabel.setObjectName("angleSetLabel")
        self.currentSetMode = QtWidgets.QLineEdit(self.page_2)
        self.currentSetMode.setGeometry(QtCore.QRect(820, 280, 31, 31))
        self.currentSetMode.setText("")
        self.currentSetMode.setMaxLength(1)
        self.currentSetMode.setObjectName("currentSetMode")
        self.modesSetLabel = QtWidgets.QLabel(self.page_2)
        self.modesSetLabel.setGeometry(QtCore.QRect(720, 110, 121, 21))
        self.modesSetLabel.setObjectName("modesSetLabel")
        self.armSetKey = QtWidgets.QLineEdit(self.page_2)
        self.armSetKey.setGeometry(QtCore.QRect(770, 230, 31, 31))
        self.armSetKey.setText("")
        self.armSetKey.setMaxLength(1)
        self.armSetKey.setObjectName("armSetKey")
        self.prearmSetKey = QtWidgets.QLineEdit(self.page_2)
        self.prearmSetKey.setGeometry(QtCore.QRect(770, 180, 31, 31))
        self.prearmSetKey.setText("")
        self.prearmSetKey.setMaxLength(1)
        self.prearmSetKey.setObjectName("prearmSetKey")
        self.horizonSetLabel = QtWidgets.QLabel(self.page_2)
        self.horizonSetLabel.setGeometry(QtCore.QRect(670, 290, 51, 21))
        self.horizonSetLabel.setObjectName("horizonSetLabel")
        self.acroSetLabel = QtWidgets.QLabel(self.page_2)
        self.acroSetLabel.setGeometry(QtCore.QRect(730, 290, 31, 21))
        self.acroSetLabel.setObjectName("acroSetLabel")
        self.OSDSetKey = QtWidgets.QLineEdit(self.page_2)
        self.OSDSetKey.setGeometry(QtCore.QRect(770, 380, 31, 31))
        self.OSDSetKey.setText("")
        self.OSDSetKey.setMaxLength(1)
        self.OSDSetKey.setObjectName("OSDSetKey")
        self.prearmSetLabel = QtWidgets.QLabel(self.page_2)
        self.prearmSetLabel.setGeometry(QtCore.QRect(710, 190, 51, 21))
        self.prearmSetLabel.setObjectName("prearmSetLabel")
        self.OSDDisableSetLabel = QtWidgets.QLabel(self.page_2)
        self.OSDDisableSetLabel.setGeometry(QtCore.QRect(650, 390, 111, 21))
        self.OSDDisableSetLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.OSDDisableSetLabel.setObjectName("OSDDisableSetLabel")



        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.armSetLabel.setText(_translate("MainWindow", "Arm"))
        self.beeperSetLabel.setText(_translate("MainWindow", "Beeper"))
        self.angleSetLabel.setText(_translate("MainWindow", "Angle"))
        self.modesSetLabel.setText(_translate("MainWindow", "Modes/Features"))
        self.horizonSetLabel.setText(_translate("MainWindow", "Horizon"))
        self.acroSetLabel.setText(_translate("MainWindow", "Acro"))
        self.prearmSetLabel.setText(_translate("MainWindow", "Prearm"))
        self.OSDDisableSetLabel.setText(_translate("MainWindow", "OSD Disable SW"))

        


    #CREATE ACTIONS FOR TOOL BAR
    def createActions(self, mainWindowBase):
        self.homeAction = QtWidgets.QAction(mainWindowBase)
        self.homeAction.setText("&Home")
        self.homeAction.setIcon(QIcon(QPixmap("./icons/house-icon.webp")))
        self.toolBar.addAction(self.homeAction)
        self.homeAction.triggered.connect(lambda: self.toPage(HOMEPAGE))

        self.controlAction = QtWidgets.QAction(mainWindowBase)
        self.controlAction.setText("&Drone Controls")
        self.controlAction.setIcon(QIcon(QPixmap("./icons/control-panel-icon.webp")))
        self.toolBar.addAction(self.controlAction)
        self.controlAction.triggered.connect(lambda: self.toPage(CONTROLPAGE))

        self.swarmAction = QtWidgets.QAction(mainWindowBase)
        self.swarmAction.setText("&Swarming")
        self.swarmAction.setIcon(QIcon(QPixmap("./icons/air-drone-icon.png")))
        self.toolBar.addAction(self.swarmAction)
        self.swarmAction.triggered.connect(lambda: self.toPage(SWARMPAGE))


        self.settingAction = QtWidgets.QAction(mainWindowBase)
        self.settingAction.setText("&Setting")
        self.settingAction.setIcon(QIcon(QPixmap("./icons/setting-line-icon.webp")))
        self.toolBar.addAction(self.settingAction)
        self.settingAction.triggered.connect(lambda: self.toPage(SETTINGPAGE))


        self.toolBar.setIconSize(QtCore.QSize(48, 48))
        self.toolBar.setStyleSheet("QToolBar{spacing:30px;}");
    

    #REDIRECT PAGE AFTER CLICKING TOOLBAR ICONS
    def toPage(self, pageNumber):

        self.stackedWidget.setCurrentIndex(pageNumber)



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

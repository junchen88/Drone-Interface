import sys
from Controls import *
from PyQt5.QtGui import QIcon, QPixmap

HOMEPAGE = 0
CONTROLPAGE = 1
SWARMPAGE = 2
SETTINGPAGE = 3

class MainApp():

    def __init__(self, args):
        self.app = QtWidgets.QApplication(args)
        self.window = QtWidgets.QMainWindow()

        self.ui = Controls(self.window)
        self.ui.flightDataLabel = QtWidgets.QLabel()
        self.ui.flightDataLabel.setGeometry(QtCore.QRect(720, 240, 31, 21))
        self.ui.flightDataLabel.setObjectName("flightDataLabel")
        self.createActions(self.window)
        self.ui.toolBar.addWidget(self.ui.flightDataLabel)


        self.retranslateUi()
        self.window.show()
        sys.exit(self.app.exec_())

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

        self.ui.flightDataLabel.setText(_translate("MainWindow", "Flight Data:"))


    #CREATE ACTIONS FOR TOOL BAR
    def createActions(self, mainWindowBase):
        self.ui.homeAction = QtWidgets.QAction(mainWindowBase)
        self.ui.homeAction.setText("&Home")
        self.ui.homeAction.setIcon(QIcon(QPixmap("./icons/house-icon.webp")))
        self.ui.toolBar.addAction(self.ui.homeAction)
        self.ui.homeAction.triggered.connect(lambda: self.toPage(HOMEPAGE))

        self.ui.controlAction = QtWidgets.QAction(mainWindowBase)
        self.ui.controlAction.setText("&Drone Controls")
        self.ui.controlAction.setIcon(QIcon(QPixmap("./icons/control-panel-icon.webp")))
        self.ui.toolBar.addAction(self.ui.controlAction)
        self.ui.controlAction.triggered.connect(lambda: self.toPage(CONTROLPAGE))

        self.ui.swarmAction = QtWidgets.QAction(mainWindowBase)
        self.ui.swarmAction.setText("&Swarming")
        self.ui.swarmAction.setIcon(QIcon(QPixmap("./icons/air-drone-icon.png")))
        self.ui.toolBar.addAction(self.ui.swarmAction)
        self.ui.swarmAction.triggered.connect(lambda: self.toPage(SWARMPAGE))


        self.ui.settingAction = QtWidgets.QAction(mainWindowBase)
        self.ui.settingAction.setText("&Setting")
        self.ui.settingAction.setIcon(QIcon(QPixmap("./icons/setting-line-icon.webp")))
        self.ui.toolBar.addAction(self.ui.settingAction)
        self.ui.settingAction.triggered.connect(lambda: self.toPage(SETTINGPAGE))


        self.ui.toolBar.setIconSize(QtCore.QSize(48, 48))
        self.ui.toolBar.setStyleSheet("QToolBar{spacing:30px;}")
    

    #REDIRECT PAGE AFTER CLICKING TOOLBAR ICONS
    def toPage(self, pageNumber):

        self.ui.stackedWidget.setCurrentIndex(pageNumber)


if __name__ == "__main__":
   MainApp(sys.argv)
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore


class Joystick(QWidget):
    def __init__(self, parent=None):
        self.resetFlag = False
        super(Joystick, self).__init__(parent)
        self.setMinimumSize(100, 100)
        self.offsetFromTopLeft = QPointF(0, 0)
        self.grabHandle = False
        self.__maxDistance = 50

    def paintEvent(self, event):
        """
            Called by update() function to update the drawing
        """
        painter = QPainter(self)
        bounds = QRectF(-self.__maxDistance, -self.__maxDistance, self.__maxDistance * 2, self.__maxDistance * 2).translated(self._center())
        painter.drawEllipse(bounds)
        painter.setBrush(Qt.blue)
        painter.drawEllipse(self._ellipseHandle())

    def _ellipseHandle(self):
        """
            Gets the dimension and location of the ellipse
        """

        if self.offsetFromTopLeft == QPointF(0, 0):
            return QRectF(-20, -20, 40, 40).translated(self._center())

        return QRectF(-20, -20, 40, 40).translated(self.offsetFromTopLeft)
        

    def _center(self):
        """
            Gets the joystick circle center
        """
        return QPointF(self.width()/2, self.height()/2)


    def _boundJoystick(self, point):
        """
            limits the joystick boundary
        """
        limitLine = QLineF(self._center(), point)
        if (limitLine.length() > self.__maxDistance):
            limitLine.setLength(self.__maxDistance)
        return limitLine.p2()

    def joystickDirection(self):
        """
            Gets the current joystick direction in terms of
            horizontal and vertical axis
        """
        if not self.grabHandle:
            return "User did not drag or click the joystick handle"
        norm = QLineF(self._center(), self.offsetFromTopLeft)
        currentDistanceX = norm.dx()
        currentDistanceY = norm.dy()

        distanceX = min(currentDistanceX / self.__maxDistance, 1.0)
        distanceY = min(currentDistanceY / self.__maxDistance, 1.0)

        return ({"x":distanceX, "y":-distanceY})


    def mousePressEvent(self, event):
        """
            Change grab handle flag status depending on
            whether the users have clicked on the handle
        """
        self.grabHandle = self._ellipseHandle().contains(event.pos())
        return super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        """
            Recenter the joystick handle when users release
            the handle and if the reset check box is selected
        """
        if self.resetFlag == True:
            self.recenterJoystick()

    def mouseMoveEvent(self, event):
        """
            To track the movement of mouse while
            dragging the joystick handle
        """
        if self.grabHandle:
            print("Moving")
            self.offsetFromTopLeft = self._boundJoystick(event.pos())
            self.update() #redraw joystick
            print(self.joystickDirection())


    def changeResetFlag(self, status):
        """
            To change the flag indicating whether to reset
            joystick handle
        """
        self.resetFlag = status

    def recenterJoystick(self):
        """
            To recenter the joystick handle
        """
        self.grabHandle = False

        self.offsetFromTopLeft = self._center()
        self.update() #redraw joystick
        print("reset to original pos")
        print(self.joystickDirection())



class JoystickWidget(QWidget):
    def __init__(self, name):
        self.joystickComponent = Joystick()
        self.joystickLayout = QVBoxLayout()
        self.joystickLayout.setObjectName("joystickLayout")
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.joystickLayout.addItem(spacerItem)
        self.joystickLabel = QLabel(f"{name} Joystick")
        self.joystickLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.joystickLabel.setObjectName(f"joystickLabel-{name}")
        self.joystickLayout.addWidget(self.joystickLabel)
        self.joystickLayout.addWidget(self.joystickComponent)

        #add checkbox & use spacer to center checkbox
        #------------------------------------------------------------
        self.joystickCheckBox = QCheckBox("Reset To Centre")
        self.joystickCheckBox.setObjectName("joystickCheckBox")
        self.checkBoxHozLayout = QHBoxLayout()
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum,)
        self.checkBoxHozLayout.addItem(spacerItem)
        self.checkBoxHozLayout.addWidget(self.joystickCheckBox)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum,)
        self.checkBoxHozLayout.addItem(spacerItem)
        self.joystickLayout.addLayout(self.checkBoxHozLayout)

        self.joystickCheckBox.stateChanged.connect(lambda x: self.updateJoystickResetFlag())
        #---------------------------------------------------------------

        #bottom spacer
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.joystickLayout.addItem(spacerItem)

    def getJoystickLayout(self):
        return self.joystickLayout
    
    def updateJoystickResetFlag(self):
        self.joystickComponent.changeResetFlag(self.joystickCheckBox.isChecked())
        self.joystickComponent.recenterJoystick()
# if __name__ == '__main__':
#     # Create main application window
#     app = QApplication([])
#     app.setStyle(QStyleFactory.create("Cleanlooks"))
#     mw = QMainWindow()
#     mw.setWindowTitle('Joystick example')

#     # Create and set widget layout
#     # Main widget container
#     cw = QWidget()
#     ml = QGridLayout()
#     cw.setLayout(ml)
#     mw.setCentralWidget(cw)

#     # Create joystick 
#     joystick = JoystickWidget()

#     # ml.addLayout(joystick.get_joystick_layout(),0,0)
#     ml.addLayout(joystick.getJoystickLayout(),0,0)

#     mw.show()

#     ## Start Qt event loop unless running in interactive mode or using pyside.
#     if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        # QApplication.instance().exec_()
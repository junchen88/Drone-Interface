from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from dictionary import *


class Joystick(QWidget):
    def __init__(self, x, y, joystickXControlLabel, joystickYControlLabel, parent=None):
        self.xControl = x
        self.xControlValue = x
        self.yControl = y
        self.yControlValue = y
        self.resetFlag = False
        super(Joystick, self).__init__(parent)
        self.setMinimumSize(100, 100)
        self.offsetFromTopLeft = QPointF(0, 0)
        self.grabHandle = False
        self.__maxDistance = 50
        self.joystickXControlLabel = joystickXControlLabel
        self.joystickYControlLabel = joystickYControlLabel

    def paintEvent(self, event):
        """
            Called by update() function to update the drawing
        """
        painter = QPainter(self)
        bounds = QRectF(-self.__maxDistance, -self.__maxDistance, self.__maxDistance * 2, self.__maxDistance * 2).translated(self._center())
        painter.drawEllipse(bounds)
        painter.setBrush(Qt.blue)
        painter.drawEllipse(self._ellipseHandle())

    def resizeEvent(self, event):
        self.recenterJoystick()

    def _ellipseHandle(self):
        """
            Gets the dimension and location of the ellipse
        """

        if self.offsetFromTopLeft == QPointF(0, 0):
            self.offsetFromTopLeft = self._center()
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

    def setControlLabel(self, joystickDir):
        #To update the label showing the current control value
        #-----------------------------------------------------------------
        if joystickDir is not None and not isinstance(joystickDir,str):
            xControl = self.xControl
            yControl = self.yControl
            
            yValue = joystickDir[yControl]*100
            self.joystickYControlLabel.setText(f"{yControl}: {yValue}%")

            xValue = joystickDir[xControl]*100
            self.joystickXControlLabel.setText(f"{xControl}: {xValue}%")
        #-----------------------------------------------------------------

    #TODO sent data to interface here
    def joystickDirection(self, moveByKey = False, moveByCheckBox = False):
        """
            Gets the current joystick direction in terms of
            horizontal and vertical axis
        """
        if not self.grabHandle:
            if moveByKey is False and moveByCheckBox is False:
                return "User did not drag or click the joystick handle"

            else:
                norm = QLineF(self._center(), self.offsetFromTopLeft)
                currentDistanceX = norm.dx()
                currentDistanceY = norm.dy()

                distanceX = min(currentDistanceX / self.__maxDistance, 1.0)
                distanceY = min(currentDistanceY / self.__maxDistance, 1.0)
                self.xControlValue = distanceX
                self.yControlValue = distanceY

                #round value to 1 d.p. here
                roundedX = round(distanceX,1)
                roundedY = -round(distanceY,1)

                #check for correct signage here
                if roundedY == -0.0:
                    roundedY = 0.0
                
                if roundedX == -0.0:
                    roundedX = 0.0

                joystickDir = {self.xControl:roundedX, self.yControl:roundedY}
                self.setControlLabel(joystickDir)

                return joystickDir

                
        
        norm = QLineF(self._center(), self.offsetFromTopLeft)
        currentDistanceX = norm.dx()
        currentDistanceY = norm.dy()

        distanceX = min(currentDistanceX / self.__maxDistance, 1.0)
        distanceY = min(currentDistanceY / self.__maxDistance, 1.0)
        self.xControlValue = distanceX
        self.yControlValue = distanceY
                
        #round value to 1 d.p. here
        roundedX = round(distanceX,1)
        roundedY = -round(distanceY,1)

        #check for correct signage here
        if roundedY == -0.0:
            roundedY = 0.0
        
        if roundedX == -0.0:
            roundedX = 0.0

        joystickDir = {self.xControl:roundedX, self.yControl:roundedY}
        self.setControlLabel(joystickDir)
        return joystickDir


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
        print(self.joystickDirection(moveByCheckBox=True))

    def moveJoystick(self, action):
        """
            Move joystick with keys
        """
        posOrNeg = -1

        #check for positive/negative direction
        #---------------------------------------------------------
        for posWord in ["up", "clockwise", "forward", "right"]:
            if posWord in action.casefold():
                posOrNeg = 1
                break

        for negWord in ["down", "anticlockwise", "backward", "left"]:
            if negWord in action.casefold():
                posOrNeg = -1
                break
        #---------------------------------------------------------
        joystickDir = None
        #check for x axis control
        if self.xControl.casefold() in action.casefold():
            self.offsetFromTopLeft.setX(self.offsetFromTopLeft.x() + posOrNeg*0.1*self.width()/2)
            self.offsetFromTopLeft = self._boundJoystick(self.offsetFromTopLeft)
            joystickDir = self.joystickDirection(moveByKey=True)
            print(joystickDir)
            self.update() #redraw joystick

        #check for y axis control
        elif self.yControl.casefold() in action.casefold():
            
            # We use negative here since the qpainter class moving down is positive
            self.offsetFromTopLeft.setY(self.offsetFromTopLeft.y() + -posOrNeg*0.1*self.height()/2)
            self.offsetFromTopLeft = self._boundJoystick(self.offsetFromTopLeft)
            joystickDir = self.joystickDirection(moveByKey=True)
            print(joystickDir)            
            self.update() #redraw joystick
        
        




class JoystickWidget(QWidget):
    def __init__(self, name:str, keySettingInfo, parent=None):
        super(JoystickWidget, self).__init__(parent)
        self.name = name
        if name.lower() == "left":
            self.joystickXControlLabel = QLabel("Yaw: 0.0%")
            self.joystickYControlLabel = QLabel("Throttle: 0.0%")


            self.joystickComponent = Joystick("Yaw", "Throttle", self.joystickXControlLabel, self.joystickYControlLabel)

        elif name.lower() == "right":
            self.joystickXControlLabel = QLabel("Roll: 0.0%")
            self.joystickYControlLabel = QLabel("Pitch: 0.0%")

            self.joystickComponent = Joystick("Roll", "Pitch", self.joystickXControlLabel, self.joystickYControlLabel)

        self.joystickComponent.setObjectName(f"joystick-{name}")
        self.joystickLayout = QVBoxLayout()
        self.joystickLayout.setObjectName(f"joystickLayout-{name}")
        self.setLayout(self.joystickLayout)

        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.joystickLayout.addItem(spacerItem)
        self.joystickLabel = QLabel(f"{name} Joystick")
        self.joystickLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.joystickLabel.setStyleSheet(TITLESTYLE)
        self.joystickLabel.setObjectName(f"joystickLabel-{name}")
        self.joystickLayout.addWidget(self.joystickLabel)
        self.joystickHorizontalLayout = QHBoxLayout()
        self.joystickHorizontalLayout.setObjectName(f"joystickHorizontalLayout-{name}")


        #left joy
        if name.lower() == "left":
            self.keyActions = {"Throttle":0,"Yaw":0}
            tUpText = keySettingInfo.getRelevantComboBox(TU).currentText()
            tDownText = keySettingInfo.getRelevantComboBox(TD).currentText()
            self.joystickThrottleUpLabel = QLabel(f"Throttle Up: {tUpText}")
            self.joystickThrottleDownLabel = QLabel(f"Throttle Down: {tDownText}")
            self.joystickThrottleUpLabel.setAlignment(QtCore.Qt.AlignCenter)
            self.joystickThrottleDownLabel.setAlignment(QtCore.Qt.AlignCenter)



            self.joystickLayout.addWidget(self.joystickThrottleUpLabel)
            yAntiText = keySettingInfo.getRelevantComboBox(YA).currentText()
            yClockText = keySettingInfo.getRelevantComboBox(YC).currentText()
            self.joystickYawLeftLabel = QLabel(f"Yaw Anticlockwise: {yAntiText}")
            self.joystickYawRightLabel = QLabel(f"Yaw Clockwise: {yClockText}")

            
            self.joystickHorizontalLayout.addWidget(self.joystickYawLeftLabel)

            self.joystickHorizontalLayout.addWidget(self.joystickComponent)
            self.joystickHorizontalLayout.addWidget(self.joystickYawRightLabel)

            self.joystickLayout.addLayout(self.joystickHorizontalLayout)

            self.joystickLayout.addWidget(self.joystickThrottleDownLabel)

            self.joystickLayout.addWidget(self.joystickXControlLabel)
            self.joystickLayout.addWidget(self.joystickYControlLabel)

        #right joy
        elif name.lower() == "right":
            self.keyActions = {"Pitch":0,"Roll":0}
            pForwardText = keySettingInfo.getRelevantComboBox(PF).currentText()
            pBackText = keySettingInfo.getRelevantComboBox(PB).currentText()
            self.joystickPitchForwardLabel = QLabel(f"Pitch Forward: {pForwardText}")
            self.joystickPitchBackwardLabel = QLabel(f"Pitch Backward: {pBackText}")
            
            self.joystickPitchForwardLabel.setAlignment(QtCore.Qt.AlignCenter)
            self.joystickPitchBackwardLabel.setAlignment(QtCore.Qt.AlignCenter)

            self.joystickLayout.addWidget(self.joystickPitchForwardLabel)
            rLeftText = keySettingInfo.getRelevantComboBox(RL).currentText()
            rRightText = keySettingInfo.getRelevantComboBox(RR).currentText()
            self.joystickRollLeftLabel = QLabel(f"Roll Left: {rLeftText}")
            self.joystickRollRightLabel = QLabel(f"Roll Right: {rRightText}")
            

            self.joystickHorizontalLayout.addWidget(self.joystickRollLeftLabel)

            self.joystickHorizontalLayout.addWidget(self.joystickComponent)
            self.joystickHorizontalLayout.addWidget(self.joystickRollRightLabel)

            self.joystickLayout.addLayout(self.joystickHorizontalLayout)

            self.joystickLayout.addWidget(self.joystickPitchBackwardLabel)

            self.joystickLayout.addWidget(self.joystickXControlLabel)
            self.joystickLayout.addWidget(self.joystickYControlLabel)



        #add checkbox & use spacer to center checkbox
        #------------------------------------------------------------
        self.joystickCheckBox = QCheckBox("Reset To Centre")
        self.joystickCheckBox.setObjectName(f"joystickCheckBox-{name}")
        self.checkBoxHozLayout = QHBoxLayout()
        self.checkBoxHozLayout.setObjectName("checkbox horizontal layout")
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

        #Spacing Layout
        self.joystickLayout.setStretch(0,2)
        self.joystickLayout.setStretch(1,2)
        self.joystickLayout.setStretch(8,2)


    def getJoystickLayout(self):
        return self.joystickLayout
    
    def updateJoystickResetFlag(self):
        """
            to update reset flag and recenter joystick
        """
        self.joystickComponent.changeResetFlag(self.joystickCheckBox.isChecked())
        self.joystickComponent.recenterJoystick()

    def reservedKeyEvent(self, keyDict, key):
        """
            when reserved keys are pressed
        """
        try:
            if keyDict[key] == RESET:
                self.joystickCheckBox.setChecked(not self.joystickCheckBox.isChecked())

        except Exception as e:
            print(f"not reserved key: {e}")
        
    def moveJoystick(self, action:str):
        
        joystickDir = self.joystickComponent.moveJoystick(action)

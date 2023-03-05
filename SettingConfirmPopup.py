
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QMainWindow


class SettingConfirmPopup(QMainWindow):
    def __init__(self, mainwindow):
        super().__init__()
        # self.reply = QMessageBox.question(self, "Message", "Do you want to discard the changes?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        self.msgBox = QMessageBox(mainwindow)
        self.msgBox.setWindowTitle("Message")
        self.msgBox.setText("Do you want to discard the changes?")
        self.msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.msgBox.setDefaultButton(QMessageBox.No)
        self.msgBox.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowTitleHint)
        self.value = self.msgBox.exec()
        
    def getResult(self):
        if self.value == QMessageBox.Yes:
            #CONVERT BACK TO ORIGINAL
            return "Ignore Changes"
        else:
            return "Go Back"


import sys
import cv2

def runCamera(threadVar):
    # 0 IS FOR THE PRIMARY CAMERA DEVICE
    
    cap = cv2.VideoCapture(0)
    while threadVar.isWorkerRunning:
        status, frame = cap.read()
        if status:
            threadVar.change_pixmap_signal.emit(frame)
    # shut down capture system
    cap.release()
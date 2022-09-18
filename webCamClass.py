from threading import Thread
import cv2, time

##IF USING VMWARE, NEED TO MAKE USB CONTROLLER AS 3.0

class videoStream():
    def __init__(self):
        #0 IS FOR PRIMARY CAM
        self.capture = cv2.VideoCapture(0)


        # Lets check start/open your cam!
        if self.capture.read() == False:
            self.capture.open()

        if not self.capture.isOpened():
            print('Cannot open camera')

        #START A THREAD FOR READING FRAME IN PARALLEL
        self.thread = Thread(target=self.readFrames, args=())
        self.thread.daemon = True
        self.thread.start()

    
    def readFrames(self):

        #INFINITE LOOP FOR READING FRAMES
        while True:
            if self.capture.isOpened():
                (self.status, self.frame) = self.capture.read()



    
    #SHOW FRAMES/STREAM WITHOUT GUI
    def show_frame_no_gui(self):

        cv2.imshow('live cam', self.frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            self.capture.release()
            cv2.destroyAllWindows()
            exit(1)

    #RETURN THE FRAME
    def get_frame(self):
        return self.frame


if __name__ == '__main__':
    video_stream = videoStream()
    while True:
        try:
            video_stream.show_frame_no_gui()
        except AttributeError:
            pass
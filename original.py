import threading
import cv2


class webcam:
    def __init__(self):

        self.video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        thread = threading.Thread(target=self.window, args=())
        thread.daemon = True
        thread.start()

    def window(self):

        while True:

            ret, self.frame = self.video.read()

            cv2.imshow("frame", self.frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        self.video.release()
        cv2.destroyAllWindows()

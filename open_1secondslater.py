import threading
import original
import cv2
import time


class process1:

    def __init__(self):

        thread = threading.Thread(target=self.open_slowly, name="1 second delay", args=())
        thread.daemon = True
        thread.start()

    def open_slowly(self):

        while True:

            time.sleep(1)
            cv2.imshow("frame2", window.frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cv2.destroyAllWindows()


window = original.webcam()
process1 = process1()

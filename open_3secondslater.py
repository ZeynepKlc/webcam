from open_1secondslater import window
import time
import cv2
import threading


class process2:

    def __init__(self):

        thread = threading.Thread(target=self.threeseconds_delay, name="3 seconds delay", args=())
        thread.start()

    def threeseconds_delay(self):

        while True:

            time.sleep(3)
            cv2.imshow("frame3", window.frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cv2.destroyAllWindows()


process2 = process2()

thread_list = threading.enumerate()
for thread in thread_list:
    print("Name:", thread.name)

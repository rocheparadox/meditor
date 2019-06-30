
from datetime import datetime
from pyzbar import pyzbar
from time import sleep
import cv2

class qr_read():

    def __init__(self):

        self.qr_data=0
        self.r_data=0
        self.r_type=0
        self.csv_file="read_files.csv"
        self.w_to_file=open(self.csv_file,"w")
        self.found = set()

    def qr_detect(self,frame):

        self.qr_data=pyzbar.decode(frame)

        for qr in  self.qr_data:
            (x, y, w, h) = qr.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

            self.r_data=qr.data.decode("utf-8")
            self.r_type=qr.type

            text="{} ({})".format(self.r_data,self.r_type)
            cv2.putText(frame, text, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            if self.r_data not in self.found:
                self.w_to_file.write("{},{}\n".format(datetime.now(),self.r_data))
                self.w_to_file.flush()
                self.found.add(self.r_data)

            print(text)

            #sleep(1)



        return  self.r_data

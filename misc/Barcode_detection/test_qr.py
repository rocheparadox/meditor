import cv2

from getqr import qr_read

cap=cv2.VideoCapture(2)

readqr=qr_read()

while True:

    ret,frame=cap.read()

    data=readqr.qr_detect(frame)

    #cv2.putText(frame,data,(),(10,10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),2)

    cv2.imshow("qrwindow",frame)

    if cv2.waitKey(1) & 0xff==ord('q'):
        break


cv2.destroyAllWindows()




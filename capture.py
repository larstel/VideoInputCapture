import numpy as np
import cv2

cap = cv2.VideoCapture(2)
cap.set(cv2.CAP_PROP_FPS, 30)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    resize = cv2.resize(frame, (1024,600))

    # Display the resulting frame
    cv2.imshow('frame',resize)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
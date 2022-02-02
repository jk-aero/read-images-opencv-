import cv2 as cv
cap = cv.VideoCapture(0)
while True:
    variable, frame = cap.read()
    grey = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    cv.imshow('title', grey)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()

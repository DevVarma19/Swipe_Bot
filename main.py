# Import the modules
import cv2
import numpy as np
import pyautogui

# initializing the camera
cap = cv2.VideoCapture(0)

# Detect Skin Color
# lower = np.array([0, 48, 80], dtype = "uint8")
# upper = np.array([20, 255, 255], dtype = "uint8")

# Blue Color
lower = np.array([110,50,50])
upper = np.array([130,255,255])

prev_y = 0

pyautogui.FAILSAFE = False
while True:
    ret, frame = cap.read()
    # Convert the BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Creating a mask
    mask = cv2.inRange(hsv, lower, upper)
    # Drawing Contours
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # Removing the noises
    for c in contours:
        area = cv2.contourArea(c)
        if area > 300:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            if y < prev_y :
                pyautogui.press('down')
            elif y > prev_y :
                pyautogui.press('up')
            prev_y = y

    # cv2.drawContours(frame, contours, -1, (0, 0 , 255), 2)
    # Displaying the frames
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)

    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
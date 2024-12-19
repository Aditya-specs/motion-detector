import cv2
import time


video = cv2.VideoCapture(0)
first_frame = None
while True:
    time.sleep(0)
    check, frame = video.read()

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gaussain_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)


    if first_frame is None:
        first_frame = gaussain_frame

    
    delta_frame = cv2.absdiff(first_frame , gaussain_frame)
    thresh_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)

    

    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 1000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)

        cv2.imshow("MY video", frame)

    key = cv2.waitKey(1)
    




    if key == ord("a"):
        break

video.release()


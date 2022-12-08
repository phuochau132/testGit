import cv2

# define a video capture object
vid = cv2.VideoCapture("./test.mp4")
rotate = 0
while (True):

    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    if rotate != 0:
        image = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        cv2.imshow('frame', image)
    else:
        cv2.imshow('frame', frame)
    # Display the resulting frame

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if cv2.waitKey(1) & 0xFF == ord('a'):
        rotate = -90


# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
"asdadasdhaudeptrai"

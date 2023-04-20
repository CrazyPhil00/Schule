import cv2

# Open a connection to the camera (0 is the default camera)
cap = cv2.VideoCapture(0)

# Load the pre-trained classifier for detecting faces
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Loop over frames from the camera
while True:
    # Capture the current frame
    ret, frame = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the output
    cv2.imshow('output', frame)

    # Wait for a key press and check if the "q" key was pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera and close the windows
cap.release()
cv2.destroyAllWindows()

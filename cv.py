import cv2

def main():
    # Create a VideoCapture object to access the webcam
    cap = cv2.VideoCapture(-1)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Unable to access the webcam.")
        return

    while True:
        # Capture frame-by-frame from the webcam
        ret, frame = cap.read()

        # If the frame is not read properly, break the loop
        if not ret:
            print("Error: Unable to capture frame.")
            break

        # Display the captured frame
        cv2.imshow('Webcam', frame)

        # Check for the 'q' key to quit the program
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the VideoCapture and close the OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

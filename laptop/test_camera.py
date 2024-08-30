import cv2
import time

def capture_image():
    # Capture a picture using the camera
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return ""

    # Wait two seconds for the camera to stabilize before taking a picture
    time.sleep(2)

    # Discard the first few frames to ensure a stable image
    for i in range(5):
        ret, frame = cap.read()

    if not ret or frame is None:
        print("Error: Could not capture image. Frame is empty.")
        cap.release()
        return ""

    cap.release()

    # Display the captured image (optional)
    cv2.imshow('Captured Image', frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    capture_image()

if __name__ == "__main__":
    main()
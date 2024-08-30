import cv2
import pytesseract
import time

def capture_and_recognize_text():
    # Capture a picture
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return ""

    # Wait two seconds for the camera to stabilize before taking a picture
    # -----------------------------
    # Not using it for two seconds will result in a black screen
    time.sleep(2)

    # Discard the first few frames to ensure that you are capturing a stable image
    # ----------------------
    # can deletable
    for i in range(5):
        ret, frame = cap.read()

    if not ret or frame is None:
        print("Error: Could not capture image. Frame is empty.")
        cap.release()
        return ""

    cap.release()

    # Display image
    # wait press key close window
    # Test need (need delete)
    cv2.imshow('Captured Image', frame)
    cv2.waitKey(0) # Conflict with the start function
    cv2.destroyAllWindows()

    # Transformed gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    # OCR text recognition using tesseract
    text = pytesseract.image_to_string(gray)
    return text
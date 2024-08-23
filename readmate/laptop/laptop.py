import cv2
import pytesseract
import time
from naoqi import ALProxy

tts = ALProxy("ALTextToSpeech", "127.0.0.1", 9559)


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

def main():
    recognized_text = capture_and_recognize_text()
    command = raw_input("Type 'start' to begin text recognition: ").strip().lower()
    if recognized_text and command == "start":
        recognized_text = recognized_text.encode('utf-8')
        # print text and transfer text to nao
        print("Text: ", recognized_text) # Test need (need delete)
        tts.say(recognized_text)
    else:
        print("No text recognized.") # Test need (need delete)
        tts.say("I could not recognize any text.")

if __name__ == "__main__":
    main()




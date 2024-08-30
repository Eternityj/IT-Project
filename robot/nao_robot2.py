import Language_module

import cv2
import pytesseract
import numpy as np
from naoqi import ALProxy

NAO_IP = "127.0.0.1"
NAO_PORT = 9559

tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_PORT)
memory = ALProxy("ALMemory", NAO_IP, NAO_PORT)
speech_recognition = ALProxy("ALSpeechRecognition", NAO_IP, NAO_PORT)
video_device = ALProxy("ALVideoDevice", NAO_IP, NAO_PORT)

is_paused = False
full_text = ""
current_position = 0

def capture_image():
    # The nao's camera is called, the top camera is called (0 for the top camera, 1 for the bottom camera),
    # 1 specifies the image resolution, 13 specifies the color space of the image, and 10 specifies the camera frame rate
    video_client = video_device.subscribeCamera("python_client", 0, 1, 13, 10)

    # Get image
    nao_image = video_device.getImageRemote(video_client)
    video_device.unsubscribe(video_client)
    ####### Whether the first few frame rates need to be discarded to obtain the most stable image

    if nao_image is None:
        print("Failed to capture image from NAO camera")
        return ""

    # Convert the image to OpenCV format
    width = nao_image[0]
    height = nao_image[1]
    array = nao_image[6]
    image = np.frombuffer(array, dtype=np.uint8).reshape(height, width, 3)

    # Convert to grayscale image
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # OCR using Tesseract
    text = pytesseract.image_to_string(gray_image)

    return text


def speak_text():
    global current_position, full_text, is_paused

    while current_position < len(full_text):
        if is_paused:
            break
        end_position = current_position + 50
        if end_position > len(full_text):
            end_position = len(full_text)
        segment = full_text[current_position:end_position]
        tts.say(segment)
        current_position = end_position


def on_word_recognized(value):
    global is_paused, full_text, current_position

    word = value[0]
    confidence = value[1]

    if confidence > 0.5:
        if word == "start":
            if not full_text:
                full_text = capture_image()
                if full_text:
                    is_paused = False
                    current_position = 0
                    tts.say("I have recognized the following text.")
                    speak_text()
                else:
                    tts.say("I could not recognize any text.")
        elif word == "pause":
            is_paused = True
            tts.stopAll()
        elif word == "continue":
            if is_paused:
                is_paused = False
                speak_text()


def start_recognition():
    speech_recognition.setLanguage("English")
    vocabulary = ["start", "pause", "continue"]
    speech_recognition.setVocabulary(vocabulary, False)
    speech_recognition.subscribe("Test_ASR")
    memory.subscribeToEvent("WordRecognized", "python", "on_word_recognized_event")


def on_word_recognized_event(event_name, value, subscriber_identifier):
    on_word_recognized(value)


if __name__ == "__main__":
    start_recognition()


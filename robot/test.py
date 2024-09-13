from camera_module import *
from read_module import *
from naoqi import ALProxy

NAO_IP = "192.168.1.108"
NAO_PORT = 9559

tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_PORT)
memory = ALProxy("ALMemory", NAO_IP, NAO_PORT)
speech_recognition = ALProxy("ALSpeechRecognition", NAO_IP, NAO_PORT)
video_device = ALProxy("ALVideoDevice", NAO_IP, NAO_PORT)

def main():
    # text = capture_image()
    # recognized_text = text.encode('utf-8')
    text= "hello read mate"
    read_text(text)
    if speech_recognition.getActiveLanguage() is not None:
        speech_recognition.stopProcessing()

if __name__ == "__main__":
    main()
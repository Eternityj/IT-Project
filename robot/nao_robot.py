from Interactive_module import *
from naoqi import ALProxy

NAO_IP = "127.0.0.1"
NAO_PORT = 9559

tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_PORT)
memory = ALProxy("ALMemory", NAO_IP, NAO_PORT)
speech_recognition = ALProxy("ALSpeechRecognition", NAO_IP, NAO_PORT)
video_device = ALProxy("ALVideoDevice", NAO_IP, NAO_PORT)

def main():
    start_recognition()

if __name__ == "__main__":
    main()


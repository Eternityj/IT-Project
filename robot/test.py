from read_module import *
from naoqi import ALProxy
from music_module import *
from flip_page_module import *
from interactive_module import *

NAO_IP = "192.168.1.112"
NAO_PORT = 9559

tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_PORT)
memory = ALProxy("ALMemory", NAO_IP, NAO_PORT)
speech_recognition = ALProxy("ALSpeechRecognition", NAO_IP, NAO_PORT)
video_device = ALProxy("ALVideoDevice", NAO_IP, NAO_PORT)

def main():
    start_read()
    # flip_page()

if __name__ == "__main__":
    main()


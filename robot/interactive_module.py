from voice_module import *
from camera_module import *
from music_module import *
from read_module import *
from naoqi import ALProxy


NAO_IP = "192.168.1.108"
NAO_PORT = 9559

tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_PORT)
memory = ALProxy("ALMemory", NAO_IP, NAO_PORT)
speech_recognition = ALProxy("ALSpeechRecognition", NAO_IP, NAO_PORT)

def on_word_recognized(value):
    state = "off"

    word = value[0]  # Recognized word
    confidence = value[1]  # Confidence level of the recognized word

    if confidence > 0.5:  # Check if the confidence level is acceptable
        if word == "hi, readmate":
            recognized_text = capture_image()
            tts.say("I am here, how can i help you?")
            state = "on"
        else:
            tts.say("please say hi, readmate")

    while state == "on":
        if confidence > 0.5:
            if word == "readmate, start read":
                if recognized_text:
                    recognized_text = recognized_text.encode('utf-8')
                    read_text(recognized_text)
                else:
                    tts.say("I could not recognize any text.")
            elif word == "readmate, pause reading":
                pause_reading()
            elif word == "readmate, continue reading":
                continue_reading()
            # stop not supported
            # elif word == "readmate, stop reading":
            #     # stop_reading()
            elif word == "readmate, play music":
                play_music()
            elif word == "readmate, stop music":
                stop_music()
            elif word == "readmate, increase volume":
                change_volume(10)
            elif word == "readmate, decrease volume":
                change_volume(-10)
            elif word.lower() in ["english", "french", "chinese"]:
                change_language(word)
            elif word == "bye readmate":
                stop_music()
                # stop_reading()
                tts.say("Goodbye!")
                state = "off"
                exit()
            else:
                tts.say("Unknown command, please try again.")
def start_recognition():
    speech_recognition.setLanguage("English")
    vocabulary = ["hi, readmate", "readmate, start read", "readmate, pause reading", "readmate, continue reading",
                  "readmate, stop reading","readmate, play music", "readmate, stop music", "readmate, increase volume",
                  "readmate, decrease volume", "bye readmate", "english", "french", "chinese"]
    speech_recognition.setVocabulary(vocabulary, False)
    speech_recognition.subscribe("Test_ASR")
    memory.subscribeToEvent("WordRecognized", "interactive_module", "on_word_recognized_event")

def on_word_recognized_event(event_name, value, subscriber_identifier):
    on_word_recognized(value)

import sys
from naoqi import ALProxy, ALModule, ALBroker
from camera_module import *
from voice_module import *
from music_module import *
from read_module import *
from gpt import *

NAO_IP = "127.0.0.1"
NAO_PORT = 9559

tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_PORT)
speech_recognition = ALProxy("ALSpeechRecognition", NAO_IP, NAO_PORT)
memory = ALProxy("ALMemory", NAO_IP, NAO_PORT)

broker = ALBroker("myBroker", "0.0.0.0", 0, NAO_IP, NAO_PORT)

text = ""

class InteractiveModule(ALModule):
    def __init__(self, name):
        ALModule.__init__(self, name)
        self.memory = ALProxy("ALMemory", NAO_IP, NAO_PORT)
        self.tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_PORT)
        self.speech_recognition = ALProxy("ALSpeechRecognition", NAO_IP, NAO_PORT)


        self.start_recognition()

    def start_recognition(self):
        self.speech_recognition.setLanguage("English")

        self.speech_recognition.pause(True)


        vocabulary = ["hi, read mate", "read mate, start read", "read mate, pause reading", "read mate, continue reading",
                  "read mate, stop reading", "read mate, play music", "read mate, stop music", "read mate, increase volume",
                  "read mate, decrease volume", "read mate ask", "bye read mate", "english", "french", "chinese"]
        self.speech_recognition.setVocabulary(vocabulary, False)


        self.speech_recognition.pause(False)

        try:
            self.memory.subscribeToEvent("WordRecognized", "interactive_module", "on_word_recognized_event")
        except Exception as e:
            print("Failed to subscribe to WordRecognized event")

    def on_word_recognized_event(self, event_name, value, subscriber_identifier):
        global text
        if value:
            word = value[0]
            confidence = value[1]
            if confidence > 0.5:  # Check if the confidence level is acceptable
                if word == "hi,read mate":
                    tts.say("I am here, how can I help you?")
                elif word == "read mate, start read":
                    recognized_text = capture_image()
                    if not recognized_text:
                        tts.say("I could not recognize any text.")
                    else:
                        recognized_text = recognized_text.encode('utf-8')
                        text = recognized_text
                        read_text(recognized_text)
                elif word == "read mate, pause reading":
                    pause_reading()
                elif word == "read mate, continue reading":
                    continue_reading()
                elif word == "read mate, play music":
                    play_music()
                elif word == "read mate, stop music":
                    stop_music()
                elif word == "read mate, increase volume":
                    change_volume(10)
                elif word == "read mate, decrease volume":
                    change_volume(-10)
                elif word.lower() in ["english", "french", "chinese"]:
                    change_language(word)
                elif word.startswith("read mate, ask"):
                    question = word[len("read mate, ask "):]
                    answer = ask_gpt_with_current_page(text, question)
                    answer = answer.encode('utf-8')
                    if answer:
                        tts.say("Here is the answer: " + answer)
                    else:
                        tts.say("Sorry, I could not find an answer.")
                    tts.say("Here is the answer: " + answer)
                elif word == "bye read mate":
                    stop_music()
                    broker.shutdown()
                    sys.exit()
                    tts.say("Goodbye!")
                else:
                    tts.say("Unknown command, please try again.")

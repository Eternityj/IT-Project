from Camera_module import capture_image
from Language_module import change_language
from naoqi import ALProxy

NAO_IP = "127.0.0.1"
NAO_PORT = 9559

tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_PORT)
memory = ALProxy("ALMemory", NAO_IP, NAO_PORT)
speech_recognition = ALProxy("ALSpeechRecognition", NAO_IP, NAO_PORT)

is_paused = False
full_text = ""
current_position = 0

def read_text():
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



def start_recognition():
    speech_recognition.setLanguage("English")
    vocabulary = ["readmate start", "read pause", "read continue", "change language to english", "change language to french", "change language to chinese"]
    speech_recognition.setVocabulary(vocabulary, False)
    speech_recognition.subscribe("Test_ASR")
    memory.subscribeToEvent("WordRecognized", "python", "on_word_recognized_event")

def on_word_recognized_event(event_name, value, subscriber_identifier):
    on_word_recognized(value)

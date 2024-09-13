from camera_module import capture_image
from language_module import change_language
from voice_module import *
from emotion_module import *
from naoqi import ALProxy
import nltk


NAO_IP = "192.168.1.108"
NAO_PORT = 9559

custom_data_path = '/Users/yangjiesen/PycharmProjects/readmate/nltk_data'
nltk.data.path.append(custom_data_path)

tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_PORT)

is_paused = False
current_position = 0

def read_text(text):
    global is_paused, current_position

    sentences = nltk.sent_tokenize(text)
    current_volume = get_current_volume()
    current_rate = get_current_rate()

    while current_position < len(sentences):
        if is_paused:
            break  # Skip reading if paused

        sentence = sentences[current_position]
        rate, volume = emotion_read(sentence)
        tts.setVolume(current_volume + volume)
        tts.setParameter("speed", current_rate + rate)

        # Speak the current sentence
        tts.say(sentence)

        current_position += 1  # Move to the next sentence

    if current_position == len(sentences):
        current_position = 0

def pause_reading():
    global is_paused
    is_paused = True

def continue_reading():
    global is_paused
    is_paused = False


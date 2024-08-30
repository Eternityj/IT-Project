from emotion_module import *
import subprocess
import os
import nltk

read_process = None

custom_data_path = '/Users/yangjiesen/PycharmProjects/readmate/nltk_data'
nltk.data.path.append(custom_data_path)

def read_text(text):
    global read_process

    stop_reading()

    sentences = nltk.sent_tokenize(text)

    for sentence in sentences:
        rate, volume = A(sentence)
        os.system("osascript -e 'set volume output volume {}'".format(volume))
        read_process = subprocess.Popen(['say', '-r', str(rate), sentence])
        read_process.wait()



def stop_reading():
    global read_process

    if read_process:
        read_process.terminate()
        read_process = None


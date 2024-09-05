from emotion_module import *
from voice_module import *
import subprocess
import threading
import os
import nltk

read_process = None
read_thread = None
is_paused = False
current_position = 0

custom_data_path = '/Users/yangjiesen/PycharmProjects/readmate/nltk_data'
nltk.data.path.append(custom_data_path)

def read_text(text):
    global read_process, is_paused, current_position

    sentences = nltk.sent_tokenize(text)
    current_volume = get_current_volume()
    print(current_volume)

    while current_position < len(sentences):
        if is_paused:
            break  # Skip reading if paused

        sentence = sentences[current_position]
        rate, volume = emotion_read(sentence)
        os.system("osascript -e 'set volume output volume {}'".format(current_volume + volume))
        # test need
        # print(volume)

        # Terminate previous process if still running
        # No use for the moment, not sure if it can be used in stop read
        if read_process and read_process.poll() is None:
            read_process.terminate()

        read_process = subprocess.Popen(['say', '-r', str(rate), sentence])
        read_process.communicate()

        current_position += 1  # Move to the next sentence

    if current_position == len(sentences):
        current_position = 0

def start_reading(text):
    global read_thread
    read_thread = threading.Thread(target=read_text, args=(text,))
    read_thread.start()

def pause_reading():
    global is_paused
    is_paused = True

def continue_reading(text):
    global is_paused, read_thread
    is_paused = False
    if read_thread and not read_thread.is_alive():
        # Start a new thread to continue reading
        read_thread = threading.Thread(target=read_text, args=(text,))
        read_thread.start()

# not supported
def stop_reading():
    global read_process

    if read_process:
        try:
            read_process.terminate()
            read_process.wait(timeout=5)  # Wait for process to terminate
        except subprocess.TimeoutExpired:
            read_process.kill()  # Force kill if termination is not successful
        finally:
            read_process = None


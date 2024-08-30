from laptop import *
import time
import random
import os
import subprocess
from naoqi import ALProxy

tts = ALProxy("ALTextToSpeech", "127.0.0.1", 9559)

music_process = None

def play_music_every_hour():
    while True:
        time.sleep(3600)
        play_music()

def play_music():
    global music_process

    # Specify the music folder path
    music_folder = "/Users/yangjiesen/PycharmProjects/readmate/music"

    # Gets all the music files in the folder
    music_files = [f for f in os.listdir(music_folder) if f.endswith(('.mp3', '.wav'))]

    if not music_files:
        print("No music files found in the folder.")
        tts.say("I could not find any music files.")
        return

    # Choose a music file at random
    selected_music = random.choice(music_files)

    # Play music file
    music_path = os.path.join(music_folder, selected_music)
    print("Playing")
    stop_music()
    music_process = subprocess.Popen(['afplay', music_path])

def stop_music():
    global music_process

    if music_process:
        # Stop music process
        music_process.terminate()
        music_process = None
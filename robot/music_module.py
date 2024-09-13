import time
import random
import os
from naoqi import ALProxy
#import wave
#import contextlib

NAO_IP = "192.168.1.108"
NAO_PORT = 9559

tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_PORT)
''''
def is_valid_audio(file_path):
    # Check if the file is a valid audio file
    try:
        if file_path.endswith('.wav'):
            with contextlib.closing(wave.open(file_path, 'rb')) as f:
                return True
        elif file_path.endswith('.mp3'):
            # For mp3 files, we can attempt to open them with a third-party library like mutagen
            from mutagen.mp3 import MP3
            audio = MP3(file_path)
            return True
        else:
            return False
    except Exception as e:
        print(f"Invalid audio file detected: {file_path}, Error: {e}")
        return False

''''
''''
def play_music():
    # Specify the music folder path
    music_folder = "/Users/yangjiesen/PycharmProjects/readmate/music"

    # Gets all the music files in the folder
    music_files = [f for f in os.listdir(music_folder) if f.endswith(('.mp3', '.wav'))]

    # Validate each music file
    valid_music_files = []
    for music_file in music_files:
        music_path = os.path.join(music_folder, music_file)
        if is_valid_audio(music_path):
            valid_music_files.append(music_file)
        else:
            print(f"Skipping invalid file: {music_file}")

    if not valid_music_files:
        print("No valid music files found in the folder.")
        tts.say("I could not find any valid music files.")
        return

    # Choose a music file at random
    selected_music = random.choice(valid_music_files)
    music_path = os.path.join(music_folder, selected_music)

    # Stop any currently playing music
    stop_music()

    # Create a proxy for the ALAudioPlayer module
    audio_player = ALProxy("ALAudioPlayer", NAO_IP, NAO_PORT)

    try:
        # Play the music file using ALAudioPlayer
        audio_player.playFile(music_path)
        print("Playing music on the robot.")
    except Exception as e:
        print("Error while playing music:", e)
        tts.say("There was an error playing the music.")
    ''''
def play_music():
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
    music_path = os.path.join(music_folder, selected_music)

    # Stop any currently playing music
    stop_music()

    # Create a proxy for the ALAudioPlayer module
    audio_player = ALProxy("ALAudioPlayer", NAO_IP, NAO_PORT)

    try:
        # Play the music file using ALAudioPlayer
        audio_player.playFile(music_path)
        print("Playing music on the robot.")
    except Exception as e:
        print("Error while playing music")

def stop_music():
    # Create a proxy for the ALAudioPlayer module
    audio_player = ALProxy("ALAudioPlayer", NAO_IP, NAO_PORT)

    try:
        # Stop all currently playing audio
        audio_player.stopAll()
        print("Music stopped.")
    except Exception as e:
        print("Error while stopping music")

def play_music_every_hour():
    while True:
        time.sleep(3600)
        play_music()

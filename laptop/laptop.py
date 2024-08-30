from camera_module import *
from music_module import *
from read_module import *
from voice_module import *
import threading
from naoqi import ALProxy

tts = ALProxy("ALTextToSpeech", "127.0.0.1", 9559)

is_paused = False

def main():
    global is_paused
    state = "off"

    command = raw_input().strip().lower()
    if command == "hi, readmate":
        recognized_text = capture_and_recognize_text()
        state = "on"
        # for nao robot
        tts.say("I am here, how can i help you?")
    else:
        tts.say("please say hi, readmate")

    while state == "on":
        command = raw_input().strip().lower()
        if command == "readmate, start read":
            if recognized_text:
                recognized_text = recognized_text.encode('utf-8')
                # print text and transfer text to nao
                print("Text: ", recognized_text) # Test need (need delete)
                read_text(recognized_text)
                # for nao robot
                tts.say(recognized_text)
            else:
                print("No text recognized.") # Test need (need delete)
                tts.say("I could not recognize any text.")
        elif command == "readmate, pause":
            # Pause not supported
            print("Pausing...")
            is_paused = True
        elif command == "readmate, continue":
            # Continue not supported
            print("Continuing...")
            is_paused = False
        elif command == "readmate, stop read":
            stop_reading()
        elif command == "readmate, play music":
            play_music()
        elif command == "readmate, stop music":
            stop_music()
            print("Music stopped.")
        elif command == "readmate, increase the volume":
            change_volume(10)
        elif command == "readmate, decrease the volume":
            change_volume(-10)
        # can not use
        elif command == "readmate, increase the rate":
            change_rate(20)
        # can not use
        elif command == "readmate, decrease the rate":
            change_rate(-20)
        elif command == "bye, readmate":
            stop_music()
            stop_reading()
            print("Exiting program.")
            break
        else:
            print("Unknown command, please try again.")
            tts.say("Unknown command, please try again.")


if __name__ == "__main__":
    music_thread = threading.Thread(target=play_music_every_hour)
    music_thread.setDaemon(True)
    music_thread.start()
    main()




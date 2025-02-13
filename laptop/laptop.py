from camera_module import *
from voice_module import *
from music_module import *
from read_module import *
from gpt import *
import threading
from naoqi import ALProxy

tts = ALProxy("ALTextToSpeech", "127.0.0.1", 9559)

is_paused = False

def main():
    global is_paused
    state = "off"

    while state == "off":
        command = raw_input().strip().lower()
        if command == "hi, readmate":
            recognized_text = capture_and_recognize_text()
            state = "on"
            print("I am here, how can i help you?")
            # for nao robot
            # tts.say("I am here, how can i help you?")
        else:
            print("please say hi, readmate")
            # tts.say("please say hi, readmate")

    while state == "on":
        command = raw_input().strip().lower()
        if command == "readmate, start read":
            if recognized_text:
                recognized_text = recognized_text.encode('utf-8')
                # print text and transfer text to nao
                print("start read")
                print("Text: ", recognized_text) # Test need (need delete)
                start_reading(recognized_text)
                # for nao robot
                # tts.say(recognized_text)
            else:
                print("No text recognized.") # Test need (need delete)
                # tts.say("I could not recognize any text.")
        elif command == "readmate, pause reading":
            print("Pausing")
            pause_reading()
        elif command == "readmate, continue reading":
            print("Continuing")
            continue_reading(recognized_text)
        # stop not supported
        # elif command == "readmate, stop reading":
        #     stop_reading()
        elif command == "readmate, play music":
            play_music()
        elif command == "readmate, stop music":
            stop_music()
            print("Music stopped.")
        elif command == "readmate, increase the volume":
            change_volume(10)
            print("Volume increased")
        elif command == "readmate, decrease the volume":
            change_volume(-10)
            print("Volume decreased")
        # not supported
        elif command == "readmate, increase the rate":
            change_rate(20)
            print("Rate increased")
        # not supported
        elif command == "readmate, decrease the rate":
            change_rate(-20)
            print("Rate decreased")
        elif command == "ask gpt":
            if not recognized_text:
                recognized_text = ""
            user_question = raw_input("Ask your question: ").strip()
            answer = ask_gpt_with_current_page(recognized_text, user_question)
            # tts.say(answer)
            print("GPT Answer:", answer)
        elif command == "bye, readmate":
            # not supported stop reading
            # stop_reading()
            stop_music()
            print("Goodbye! Feel free to reach out anytime.")
            exit()
        else:
            print("Unknown command, please try again.")
            # tts.say("Unknown command, please try again.")


if __name__ == "__main__":
    music_thread = threading.Thread(target=play_music_every_hour)
    music_thread.setDaemon(True)
    music_thread.start()
    main()




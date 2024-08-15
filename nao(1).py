import subprocess
from naoqi import ALProxy


tts = ALProxy("ALTextToSpeech", "127.0.0.1", 9559)

def recognize_text_with_camera():
    # Remember to replace it with the address of your camera
    process = subprocess.Popen(["python3", "/Users/yangjiesen/PycharmProjects/pythonProject/text_recognition.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if process.returncode != 0:
        print("Error running text_recognition.py: ", error)
        return ""
    return output.strip()

def main():
    recognized_text = recognize_text_with_camera()
    if recognized_text:
        # print text and transfer text to nao
        print("Text: ", recognized_text)
        tts.say(recognized_text)
    else:
        print("No text recognized.")
        tts.say("I could not recognize any text.")

if __name__ == "__main__":
    main()



from naoqi import ALProxy

NAO_IP = "127.0.0.1"
NAO_PORT = 9559

tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_PORT)

def change_volume(change):
    global current_volume
    tts.setVolume(current_volume + change)
    print("Current volume:", current_volume)
from naoqi import ALProxy

NAO_IP = "127.0.0.1"
NAO_PORT = 9559

tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_PORT)

current_volume = 50
read_rate = 160

def change_volume(change):
    global current_volume

    current_volume = max(0, min(200, current_volume + change))
    tts.setVolume(current_volume + change)
    print("Current volume:", current_volume)

def get_current_volume():
    return current_volume

# Conflict with emotional reading
def change_rate(change):
    global read_rate

    read_rate = max(100, min(350, read_rate + change))
    tts.setParameter("speed", read_rate)
    print(read_rate)

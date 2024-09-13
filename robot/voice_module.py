from naoqi import ALProxy

NAO_IP = "192.168.1.108"
NAO_PORT = 9559

tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_PORT)

current_volume = 0.5
current_rate = 140

def change_volume(change):
    global current_volume

    current_volume = max(0.0, min(1.0, current_volume + change))
    tts.setVolume(current_volume + change)
    print("Current volume:", current_volume)

def get_current_volume():
    return current_volume

# Conflict with emotional reading
def change_rate(change):
    global current_rate

    current_rate = max(20, min(240, current_rate + change))
    tts.setParameter("speed", current_rate)
    print(current_rate)

def get_current_rate():
    return current_rate

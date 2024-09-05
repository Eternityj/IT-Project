import os

current_volume = 50
read_rate = 160

def change_volume(change):
    global current_volume

    current_volume = max(0, min(200, current_volume + change))  # Limit the volume between 0 and 100
    os.system("osascript -e 'set volume output volume {}'".format(current_volume))

def get_current_volume():
    return current_volume

# Conflict with emotional reading
def change_rate(change):
    global read_rate

    read_rate = max(0, min(260, read_rate + change))  # Limit reading speeds between 100 and 350 WPM
    print(read_rate)

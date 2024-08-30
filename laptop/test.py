from read_module import *
from voice_module import *


current_volume = 50
read_rate = 180
def main():
    read_text("Long ago, there was a big cat in the house. He caught many mice while they were stealing food.One day the mice had a meeting to talk about the way to deal with their common enemy. Some said this, and some said that.At last a young mouse got up, and said that he had a good idea.We could tie a bell around the neck of the cat. Then when he comes near, we can hear the sound of the bell, and run away.Everyone approved of this proposal, but an old wise mouse got up and said, That is all very well, but who will tie the bell to the cat? The mice looked at each other, but nobody spoke.")
    # while True:
    #     command = raw_input().strip().lower()
    #     if command == "start":
    #         read_text("Long ago, there was a big cat in the house. He caught many mice while they were stealing food.One day the mice had a meeting to talk about the way to deal with their common enemy. Some said this, and some said that.At last a young mouse got up, and said that he had a good idea.We could tie a bell around the neck of the cat. Then when he comes near, we can hear the sound of the bell, and run away.Everyone approved of this proposal, but an old wise mouse got up and said, That is all very well, but who will tie the bell to the cat? The mice looked at each other, but nobody spoke.")
    #     elif command == "readmate, increase the volume":
    #         change_volume(10)
    #     elif command == "readmate, decrease the volume":
    #         change_volume(-10)
    #     elif command == "readmate, increase the rate":
    #         change_rate(20)
    #     elif command == "readmate, decrease the rate":
    #         change_rate(-20)

if __name__ == "__main__":
    main()
from interactive_module import *

NAO_IP = "127.0.0.1"
NAO_PORT = 9559

if __name__ == "__main__":
    interactive_module = InteractiveModule("interactive_module")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        broker.shutdown()


def handle_Speech(command):
    global is_paused
    if command == "readmate, start read":
        recognized_text = capture_and_recognize_text()
        if recognized_text:
            read_text(recognized_text)
        else:
            tts.say("I could not recognize any text.")
    elif command == "readmate, stop read":
        stop_reading()
    elif command == "readmate, increase the volume":
        change_volume(10)
    elif command == "readmate, decrease the volume":
        change_volume(-10)
    elif command == "readmate, increase the rate":
        change_rate(20)
    elif command == "readmate, decrease the rate":
        change_rate(-20)
    elif command == "bye, readmate":
        stop_reading()
        print("Exiting program.")
        tts.say("Goodbye!")
    else:
        print("Unknown command, please try again.")
        tts.say("Unknown command, please try again.")
from naoqi import ALProxy


NAO_IP = "127.0.0.1"
NAO_PORT = 9559

tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_PORT)
memory = ALProxy("ALMemory", NAO_IP, NAO_PORT)
speech_recognition = ALProxy("ALSpeechRecognition", NAO_IP, NAO_PORT)

def change_language(language):
    supported_languages = speech_recognition.getAvailableLanguages()

    if language in supported_languages:
        speech_recognition.setLanguage(language)
        tts.setLanguage(language)
        print("The language has been changed to" +language) # text need
        tts.say("The language has been changed to" +language)
    else:
        print("Language" + language + "is not supported.") # text need
        tts.say("Sorry, the language" + language + "is not supported.")
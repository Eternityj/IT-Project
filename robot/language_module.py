from naoqi import ALProxy


NAO_IP = "127.0.0.1"
NAO_PORT = 9559

tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_PORT)
memory = ALProxy("ALMemory", NAO_IP, NAO_PORT)
speech_recognition = ALProxy("ALSpeechRecognition", NAO_IP, NAO_PORT)

def change_language(language):
    # Find supported languages
    supported_languages = speech_recognition.getAvailableLanguages()

    if language in supported_languages:
        speech_recognition.setLanguage(language)
        tts.setLanguage(language)
        tts.say("The language has been changed to" +language)
    else:
        tts.say("Sorry, the language" + language + "is not supported.")
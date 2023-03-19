def create_speech_recognizer(recognizer_type):
    """
    Create a speech recognizer of the given type.
    """
    if recognizer_type == "whisper":
        from speech_recognizer_whisper import WhisperSpeechRecognizer
        return WhisperSpeechRecognizer()
    else:
        raise Exception("Unknown speech recognizer type: " + recognizer_type)
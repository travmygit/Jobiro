def create_speech_recorder(recorder_type):
    """
    Create a speech recorder of the given type.
    """
    if recorder_type == "microphone":
        from speech_recorder_microphone import MicrophoneSpeechRecorder
        return MicrophoneSpeechRecorder()
    else:
        raise Exception("Unknown speech recorder type: " + recorder_type)
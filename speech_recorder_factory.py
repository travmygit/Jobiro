def create_speech_recorder(recorder_type):
    """
    Create a speech recorder of the given type.
    """
    if recorder_type == "sr":
        from speech_recorder_sr import SrSpeechRecorder
        return SrSpeechRecorder()
    else:
        raise Exception("Unknown speech recorder type: " + recorder_type)
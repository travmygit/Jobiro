class SpeechRecorder:
    def setup(self):
        """
        Setup the speech recorder.
        """
        raise NotImplementedError
    
    def record(self):
        """
        Record audio.
        """
        raise NotImplementedError
    
    def stop(self):
        """
        Stop recording audio.
        """
        raise NotImplementedError
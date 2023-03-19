class SpeechRecorder:
    def setup(self):
        """
        Setup the speech recorder.
        """
        raise NotImplementedError
    
    def record(self, duration):
        """
        Record audio for the specified duration.
        """
        raise NotImplementedError
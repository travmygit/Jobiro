class SpeakerAvatar():
    def setup(self):
        """
        Setup the speaker avatar.
        """
        raise NotImplementedError
    
    def speak(self, text):
        """
        Speak text.
        """
        raise NotImplementedError
    
    def shut(self):
        """
        Shut the speaker avatar.
        """
        raise NotImplementedError
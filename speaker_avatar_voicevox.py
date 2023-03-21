from speaker_avatar import SpeakerAvatar


class VoiceVoxSpeakerAvatar(SpeakerAvatar):
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
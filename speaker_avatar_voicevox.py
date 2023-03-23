from speaker_avatar import SpeakerAvatar
from log import logger


class VoiceVoxSpeakerAvatar(SpeakerAvatar):
    def setup(self):
        """
        Setup the speaker avatar.
        """
        pass

    def speak(self, text):
        """
        Speak text.
        """
        logger.info(f'Speaking text: {text}')

    def shut(self):
        """
        Shut the speaker avatar.
        """
        pass
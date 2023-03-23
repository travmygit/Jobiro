from speaker_avatar import SpeakerAvatar
import pyaudio
import wave


class HintSpeakerAvatar(SpeakerAvatar):
    def setup(self):
        """
        Setup the speaker avatar.
        """
        self.pyaudio_module = pyaudio
        self.CHUNK = 1024  # number of frames stored in each buffer
        self.audio = None
        self.stream = None

    def speak(self, text):
        """
        Speak text.
        """
        audio_file = None

        if text == 'Recording':
            audio_file = 'sounds/Speech On.wav'
        elif text == 'Stopped recording':
            audio_file = 'sounds/Speech Off.wav'
        else:
            raise ValueError(f'Unknown text: {text}')

        with wave.open(audio_file, 'rb') as wave_file:
            self.audio = self.pyaudio_module.PyAudio()
            self.stream = self.audio.open(format=self.audio.get_format_from_width(wave_file.getsampwidth()),
                                          channels=wave_file.getnchannels(),
                                          rate=wave_file.getframerate(),
                                          output=True,
                                          frames_per_buffer=self.CHUNK)
            
            self.stream.write(wave_file.readframes(wave_file.getnframes()))
            self.stream.stop_stream()
            self.stream.close()
            self.audio.terminate()

    def shut(self):
        """
        Shut the speaker avatar.
        """
        try:
            self.stream.stop_stream()
            self.stream.close()
        except Exception:
            pass
        finally:
            self.audio.terminate()
            self.stream = None
from speech_recorder import SpeechRecorder
import pyaudio
import wave
from log import logger


class MicrophoneSpeechRecorder(SpeechRecorder):
    def setup(self):
        """
        Setup the speech recorder.
        """
        # Default values
        device_index = None
        sample_rate = None
        chunk_size = 1024

        # set up PyAudio
        self.pyaudio_module = pyaudio
        audio = self.pyaudio_module.PyAudio()
        try:
            count = audio.get_device_count()  # obtain device count
            if device_index is not None:  # ensure device index is in range
                assert 0 <= device_index < count, "Device index out of range ({} devices available; device index should be between 0 and {} inclusive)".format(count, count - 1)
            if sample_rate is None:  # automatically set the sample rate to the hardware's default sample rate if not specified
                device_info = audio.get_device_info_by_index(device_index) if device_index is not None else audio.get_default_input_device_info()
                assert isinstance(device_info.get("defaultSampleRate"), (float, int)) and device_info["defaultSampleRate"] > 0, "Invalid device info returned from PyAudio: {}".format(device_info)
                sample_rate = int(device_info["defaultSampleRate"])
        finally:
            audio.terminate()

        self.device_index = device_index
        self.FORMAT = self.pyaudio_module.paInt16  # 16-bit int sampling
        self.SAMPLE_WIDTH = self.pyaudio_module.get_sample_size(self.FORMAT)  # size of each sample
        self.SAMPLE_RATE = sample_rate  # sampling rate in Hertz
        self.CHUNK = chunk_size  # number of frames stored in each buffer
        self.CHANNELS = 1

        self.audio = None
        self.stream = None
        self.frames = []

    def stream_callback(self, in_data, frame_count, time_info, status):
        self.frames.append(in_data)
        return None, self.pyaudio_module.paContinue

    def record(self):
        """
        Record audio.
        """
        assert self.stream is None, "This speech recorder is already recording!"
        self.frames = []
        self.audio = self.pyaudio_module.PyAudio()
        try:
            self.stream = self.audio.open(
                input_device_index=self.device_index,
                format=self.FORMAT,
                channels=self.CHANNELS,
                rate=self.SAMPLE_RATE,
                input=True,
                frames_per_buffer=self.CHUNK,
                stream_callback=self.stream_callback
            )
        except Exception:
            self.audio.terminate()
            raise

    def stop(self, audio_file=None):
        """
        Stop recording audio.
        """
        try:
            wave_data = b''.join(self.frames)

            self.stream.stop_stream()
            self.stream.close()

            if not wave_data:
                return

            # Save the recorded data as a WAV file
            if audio_file:
                with wave.open(audio_file, 'wb') as wave_file:
                    wave_file.setnchannels(self.CHANNELS)
                    wave_file.setsampwidth(self.SAMPLE_WIDTH)
                    wave_file.setframerate(self.SAMPLE_RATE)
                    wave_file.writeframes(wave_data)
                    logger.info('Saving recorded audio to file: %s', audio_file)
        finally:
            self.audio.terminate()
            self.audio = None
            self.stream = None
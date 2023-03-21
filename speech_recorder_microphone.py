from speech_recorder import SpeechRecorder
import pyaudio
import wave
import threading


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
        self.thread_stop = None

    def record(self):
        """
        Record audio.
        """
        assert self.stream is None, "This speech recorder is already recording!"
        assert self.thread_stop is None, "This speech recorder is already recording!"
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
            )
        except Exception:
            self.audio.terminate()
            raise

        running = [True]

        def thread_listen():
            while running[0]:
                self.frames.append(self.stream.read(self.CHUNK))
        
        def thread_stop():
            running[0] = False

        thread = threading.Thread(target=thread_listen)
        thread.start()
        self.thread_stop = thread_stop
            
    def stop(self, audio_file=None):
        """
        Stop recording audio.
        """
        try:
            self.thread_stop()
            self.stream.stop_stream()
            self.stream.close()

            if not self.frames:
                return

            # Save the recorded data as a WAV file
            if audio_file:
                wf = wave.open(audio_file, 'wb')
                wf.setnchannels(self.CHANNELS)
                wf.setsampwidth(self.audio.get_sample_size(self.FORMAT))
                wf.setframerate(self.SAMPLE_RATE)
                wf.writeframes(b''.join(self.frames))
                wf.close()
        finally:
            self.stream = None
            self.thread_stop = None
            self.audio.terminate()
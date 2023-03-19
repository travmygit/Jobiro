from speech_recorder import SpeechRecorder
import speech_recognition as sr


class SrSpeechRecorder(SpeechRecorder):
    def setup(self):
        """
        Setup the speech recorder.
        """
        pass

    def record(self, duration):
        """
        Record audio for the specified duration.
        """
        # 创建识别器对象
        r = sr.Recognizer()

        # 设置录音的参数
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)  # 噪音抑制
            print("请开始说话：")
            audio = r.listen(source, phrase_time_limit=20)  # 20秒超时限制

        # 将录音保存为文件
        with open("output.wav", "wb") as f:
            f.write(audio.get_wav_data())
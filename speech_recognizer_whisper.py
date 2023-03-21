from speech_recognizer import SpeechRecognizer
import os
from app_config import config
import openai
from log import logger


class WhisperSpeechRecognizer(SpeechRecognizer):
    def setup(self):
        """
        Setup the speech recognizer.
        """
        # Setup OpenAI
        openai.api_key = config.openai_api_key

        # Setup proxies
        os.environ["http_proxy"] = config.http_proxy
        os.environ["https_proxy"] = config.https_proxy

    def translate_audio(self, audio):
        """
        Translate audio to text.
        """
        try:
            with open(audio, "rb") as f:
                response = openai.Audio.transcribe("whisper-1", f)
                text = response.text.strip()
                return text
        except FileNotFoundError:
            logger.error(f'Audio file not found: {audio}')
            raise
    
    def translate_text(self, text, source_lang, target_lang):
        """
        Translate text from source language to target language.
        """
        # Translate text
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Translate '{text}' from {source_lang} to {target_lang}:",
            temperature=0.5,
            max_tokens=1024,
            n = 1,
            stop=None,
            frequency_penalty=0,
            presence_penalty=0
        )

        # Return translated text
        translated_text = response.choices[0].text.strip()
        return translated_text
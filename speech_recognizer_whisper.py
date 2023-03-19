from speech_recognizer import SpeechRecognizer
import os
import config
import openai


class WhisperSpeechRecognizer(SpeechRecognizer):
    def setup(self):
        """
        Setup the speech recognizer.
        """
        # Get config
        conf = config.conf()

        # Setup OpenAI
        openai.api_key = conf.openai_api_key

        # Setup proxies
        os.environ["http_proxy"] = conf.http_proxy
        os.environ["https_proxy"] = conf.https_proxy

    def translate_audio(self, audio):
        """
        Translate audio to text.
        """
        return "Hello world!"
    
    def translate_text(self, text, source_lang, target_lang):
        """
        Translate text from source language to target language.
        """
        # Call OpenAI
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
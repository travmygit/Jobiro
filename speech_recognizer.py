class SpeechRecognizer(object):
    def setup(self):
        """
        Setup the speech recognizer.
        """
        raise NotImplementedError
    
    def translate_audio(self, audio):
        """
        Translate audio to text.
        """
        raise NotImplementedError
    
    def translate_text(self, text, source_lang, target_lang):
        """
        Translate text from source language to target language.
        """
        raise NotImplementedError
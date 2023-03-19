import config
from log import logger
import speech_recognizer_factory
import speech_recorder_factory


if __name__ == '__main__':
    try:
        # Load config
        config.load_config()

        # Get config
        conf = config.conf()

        logger.info('App start')

        # Create speech recorder
        speech_recorder = speech_recorder_factory.create_speech_recorder(conf.speech_recorder_type)

        # Setup speech recorder
        speech_recorder.setup()

        # Record audio
        speech_recorder.record(5)
        # quit()

        # Create speech recognizer
        speech_recognizer = speech_recognizer_factory.create_speech_recognizer(conf.speech_recognizer_type)

        # Setup speech recognizer
        speech_recognizer.setup()

        # Translate audio to text
        text = speech_recognizer.translate_audio(conf.audio_file)

        # Log text
        logger.info(f'Text: {text}' if text else 'No text found')

        # Translate text from source language to target language
        translated_text = speech_recognizer.translate_text(text, conf.source_lang, conf.target_lang)

        # Log translated text
        logger.info(f'Translated text: {translated_text}')

        logger.info('App end')
    except Exception as e:
        logger.error('App start failed')
        logger.exception(e)
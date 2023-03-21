from app_config import config
from log import logger
import keyboard
import speech_recognizer_factory
import speech_recorder_factory


is_recording = False
is_running = True


def on_record_start(_):
    """
    Start recording audio.
    """
    global is_recording, speech_recorder

    if not is_recording:
        is_recording = True
        speech_recorder.record()


def on_record_stop(_):
    """
    Stop recording audio.
    """
    global is_recording, speech_recorder

    if is_recording:
        is_recording = False
        speech_recorder.stop()


if __name__ == '__main__':
    try:
        # Create speech recorder
        speech_recorder = speech_recorder_factory.create_speech_recorder(config.speech_recorder_type)

        # Setup speech recorder
        speech_recorder.setup()

        # # Record audio
        # speech_recorder.record(5)

        # Create speech recognizer
        speech_recognizer = speech_recognizer_factory.create_speech_recognizer(config.speech_recognizer_type)

        # Setup speech recognizer
        speech_recognizer.setup()

        # # Translate audio to text
        # text = speech_recognizer.translate_audio(conf.audio_file)

        # # Log text
        # logger.info(f'Text: {text}' if text else 'No text found')

        # # Translate text from source language to target language
        # translated_text = speech_recognizer.translate_text(text, conf.source_lang, conf.target_lang)

        # # Log translated text
        # logger.info(f'Translated text: {translated_text}')

        keyboard.on_press_key(config.record_key, on_record_start)
        keyboard.on_release_key(config.record_key, on_record_stop)

        logger.info('App start')

        keyboard.wait('esc')

        logger.info('App end')
    except Exception as e:
        logger.error('App start failed')
        logger.exception(e)
def create_speaker_avatar(avatar_type):
    """
    Create a speaker avatar of the given type.
    """
    if avatar_type == "hint":
        from speaker_avatar_hint import HintSpeakerAvatar
        return HintSpeakerAvatar()
    elif avatar_type == "voicevox":
        from speaker_avatar_voicevox import VoiceVoxSpeakerAvatar
        return VoiceVoxSpeakerAvatar()
    else:
        raise Exception("Unknown speaker avatar type: " + avatar_type)
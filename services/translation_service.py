from deep_translator import GoogleTranslator

def translate(text, lang):
    if not text:
        return ""
    return GoogleTranslator(source='auto', target=lang).translate(text)
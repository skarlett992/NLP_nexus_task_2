import langid as langid
import pycountry

def detect_languages(text):
    print(f'run detect_languages., args: text: {text}')
    language = langid.classify(' '.join(text))
    # convert code from ISO 639-1 to ISO 639-2
    langs = pycountry.languages.get(alpha_2=language[0]).alpha_3
    print(f'finish detect_languages., returns: {langs}')
    return langs
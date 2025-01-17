import json
from pandas import json_normalize
import requests


def ocr_space_file(filename, overlay=False, api_key='K88833829588957', language='eng'):
    """ OCR.space API request with local file.
        Python3.5 - not tested on 2.7
    :param filename: Your file path & name.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()


def new_func(filename, api_key, language):
    test_file = ocr_space_file(filename, api_key = api_key, language = language)
    result = json.loads(test_file)
    df = json_normalize(result['ParsedResults'])
    text = df['ParsedText'].str.replace('\r\n', ' ')
    text = str(text)
    with open('output.txt', 'w') as f:
        f.write(text)


file_name = 'life_is_short.jpg'
api_key = 'K88833829588957'
language = 'pol'

new_func(file_name, api_key, language)

